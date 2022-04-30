#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
该程序只用来设定挖掘机机械臂的初始位置。
'''
import rospy, sys
import moveit_commander

class MoveItFkDemo:
    def __init__(self):
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('moveit_fk_demo', anonymous=True)
        arm = moveit_commander.MoveGroupCommander('wajueji')
        arm.set_goal_joint_tolerance(0.001)
        arm.set_max_acceleration_scaling_factor(1.0)
        arm.set_max_velocity_scaling_factor(1.0)

        # 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        joint_positions = [0.0, -0.593412, 0.872665, 0.209436]
        arm.set_joint_value_target(joint_positions)
        arm.go()
        rospy.sleep(1)

        # 关闭并退出moveit
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

if __name__ == "__main__":
    try:
        MoveItFkDemo()
    except rospy.ROSInterruptException:
        pass
