#!/usr/bin/env python
# -*- coding:utf-8   -*-

import roslib
import rospy
import tf
from gazebo_msgs.msg import ModelStates
from gazebo_msgs.msg import ModelState
from gazebo_msgs.msg import LinkStates
from std_msgs.msg import Float64


class NumberStatistics():
    """统计在原本区域内的石块个数，并实时显示出总共的和现在还剩下的"""

    def __init__(self):
        rospy.init_node('number_statistic')
        nodename = rospy.get_name()
        rospy.loginfo("%s started" % nodename)

        rospy.Subscriber('gazebo/model_states', ModelStates, self.twistCallback)
        self.pub_set = rospy.Publisher('gazebo/set_model_state', ModelState, queue_size=10)
        self.model_final_state = ModelState()
        self.msg = ModelStates()

        self.ticks_since_target = 0

        self.rate = rospy.get_param("~rate", 5)
        self.timeout_ticks = rospy.get_param("~timeout_ticks", 2)

        self.whole_numbers = 0
        self.last_numbers = 0
        self.in_chandou_numbers = 0
        self.out_numbers = 0
        # 设置除了石块以外的模型个数
        self.number_of_other_models = 7

        self.last_in_chandou_numbers = 0
        # 设置self.last_out_numbers初始值为1，则刚开始可以先输出一次所有的个数
        self.last_out_numbers = 1

    def spin(self):
        """该函数可以在ROS中无限循环，并通过spinOnce()函数实时接收数据"""
        r = rospy.Rate(self.rate)
        idle = rospy.Rate(5)
        then = rospy.Time.now()
        self.ticks_since_target = self.timeout_ticks

        while not rospy.is_shutdown():

            while not rospy.is_shutdown() and self.ticks_since_target < self.timeout_ticks:
                self.spinOnce()
                r.sleep()
            idle.sleep()

    def spinOnce(self):
        self.ticks_since_target += 1

    def screen_show(self):
        rospy.loginfo("Whole numbers of stones:  " + str(self.whole_numbers))
        rospy.loginfo("Stones in circle now:     " + str(self.last_numbers))
        rospy.loginfo("Stones in excavator now:  " + str(self.in_chandou_numbers))
        rospy.loginfo("Stones out of circle now: " + str(self.out_numbers))

    def position_out(self, model_name):
        self.model_final_state.model_name = model_name
        self.model_final_state.pose.position.x = 16.0
        self.model_final_state.pose.position.y = 2.6
        self.model_final_state.pose.position.z = 0.05
        self.model_final_state.pose.orientation.x = 0.0
        self.model_final_state.pose.orientation.y = 0.0
        self.model_final_state.pose.orientation.z = 0.0
        self.model_final_state.pose.orientation.w = 1.0
        self.model_final_state.twist.linear.x = 0.0
        self.model_final_state.twist.linear.y = 0.0
        self.model_final_state.twist.linear.z = 0.0
        self.model_final_state.twist.angular.x = 0.0
        self.model_final_state.twist.angular.y = 0.0
        self.model_final_state.twist.angular.z = 0.0
        self.model_final_state.reference_frame = 'world'

    def twistCallback(self, msg):
        self.ticks_since_target = 0
        self.msg = msg
        self.last_numbers = 0
        self.in_chandou_numbers = 0
        self.out_numbers = 0
        self.whole_numbers = len(msg.name) - self.number_of_other_models

        poses = self.msg.pose

        # 判断石块是否在范围内，并统计个数
        for rank in range(0, len(poses)):
            # 石块应处于的范围
            x = 8.0 < poses[rank].position.x < 14.0
            y = 4.0 < poses[rank].position.y < 10.0
            z = -0.5 < poses[rank].position.z < 1.5
            """
            # 被推出圈后的修正范围
            x1 = 8.0 < poses[rank].position.x < 14
            y1 = 4.1 < poses[rank].position.x < 9.5
            z1 = -0.5 < poses[rank].position.z < 0.05
            t1 = not (x and y)
            # 修正,将在该范围内的球认为是模型误差，直接放置在最终框内
            # if x1 and y1 and z1 and t1:
                # model_name = names[rank]
                # self.position_out(model_name)
                # self.pub_set.publish(self.model_final_state)
            """
            # 统计个数
            if x and y and z:
                self.last_numbers += 1
            elif not z:
                self.in_chandou_numbers += 1
            if (x == False or y == False) and z:
                self.out_numbers += 1

        # 减去除了石块以外的物体个数，如挖掘机和墙体、房子
        self.out_numbers -= self.number_of_other_models

        # 如果铲斗内或者圈外的石头数目改变，则更新一下石头个数
        if (self.out_numbers != self.last_out_numbers) or (self.in_chandou_numbers != self.last_in_chandou_numbers):
            self.screen_show()

        self.last_out_numbers = self.out_numbers
        self.last_in_chandou_numbers = self.in_chandou_numbers


if __name__ == '__main__':
    ns = NumberStatistics()
    ns.spin()
