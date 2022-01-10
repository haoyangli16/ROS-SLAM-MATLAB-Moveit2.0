#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy, sys
import moveit_commander

PI = 3.1415926535

def angle_to_rad(joint_list):
    # 将导入的角度列表转化为弧度列表
    new_list = joint_list[:]
    for rank in range(0, len(joint_list)):
        if type(joint_list[rank]) == int:
            new_list[rank] = float(joint_list[rank] * PI / 180)
    return new_list

class MoveItFkDemo:
    def __init__(self):
        # 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        joint_positions1 = [0, -40, 0, 35]
        joint_positions2 = [0, -30, 0, 0]     
        joint_positions3 = [0, -15, 0, -40]  
        joint_positions4 = [0, -6, 0, -49]   
        joint_positions5 = [0, -10, 11, 35]   
        joint_positions6 = [0, -40, 35, 35]
        joint_positions7 = [40, -40, 35, 35]
        joint_positions8 = [40, -20, 15, 35]
        joint_positions9 = [40, -5, 6, 35]
        joint_positions10 = [40, -5, 1, 35]
        joint_positions11 = [40, -5, 1, -49]
        joint_positions12 = [40, -30, 35, 30]
        joint_positions13 = [0, -35, 0, -30]
        joint_value_list = [joint_positions1, joint_positions2, joint_positions3, joint_positions4, joint_positions5, joint_positions6, joint_positions7, joint_positions8, joint_positions9,joint_positions10,joint_positions11,joint_positions12,joint_positions13]
        for joint_positions in joint_value_list:
            moveit_commander.roscpp_initialize(sys.argv)
            rospy.init_node('moveit_fk_demo', anonymous=True)
            arm = moveit_commander.MoveGroupCommander('wajueji')
            arm.allow_replanning(True)
            arm.set_goal_joint_tolerance(0.001)
            arm.set_max_acceleration_scaling_factor(1.0)
            arm.set_max_velocity_scaling_factor(1.0)
            print(joint_positions)
            arm.set_joint_value_target(angle_to_rad(joint_positions))
            result=arm.set_joint_value_target(angle_to_rad(joint_positions))
            rospy.loginfo(str(result))
            arm.go()
            arm.stop()
       
if __name__ == "__main__":
    try:
        MoveItFkDemo()
    except rospy.ROSInterruptException:
        pass
