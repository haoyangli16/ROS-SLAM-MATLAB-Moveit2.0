#!/usr/bin/env python

import roslib
import rospy
import cmd
import math
import sys

from control_msgs.msg import JointControllerState
from control_msgs.msg import JointTrajectoryControllerState
from std_msgs.msg import Float64

# Global constants
PI = 3.1415926535897931

####  Initial Parameters of peijian    ####
# cheshen -- 03 -- yg1220_1/2
DEFAULT_X1_RAD = 1.7139
DEFAULT_Y1_RAD = 1.13357
DEFAULT_Z1_MM = 2594.8156
# O3 -- 04 -- yg1480
DEFAULT_X2_RAD = 1.297
DEFAULT_Y2_RAD = 0.3227
DEFAULT_Z2_MM = 2641.1
# 04 -- chandou -- yg1050 -- 05_1/2 -- 06
DEFAULT_X3_RAD = 2.81754
DEFAULT_Y3_MM = 1036.53
DEFAULT_Z3_MM = 2520.09
DEFAULT_T1_RAD = 0.18537
DEFAULT_T2_RAD = 0.13868
DEFAULT_T3_RAD = 0.56912
DEFAULT_T4_RAD = 0.58811
DEFAULT_T5_RAD = 2.13712
DEFAULT_T6_RAD = 0.20571
DEFAULT_B1_RAD = 0.77348
DEFAULT_B2_RAD = 0.70781

####         List of topics            ####
# cheshen to 03 followings:
TOPIC_J1_CMD = '/wajueji/cheshen_to_1220_1_position_controller/command'
TOPIC_J2_CMD = '/wajueji/cheshen_to_1220_2_position_controller/command'
TOPIC_J3_CMD = '/wajueji/yg1220_1_position_controller/command'
TOPIC_J4_CMD = '/wajueji/yg1220_2_position_controller/command'
# 03 to 04 followings:
TOPIC_J5_CMD = '/wajueji/t03_to_1480_position_controller/command'
TOPIC_J6_CMD = '/wajueji/t1480_1_to_2_position_controller/command'
# 05 to chandou followings:
TOPIC_J7_CMD = '/wajueji/t04_to_1050_position_controller/command'
TOPIC_J8_CMD = '/wajueji/t1050_1_to_2_position_controller/command'
TOPIC_J9_CMD = '/wajueji/t04_to_05_1_position_controller/command'
TOPIC_J10_CMD = '/wajueji/t04_to_05_2_position_controller/command'
TOPIC_J11_CMD = '/wajueji/chandou_to_06_position_controller/command'


class PeijianMove:

    def __init__(self):
        rospy.init_node('peijian_move_commander', anonymous=True)
        nodename = rospy.get_name()
        rospy.loginfo("%s started" % nodename)

        self.pub_j1_cmd = rospy.Publisher(TOPIC_J1_CMD, Float64, queue_size=10)
        self.pub_j2_cmd = rospy.Publisher(TOPIC_J2_CMD, Float64, queue_size=10)
        self.pub_j3_cmd = rospy.Publisher(TOPIC_J3_CMD, Float64, queue_size=10)
        self.pub_j4_cmd = rospy.Publisher(TOPIC_J4_CMD, Float64, queue_size=10)
        self.pub_j5_cmd = rospy.Publisher(TOPIC_J5_CMD, Float64, queue_size=10)
        self.pub_j6_cmd = rospy.Publisher(TOPIC_J6_CMD, Float64, queue_size=10)
        self.pub_j7_cmd = rospy.Publisher(TOPIC_J7_CMD, Float64, queue_size=10)
        self.pub_j8_cmd = rospy.Publisher(TOPIC_J8_CMD, Float64, queue_size=10)
        self.pub_j9_cmd = rospy.Publisher(TOPIC_J9_CMD, Float64, queue_size=10)
        self.pub_j10_cmd = rospy.Publisher(TOPIC_J10_CMD, Float64, queue_size=10)
        self.pub_j11_cmd = rospy.Publisher(TOPIC_J11_CMD, Float64, queue_size=10)

        # absolute Value for now
        self.X1_RAD = DEFAULT_X1_RAD
        self.Y1_RAD = DEFAULT_Y1_RAD
        self.Z1_MM = DEFAULT_Z1_MM
        self.X2_RAD = DEFAULT_X2_RAD
        self.Y2_RAD = DEFAULT_Y2_RAD
        self.Z2_MM = DEFAULT_Z2_MM
        self.X3_RAD = DEFAULT_X3_RAD
        self.Y3_MM = DEFAULT_Y3_MM
        self.Z3_MM = DEFAULT_Z3_MM
        self.T1_RAD = DEFAULT_T1_RAD
        self.T2_RAD = DEFAULT_T2_RAD
        self.T3_RAD = DEFAULT_T3_RAD
        self.T4_RAD = DEFAULT_T4_RAD
        self.T5_RAD = DEFAULT_T5_RAD
        self.T6_RAD = DEFAULT_T6_RAD
        self.B1_RAD = DEFAULT_B1_RAD
        self.B2_RAD = DEFAULT_B2_RAD

        # joint_names: [base_to_cheshen, cheshen_to_03, t03_to_04, t04_to_chandou]
        self.nowpositions = [0.0, 0.0, 0.0, 0.0]

        rospy.Subscriber('/wajueji/wajueji_controller/state', JointTrajectoryControllerState, self.twistCallback)

        self.rate = rospy.get_param("~rate", 40)
        self.timeout_ticks = rospy.get_param("~timeout_ticks", 2)

    def spin(self):
        r = rospy.Rate(self.rate)
        idle = rospy.Rate(10)
        then = rospy.Time.now()
        self.ticks_since_target = self.timeout_ticks
        ###### main loop  ######
        while not rospy.is_shutdown():
            while not rospy.is_shutdown() and self.ticks_since_target < self.timeout_ticks:
                self.spinOnce()
                r.sleep()
            idle.sleep()

    def spinOnce(self):
        for i in range(0, 4):
            self.pjmove(i)

        self.ticks_since_target += 1

    def pjmove(self, joint):
        # cheshen -- 03 -- yg1220_1/2
        if joint == 1:
            self.X1_RAD = DEFAULT_X1_RAD - self.nowpositions[joint]
            self.Z1_MM = math.sqrt(760 ** 2 + 2375 ** 2 - 2 * 760 * 2375 * math.cos(self.X1_RAD))
            self.Y1_RAD = math.asin(2375 * math.sin(self.X1_RAD) / self.Z1_MM)

            self.pub_j1_cmd.publish(self.Y1_RAD - DEFAULT_Y1_RAD)
            self.pub_j2_cmd.publish(self.Y1_RAD - DEFAULT_Y1_RAD)
            self.pub_j3_cmd.publish((DEFAULT_Z1_MM - self.Z1_MM) / 1000)
            self.pub_j4_cmd.publish((DEFAULT_Z1_MM - self.Z1_MM) / 1000)

        # O3 -- 04 -- yg1480
        elif joint == 2:
            self.X2_RAD = DEFAULT_X2_RAD + self.nowpositions[joint]
            self.Z2_MM = math.sqrt(870 ** 2 + 2740 ** 2 - 2 * 870 * 2740 * math.cos(self.X2_RAD))
            self.Y2_RAD = math.asin(870 * math.sin(self.X2_RAD) / self.Z2_MM)

            self.pub_j5_cmd.publish(self.Y2_RAD - DEFAULT_Y2_RAD)
            self.pub_j6_cmd.publish((DEFAULT_Z2_MM - self.Z2_MM) / 1000)
        # 04 -- chandou -- yg1050 -- 05_1/2 -- 06
        elif joint == 3:
            self.X3_RAD = DEFAULT_X3_RAD + self.nowpositions[joint]
            self.Y3_MM = math.sqrt(450 ** 2 + 600 ** 2 - 2 * 450 * 600 * math.cos(self.X3_RAD))
            self.T1_RAD = math.asin(600 * math.sin(self.X3_RAD) / self.Y3_MM)
            self.T2_RAD = math.asin(450 * math.sin(self.X3_RAD) / self.Y3_MM)
            self.T4_RAD = math.acos((610 ** 2 + self.Y3_MM ** 2 - 628 ** 2) / (2 * self.Y3_MM * 610))
            self.T3_RAD = math.asin(610 * math.sin(self.T4_RAD) / 628)
            self.B1_RAD = self.T1_RAD + self.T4_RAD
            self.B2_RAD = self.T2_RAD + self.T3_RAD
            self.T5_RAD = PI - 0.23097 - self.B1_RAD
            self.Z3_MM = math.sqrt(2139.67 ** 2 + 610 ** 2 - 2 * 610 * 2139.67 * math.cos(self.T5_RAD))
            self.T6_RAD = math.asin(610 * math.sin(self.T5_RAD) / self.Z3_MM)

            self.pub_j7_cmd.publish(self.T6_RAD - DEFAULT_T6_RAD)
            self.pub_j8_cmd.publish((DEFAULT_Z3_MM - self.Z3_MM) / 1000)
            self.pub_j9_cmd.publish(self.T5_RAD - DEFAULT_T5_RAD)
            self.pub_j10_cmd.publish(self.T5_RAD - DEFAULT_T5_RAD)
            self.pub_j11_cmd.publish(DEFAULT_B2_RAD - self.B2_RAD)

    def twistCallback(self, msg):
        self.ticks_since_target = 0
        ###  Get the value of zhuti states ###
        self.nowpositions = msg.desired.positions


if __name__ == '__main__':
    peijianmove = PeijianMove()
    peijianmove.spin()
