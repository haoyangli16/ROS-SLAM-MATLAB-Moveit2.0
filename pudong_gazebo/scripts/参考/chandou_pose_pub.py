#!/usr/bin/env python

import roslib
import rospy
import json
import xlwt

from gazebo_msgs.msg import LinkStates
from std_msgs.msg import Float64


# PUB_TOPIC = 'chandou_mass_point_position'


def data_write():
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet('Worksheet1')
    style = xlwt.XFStyle()  
    font = xlwt.Font()  
    font.name = 'Times New Roman'
    font.bold = True  
    font.underline = True  
    font.italic = True  
    style.font = font  

    name_array = ['x', 'y', 'z']
    row = 1

    for name in name_array:
	filename = 'catkin_ws/src/pudong_gazebo/scripts/data/chandou_' + name + '.json'
        with open(filename) as file:
            pose = json.load(file)
            length = len(pose)
            for x in range(0, length):
                worksheet.write(x, row, pose[x])
        row += 1

    workbook.save('catkin_ws/src/pudong_gazebo/scripts/data/chandou_xyz.xls')


class ChandouPosePub():
    def __init__(self):
    	rospy.init_node('chandou_mass_pose_publisher')
        nodename = rospy.get_name()
        rospy.loginfo("%s started" % nodename)

	# self.pub = rospy.Publisher(PUB_TOPIC, Float64, queue_size=10)

        rospy.Subscriber('gazebo/link_states', LinkStates, self.twistCallback)

        self.rate = rospy.get_param("~rate", 10)
        self.timeout_ticks = rospy.get_param("~timeout_ticks", 2)

	self.chandou_pose_x = 0.0
	self.chandou_pose_y = 0.0
	self.chandou_pose_z = 0.0
	
	self.x = []
	self.y = []
	self.z = []


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
	# self.pub.publish(self.chandou_pose_x)

	self.x.append(self.chandou_pose_x)
	self.y.append(self.chandou_pose_y)
	self.z.append(self.chandou_pose_z)

	with open('catkin_ws/src/pudong_gazebo/scripts/data/chandou_x.json', 'w') as filex:
	    json.dump(self.x, filex)
	with open('catkin_ws/src/pudong_gazebo/scripts/data/chandou_y.json', 'w') as filey:
	    json.dump(self.y, filey)
	with open('catkin_ws/src/pudong_gazebo/scripts/data/chandou_z.json', 'w') as filez:
	    json.dump(self.z, filez)

	data_write()
	self.ticks_since_target += 1

    def twistCallback(self, msg):
        self.ticks_since_target = 0
	self.chandou_pose_x = msg.pose[44].position.x
	self.chandou_pose_y = msg.pose[44].position.y
	self.chandou_pose_z = msg.pose[44].position.z

if __name__ == '__main__':
    cpp2 = ChandouPosePub()
    cpp2.spin()

