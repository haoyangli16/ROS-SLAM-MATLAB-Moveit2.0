#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy, sys
import tf
import math
import cmd
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
import csv

# move_base
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseWithCovarianceStamped
from actionlib_msgs.msg import *

# moveit_group
import moveit_commander
from moveit_commander import MoveGroupCommander
from geometry_msgs.msg import Pose
from copy import deepcopy

"""
该程序用来实现全流程仿真操作
包括自动升降机械臂，自主导航，机械臂挖掘
"""
# Topics
TOPIC_BASE_PLANAR = '/cmd_vel'

PI = 3.141592653589

# Default move speed
DEFAULT_SPEED_LIN = 1.8
DEFAULT_SPEED_ANG = 0.1
destination = [(11.0, 4.7, 0.393328), (0.000, 0.000, PI/2)]
init_joint_position=[0,-40, 0, 0] #定义初始姿态

# Navigation function
def goal_pose_transfer(pose):
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


def get_twist(length_x, length_y, angle_z):
    msg = Twist()
    if length_x != 0:
        msg.linear.x = (length_x / math.fabs(length_x)) * DEFAULT_SPEED_LIN
    else:
        msg.linear.x = 0

    if length_y != 0:
        msg.linear.y = (length_y / math.fabs(length_y)) * DEFAULT_SPEED_LIN
    else:
        msg.linear.y = 0

    if angle_z != 0:
        msg.angular.z = (angle_z / math.fabs(angle_z)) * DEFAULT_SPEED_ANG
    else:
        msg.angular.z = 0
    rospy.loginfo("Twist now is (" + str(msg.linear.x) + " " + str(msg.linear.y) + " " + str(msg.angular.z) + ")")
    return msg


def get_duration(length, speed):
    return float(math.fabs(length / speed))


def move_dipan(pub, msg, duration):
    pub.publish(msg)
    rospy.sleep(duration)
    msg_init = get_twist(0.0, 0.0, 0.0)
    pub.publish(msg_init)


def angle_to_rad(joint_list):
    # 将导入的角度列表转化为弧度列表
    new_list = joint_list[:]
    for rank in range(0, len(joint_list)):
        if type(joint_list[rank]) == int:
            new_list[rank] = float(joint_list[rank] * PI / 180)
    return new_list


class BaseMoveCalculator():
    """该类用来根据目标位置控制底盘的运动"""

    def __init__(self):
        self.pub_cmd = rospy.Publisher(TOPIC_BASE_PLANAR, Twist, queue_size=10)

    def move_command(self, length_x, length_y, angle_z):
        msg = get_twist(length_x, length_y, angle_z)
        if length_x != 0:
            duration = get_duration(length_x, DEFAULT_SPEED_LIN)
            rospy.loginfo("duration is length_x / DEFAULT_SPEED_LIN = " + str(duration) + " s")
        elif length_y != 0:
            duration = get_duration(length_y, DEFAULT_SPEED_LIN)
            rospy.loginfo("duration is length_y / DEFAULT_SPEED_LIN = " + str(duration) + " s")
        else:
            duration = get_duration(angle_z, DEFAULT_SPEED_ANG)
            rospy.loginfo("duration is angle_z / DEFAULT_SPEED_LIN = " + str(duration) + " s")

        move_dipan(self.pub_cmd, msg, duration)

    def stop_move(self):
        speed = get_twist(0.0, 0.0, 0.0)
        self.pub_cmd.publish(speed)

    def nav_to_point(self, pose):
        # 创建MoveBaseAction client
        client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        # 等待MoveBaseAction server启动
        client.wait_for_server()
        # 开始导航
        # try:
        rospy.sleep(1)
        goal = goal_pose_transfer(pose)
        client.send_goal(goal)
        client.wait_for_result()
        rospy.sleep(2)
        rospy.loginfo("Nav to destination finished.")


class Excavator():
    """该类用来控制挖掘机铲斗控制链的运动"""

    def __init__(self):
        # 初始化ROS节点
        rospy.init_node('wajue_process', anonymous=True)
        # 初始化参数
        self.joint_value_list = []

    def data_transfer(self, fl_name):
        """输入csv文件的完整文件名，返回一个包含所有路点数据的嵌套列表"""
        filename = 'catkin_ws/src/pudong_gazebo/scripts/waypoint_dates/' + fl_name
        dates = []
        with open(filename, 'r') as waypoints:
            reader = csv.reader(waypoints)
            for i, row in enumerate(reader):
                dates.append(row)

        joint_value = [0.0, 0.0, 0.0, 0.0]

        for data in dates:
            for i in range(0, 4):
                joint_value[i] = float(data[i].strip())
            joint_value_transfer = joint_value[:]
            self.joint_value_list.append(joint_value_transfer)

        # print self.joint_value_list

    def excavator_joint_waypoints_command(self):
        """根据joint_value_list执行挖掘机应经过的点位"""
        moveit_commander.roscpp_initialize(sys.argv)
        arm = moveit_commander.MoveGroupCommander('wajueji')
        arm.set_goal_joint_tolerance(0.001)
        arm.set_max_acceleration_scaling_factor(1.0)
        arm.set_max_velocity_scaling_factor(1.0)
        arm.allow_replanning(True)

        for joint_positions in self.joint_value_list:
            print (joint_positions)
            arm.set_start_state_to_current_state()
            arm.set_joint_value_target(angle_to_rad(joint_positions))
            arm.go()
            arm.stop()

    def single_joint_positions_command(self, joint1, joint2, joint3, joint4, max_vel=1.0):
        """到达目标点位，角度或弧度都可以"""
        moveit_commander.roscpp_initialize(sys.argv)
        arm = moveit_commander.MoveGroupCommander('wajueji')
        arm.set_goal_joint_tolerance(0.001)
        arm.set_max_acceleration_scaling_factor(1.0)
        arm.set_max_velocity_scaling_factor(max_vel)
        arm.set_start_state_to_current_state()
        joint_positions = [joint1, joint2, joint3, joint4]
        arm.set_joint_value_target(angle_to_rad(joint_positions))
        arm.go()
        arm.stop()

    def multi_joint_positions_command(self, joint1):
        """底座与车身位置固定时的挖掘规划"""
        moveit_commander.roscpp_initialize(sys.argv)
        arm = moveit_commander.MoveGroupCommander('wajueji')
        arm.set_goal_joint_tolerance(0.001)
        arm.set_max_acceleration_scaling_factor(1.0)
        arm.set_max_velocity_scaling_factor(0.5)

        joint_positions = [joint1, -0.593412, 0.872665, 0.209436]
        arm.set_joint_value_target(angle_to_rad(joint_positions))
        arm.go()
        arm.stop()
        joint_positions = [joint1, -0.069813, -0.488692, -0.471239]
        arm.set_joint_value_target(angle_to_rad(joint_positions))
        arm.go()
        arm.stop()
        joint_positions = [joint1, 0.069813, -0.383972, -0.471239]
        arm.set_joint_value_target(angle_to_rad(joint_positions))
        arm.go()
        arm.stop()
        joint_positions = [joint1, 0.069813, -0.226893, 0.174533]
        arm.set_joint_value_target(angle_to_rad(joint_positions))
        arm.go()
        arm.stop()
        joint_positions = [joint1, -0.104720, -0.0, 0.575959]
        arm.set_joint_value_target(angle_to_rad(joint_positions))
        arm.go()
        arm.stop()

    def list_command(self):
        # 一次挖掘
        self.joint_value_list = [[6, -30, 0, 35], [6, -15, 0, -19], [6, -10, 0, -55 ], [6, -2, 0, -55],[6, -2, 0, 18],[6, -15, 0, 45],[55, -15, 0, 45],[55, -7, 0, 30],[55, -9, 0, -24],[55, -3, 0, -63],[55, -15, 0, 35],[0, -15, 0, 35],[0, -30, 0, 35]]
        self.excavator_joint_waypoints_command()



if __name__ == '__main__':
    ex = Excavator()
    bmc = BaseMoveCalculator()
    pose=angle_to_rad(init_joint_position)
    ex.single_joint_positions_command(pose[0], pose[1],pose[2],pose[3])
    bmc.nav_to_point(destination)
    ex.list_command()

