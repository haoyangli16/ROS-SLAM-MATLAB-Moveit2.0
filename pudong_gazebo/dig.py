#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
该程序用来实现挖掘机机械臂的自动挖掘动作
'''
import rospy, sys
import moveit_commander
PI = 3.1415926535898

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
        joint_positions1 = [6, -30, 0, 35]    #挖掘初始位置
        joint_positions2 = [6, -15, 0, -19]   #挖掘中间位置
        joint_positions3 = [6, -10, 0, -55 ] #挖掘准备
        joint_positions4 = [6, -2, 0, -55]   #挖掘初始 
        joint_positions5 = [6, -2, 0, 18]    #挖掘结束
        
        joint_positions6 = [6, -15, 0, 45] #下料高度位置
        joint_positions7 = [55, -15, 0, 45] #旋转下料高度
        joint_positions8 = [55, -7, 0, 30] #下料准备
        joint_positions9 = [55, -9, 0, -24] #下料初始
        joint_positions10 = [55, -3, 0, -63] #下料结束
        
        joint_positions11 = [55, -15, 0, 35] #运输高度位置
        joint_positions12 = [0, -15, 0, 35] #旋转运输高度
        joint_positions13 = [0, -30, 0, 35] #回归挖掘初始

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
