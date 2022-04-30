#!/usr/bin/env python
# coding=utf-8

import roslib
import rospy
import tf
# Set_model_state 该话题用的是ModelState类型的话题
from gazebo_msgs.msg import ModelState

TOPIC_TO_SET = '/gazebo/set_model_state'
point1 = [(11.168240, 1.775917, 0.393328), (0.000, 0.001930, 1.589976)]


class MPControl():
    def __init__(self):
        rospy.init_node('model_position_control')
        nodename = rospy.get_name()
        rospy.loginfo("%s started" % nodename)

        self.pub_set = rospy.Publisher(TOPIC_TO_SET, ModelState, queue_size=10)

        self.rate = rospy.get_param("~rate", 10)
        # self.timeout_ticks = rospy.get_param("~timeout_ticks", 2)
        self.ticks_since_target = 0
        # 设置挖掘机挖掘位置
        self.model_final_state = ModelState()
        self.model_final_state.model_name = 'pudong'
        self.model_final_state.pose.position.x = point1[0][0]
        self.model_final_state.pose.position.y = point1[0][1]
        self.model_final_state.pose.position.z = point1[0][2]
        x, y, z, w = tf.transformations.quaternion_from_euler(point1[1][0], point1[1][1], point1[1][2])
        self.model_final_state.pose.orientation.x = x
        self.model_final_state.pose.orientation.y = y
        self.model_final_state.pose.orientation.z = z
        self.model_final_state.pose.orientation.w = w
        self.model_final_state.twist.linear.x = 0.0
        self.model_final_state.twist.linear.y = 0.0
        self.model_final_state.twist.linear.z = 0.0
        self.model_final_state.twist.angular.x = 0.0
        self.model_final_state.twist.angular.y = 0.0
        self.model_final_state.twist.angular.z = 0.0
        self.model_final_state.reference_frame = 'world'

    def spin(self):
        r = rospy.Rate(self.rate)
        idle = rospy.Rate(10)
        then = rospy.Time.now()
        # self.ticks_since_target = self.timeout_ticks

        # main loop
        while not rospy.is_shutdown():
            while not rospy.is_shutdown():
                self.spinOnce()
                r.sleep()
            idle.sleep()

    def spinOnce(self):
        self.pub_set.publish(self.model_final_state)


if __name__ == '__main__':
    mpc = MPControl()
    mpc.spin()
