#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy, sys
import moveit_commander

PI = 3.14159265


def angle_to_rad(joint_list):
    # 将导入的角度列表转化为弧度列表
    new_list = joint_list[:]
    for rank in range(0, len(joint_list)):
        if type(joint_list[rank]) == int:
            new_list[rank] = float(joint_list[rank] * PI / 180)
    return new_list


class MoveItFkDemo:
    def __init__(self):
        # 初始化move_group的API
        moveit_commander.roscpp_initialize(sys.argv)

        # 初始化ROS节点
        rospy.init_node('moveit_fk_demo', anonymous=True)
 
        # 初始化需要使用move group控制的机械臂中的arm group
        arm = moveit_commander.MoveGroupCommander('wajueji_controller')
        
        # 设置机械臂运动的允许误差值
        arm.set_goal_joint_tolerance(0.001)

        # 设置允许的最大速度和加速度
        arm.set_max_acceleration_scaling_factor(1.0)
        arm.set_max_velocity_scaling_factor(0.2)
        
        # 控制机械臂先回到初始化位置
        #arm.set_named_target('init_pose')
        #arm.go()
        #rospy.sleep(1)
        
        # 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        joint_positions = joint_positions = [9, -17, 0, -29]
        arm.set_joint_value_target(angle_to_rad(joint_positions))
                 
        # 控制机械臂完成运动
        arm.go()
        rospy.sleep(1)

        # 控制机械臂先回到初始化位置
        #arm.set_named_target('init_pose')
        #arm.go()
        #rospy.sleep(1)

        
        # 关闭并退出moveit
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

if __name__ == "__main__":
    try:
        MoveItFkDemo()
    except rospy.ROSInterruptException:
        pass
