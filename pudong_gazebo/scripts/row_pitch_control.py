#!/usr/bin/env python
# coding=utf-8

import roslib
import rospy
from gazebo_msgs.msg import ModelStates
# Set_model_state 该话题用的是ModelState类型的话题
from gazebo_msgs.msg import ModelState
from std_msgs.msg import Float64

TOPIC_TO_SET = '/gazebo/set_model_state'


class RPControl():
    def __init__(self):
        rospy.init_node('row_pitch_control')
        nodename = rospy.get_name()
        rospy.loginfo("%s started" % nodename)

        rospy.Subscriber('gazebo/model_states', ModelStates, self.twistCallback)
        self.pub_set = rospy.Publisher(TOPIC_TO_SET, ModelState, queue_size=10)

        self.rate = rospy.get_param("~rate", 30)
        self.timeout_ticks = rospy.get_param("~timeout_ticks", 2)
        self.ticks_since_target = 0

        self.x = 0.0
        self.y = 0.0
        self.model_state = ModelState()
        self.model_state.model_name = 'pudong'
        self.model_state.reference_frame = 'world'

    def spin(self):
        r = rospy.Rate(self.rate)
        idle = rospy.Rate(10)
        then = rospy.Time.now()
        self.ticks_since_target = self.timeout_ticks

        # main loop
        while not rospy.is_shutdown():

            while not rospy.is_shutdown() and self.ticks_since_target < self.timeout_ticks:
                self.spinOnce()
                r.sleep()
            idle.sleep()

    def spinOnce(self):
        self.ticks_since_target += 1

        if self.x != 0.0 or self.y != 0.0:
            self.model_state.pose.orientation.x = 0.0
            self.model_state.pose.orientation.y = 0.0
            self.pub_set.publish(self.model_state)

    def twistCallback(self, msg):
        self.ticks_since_target = 0

        # 获取'pudong'所在的排名位次rank，方便之后获取其位置和速度信息
        rank = 0
        tick = 0
        for name in msg.name:
            if name == 'pudong':
                rank = tick
            tick += 1
        # print('Rank is: ' + str(rank))

        self.model_state.pose = msg.pose[rank]
        self.model_state.twist = msg.twist[rank]
        self.x = msg.pose[rank].orientation.x
        self.y = msg.pose[rank].orientation.y


if __name__ == '__main__':
    rpc = RPControl()
    rpc.spin()
