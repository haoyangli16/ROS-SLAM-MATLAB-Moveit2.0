#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy, sys
import tf
import math
import cmd
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
import csv
import numpy as np

# move_base
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseWithCovarianceStamped
from actionlib_msgs.msg import *

# Topics
TOPIC_BASE_PLANAR = '/cmd_vel'


# Navigation function
def goal_pose(pose):
    goal_pose = MoveBaseGoal()
    goal_pose.target_pose.header.frame_id = "map"
    goal_pose.target_pose.pose.position.x = pose[0][0]
    goal_pose.target_pose.pose.position.y = pose[0][1]
    goal_pose.target_pose.pose.position.z = pose[0][2]

    x, y, z, w = tf.transformations.quaternion_from_euler(pose[1][0], pose[1][1], pose[1][2])

    goal_pose.target_pose.pose.orientation.x = x
    goal_pose.target_pose.pose.orientation.y = y
    goal_pose.target_pose.pose.orientation.z = z
    goal_pose.target_pose.pose.orientation.w = w
    return goal_pose


class BaseMoveCalculator():
    """该类用来根据目标位置控制底盘的运动"""

    def __init__(self):
        rospy.init_node('test_nav', anonymous=True)
        self.pub_cmd = rospy.Publisher(TOPIC_BASE_PLANAR, Twist, queue_size=10)
        self.point1 = [(11.4000, 1.80, 0.39), (0.000, 0.000, 1.57)]
        self.point2 = [(11.5000, 1.77, 0.39), (0.000, 0.000, 1.50)]
        self.point3 = [(11.1700, 1.80, 0.39), (0.000, 0.000, 1.59)]
        self.point4 = [(11.4000, 1.75, 0.39), (0.000, 0.000, 1.54)]
        self.point5 = [(11.1700, 1.80, 0.39), (0.000, 0.000, 1.59)]
        self.point6 = [(11.3600, 1.85, 0.39), (0.000, 0.000, 1.30)]
        self.point7 = [(11.5000, 1.79, 0.39), (0.000, 0.000, 1.50)]
        self.point8 = [(11.1700, 1.80, 0.39), (0.000, 0.000, 1.59)]
        self.point9 = [(11.1000, 1.88, 0.39), (0.000, 0.000, 1.80)]
        self.point10 = [(11.1700, 1.80, 0.39), (0.000, 0.000, 1.59)]
        self.point_list = [self.point1, self.point2, self.point3, self.point4, self.point5, self.point6, self.point7,
                           self.point8, self.point9, self.point10]

    def nav_to_point(self):
        # 创建MoveBaseAction client
        client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        # 等待MoveBaseAction server启动
        client.wait_for_server()
        # 开始导航
        """
        for point in self.point_list:
            goal = goal_pose(point)
            client.send_goal(goal)
            print "Now change the goal point."
            rospy.sleep(4)
        """
        goal = goal_pose(self.point10)
        client.send_goal(goal)

        client.wait_for_result()
        rospy.sleep(2)
        rospy.loginfo("Nav to point finished.")


if __name__ == '__main__':
    bmc = BaseMoveCalculator()
    bmc.nav_to_point()
