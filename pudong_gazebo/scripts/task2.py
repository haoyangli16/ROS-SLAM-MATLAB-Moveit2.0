#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy, sys
import tf
import math
import cmd
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
# move_base规划所需库
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseWithCovarianceStamped
from actionlib_msgs.msg import *
# moveit规划所需库
import moveit_commander
from moveit_commander import MoveGroupCommander
from geometry_msgs.msg import Pose
from copy import deepcopy

# Topics
TOPIC_BASE_PLANAR = '/cmd_vel'
# Default move speed
DEFAULT_SPEED_LIN = 1.5
DEFAULT_SPEED_ANG = 0.05


### Move functions ###
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


class Excavator:
    def __init__(self):
        # 初始化ROS节点
        rospy.init_node('wajue_process', anonymous=True)
        # 初始化参数
        self.pub_cmd = rospy.Publisher(TOPIC_BASE_PLANAR, Twist, queue_size=10)

    # Base move command, only support for one moving direction
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

    # Main body of excavator command
    def excavator_command_1(self, joint1, joint2, joint3, joint4):
        moveit_commander.roscpp_initialize(sys.argv)
        arm = moveit_commander.MoveGroupCommander('wajueji_controller')
        arm.set_goal_joint_tolerance(0.001)
        arm.set_max_acceleration_scaling_factor(1.0)
        arm.set_max_velocity_scaling_factor(0.5)

        joint_positions = [joint1, joint2, joint3, joint4]
        arm.set_joint_value_target(joint_positions)
        arm.go()
        rospy.sleep(1)

    def excavator_command_2(self, joint1):
        moveit_commander.roscpp_initialize(sys.argv)
        arm = moveit_commander.MoveGroupCommander('wajueji_controller')
        arm.set_goal_joint_tolerance(0.001)
        arm.set_max_acceleration_scaling_factor(1.0)
        arm.set_max_velocity_scaling_factor(0.5)

        joint_positions = [joint1, -0.279253, -0.017453, -0.872665]
        arm.set_joint_value_target(joint_positions)
        arm.go()
	arm.stop()
        # rospy.sleep(0.1)
        joint_positions = [joint1, -0.191986, -0.191986, -0.680678]
        arm.set_joint_value_target(joint_positions)
        arm.go()
	arm.stop()
        # rospy.sleep(0.1)
        joint_positions = [joint1, -0.069813, 0.017453, -0.994838]
        arm.set_joint_value_target(joint_positions)
        arm.go()
	arm.stop()
        # rospy.sleep(0.1)
        joint_positions = [joint1, -0.017453, 0.017453, -0.645772]
        arm.set_joint_value_target(joint_positions)
        arm.go()
	arm.stop()
        # rospy.sleep(0.1)
        joint_positions = [joint1, -0.052360, 0.209440, -0.715585]
        arm.set_joint_value_target(joint_positions)
        arm.go()
        # rospy.sleep(0.1)
        joint_positions = [joint1, -0.087266, 0.558505, -0.733038]
        arm.set_joint_value_target(joint_positions)
        arm.go()
        # rospy.sleep(0.1)
        joint_positions = [joint1, -0.191986, 0.680678, 0.052360]
        arm.set_joint_value_target(joint_positions)
        arm.go()
        # rospy.sleep(0.1)

    def excavator_command_route(self):
        moveit_commander.roscpp_initialize(sys.argv)
        arm = moveit_commander.MoveGroupCommander('wajueji_controller')
        arm.set_goal_joint_tolerance(0.001)
        arm.set_max_acceleration_scaling_factor(1.0)
        arm.set_max_velocity_scaling_factor(0.5)

        joint_positions = [0, -0.279253, -0.017453, -0.872665]
        arm.set_joint_value_target(joint_positions)
        arm.go()
        rospy.sleep(0.1)
        joint_positions = [0, -0.278505994, -0.011476999, -0.864746786]
        arm.set_joint_value_target(joint_positions)
        arm.go()
        rospy.sleep(0.1)
        joint_positions = [0, -0.274198495, 0.022982748, -0.819087552]
        arm.set_joint_value_target(joint_positions)
        arm.go()
        rospy.sleep(0.1)
        joint_positions = [0, -0.265021498, 0.096398203, -0.721811923]
        arm.set_joint_value_target(joint_positions)
        arm.go()
        rospy.sleep(0.1)
        joint_positions = [0, -0.251550964, 0.204161705, -0.579025064]
        arm.set_joint_value_target(joint_positions)
        arm.go()
        rospy.sleep(0.1)
        joint_positions = [0, -0.2356195, 0.3316125, -0.4101525]
        arm.set_joint_value_target(joint_positions)
        arm.go()
        rospy.sleep(0.1)
        joint_positions = [0, -0.219688036, 0.459063295, -0.241279936]
        arm.set_joint_value_target(joint_positions)
        arm.go()
        rospy.sleep(0.1)
        joint_positions = [0, -0.206217502, 0.566826797, -0.098493077]
        arm.set_joint_value_target(joint_positions)
        arm.go()
        rospy.sleep(0.1)
        joint_positions = [0, -0.197040505, 0.640242252, -0.001217448]
        arm.set_joint_value_target(joint_positions)
        arm.go()
        rospy.sleep(0.1)
        joint_positions = [0, -0.192733006, 0.674701999, 0.044441786]
        arm.set_joint_value_target(joint_positions)
        arm.go()
        rospy.sleep(0.1)
        joint_positions = [0, -0.191986, 0.680678, 0.05236]
        arm.set_joint_value_target(joint_positions)
        arm.go()
        rospy.sleep(0.1)

    def excavator_cartesian_move(self):
        # 初始化move_group的API
        moveit_commander.roscpp_initialize(sys.argv)

        cartesian = rospy.get_param('~cartesian', True)
        arm = MoveGroupCommander('wajueji_controller')
        arm.allow_replanning(True)
        arm.set_pose_reference_frame('base_link')
        arm.set_goal_position_tolerance(0.01)
        arm.set_goal_orientation_tolerance(0.01)
        arm.set_max_acceleration_scaling_factor(0.5)
        arm.set_max_velocity_scaling_factor(0.5)
        end_effector_link = arm.get_end_effector_link()

        # 控制机械臂到第一喷漆位置
        arm.set_named_target('pose1')
        arm.go()
        rospy.sleep(1)

        # 获取当前位姿数据最为机械臂运动的起始位姿
        start_pose = arm.get_current_pose(end_effector_link).pose
                
        # 初始化路点列表
        waypoints = []
        #拷贝对象
        wpose = deepcopy(start_pose)

        #process 1
        wpose.position.x -= 1.0

        if cartesian:  
            waypoints.append(deepcopy(wpose))
        else:        
            arm.set_pose_target(wpose) 
            arm.go()
            rospy.sleep(0.1)

        #process 2
        wpose.position.x += 0.5
 
        if cartesian:
            waypoints.append(deepcopy(wpose))
        else:
            arm.set_pose_target(wpose)
            arm.go()
            rospy.sleep(0.1)

        #process 3
        wpose.position.z += 0.5

        if cartesian:  
            waypoints.append(deepcopy(wpose))
        else:        
            arm.set_pose_target(wpose) 
            arm.go()
            rospy.sleep(0.1)

        #process 4
        wpose.position.z -= 0.5
        wpose.position.x += 0.5

        if cartesian:  
            waypoints.append(deepcopy(wpose))
        else:        
            arm.set_pose_target(wpose) 
            arm.go()
            rospy.sleep(0.1)

        #规划过程
        if cartesian:
		fraction = 0.0  
		maxtries = 200 
		attempts = 0  

		arm.set_start_state_to_current_state()

		while fraction < 1.0 and attempts < maxtries:

		    (plan, fraction) = arm.compute_cartesian_path (
		                            waypoints,   
		                            0.01,       
		                            0.0,        
		                            True)       
		    
		    attempts += 1
		    # 打印运动规划进程
		    if attempts % 10 == 0:
		        rospy.loginfo("Still trying after " + str(attempts) + " attempts...")
		             
		# 如果路径规划成功（覆盖率100%）,则开始控制机械臂运动
		if fraction == 1.0:
		    rospy.loginfo("Path computed successfully. Moving the arm.")
		    arm.execute(plan)
		    rospy.loginfo("Path execution complete.")
		# 如果路径规划失败，则打印失败信息
		else:
		    rospy.loginfo("Path planning failed with only " + str(fraction) + " success after " + str(maxtries) + " attempts.")  

		rospy.sleep(1)

        # 控制机械臂先回到初始化位置
        arm.set_named_target('init_pose')
        arm.go()
        rospy.sleep(0.1)
        
        arm.set_named_target('init_pose')
        arm.go()
        rospy.sleep(0.1)

if __name__ == '__main__':
    ex = Excavator()
    '''
    ex.excavator_command_1(0.0, -0.593412, 0.872665, 0.2094395)
    rospy.sleep(0.1)
    ex.move_command(0.0, 0.0, -0.8)
    rospy.sleep(0.1)
    ex.move_command(8.0, 0.0, 0.0)
    rospy.sleep(0.1)
    ex.move_command(0.0, 0.0, -0.75)
    rospy.sleep(0.1)
    ex.move_command(16.0, 0.0, 0.0)
    rospy.sleep(0.1)
    ex.move_command(0.0, 0.0, 0.3)
    rospy.sleep(0.1)
    ex.move_command(1.0, 0.0, 0.0)
    rospy.sleep(0.1)
    ex.move_command(0.0, 0.0, 0.3)
    rospy.sleep(0.1)
    ex.move_command(1.0, 0.0, 0.0)
    rospy.sleep(0.1)
    ex.move_command(0.0, 0.0, 1.4)
    rospy.sleep(0.1)
    ex.move_command(4.0, 0.0, 0.0)
    rospy.sleep(0.1)
    ex.move_command(0.0, 0.0, 0.75)
    rospy.sleep(0.1)
    ex.move_command(3.0, 0.0, 0.0)
    rospy.sleep(0.1)
    ex.move_command(0.0, 0.0, 0.3)
    rospy.sleep(0.1)
    ex.move_command(3.0, 0.0, 0.0)
    rospy.sleep(0.1)
    ex.move_command(0.0, 0.0, 0.25)
    rospy.sleep(0.1)
    ex.move_command(10.0, 0.0, 0.0)
    rospy.sleep(0.1)
    '''
    ex.excavator_command_2(0.0)
    rospy.sleep(0.1)

