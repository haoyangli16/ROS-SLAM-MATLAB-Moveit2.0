#!/usr/bin/env python
#-*- coding:utf-8   -*-


import roslib
import rospy
import json
import xlwt


from gazebo_msgs.msg import ModelStates
from gazebo_msgs.msg import LinkStates
from std_msgs.msg import Float64


def data_write():
    """该函数可以从json文件中读取数据，并按顺序分别写入csv的每一列"""
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet('Worksheet1')
    style = xlwt.XFStyle()  
    font = xlwt.Font()  
    font.name = 'Times New Roman'
    font.bold = True  
    font.underline = True  
    font.italic = True  
    style.font = font  

    name_array = ['cheshen_x', 'cheshen_y', 'cheshen_z', 'chandou_x', 'chandou_y', 'chandou_z']
    # 从第二列开始写入，空出第一列来写入时间
    row = 1

    for name in name_array:
        filename = 'catkin_ws/src/pudong_gazebo/scripts/data/' + name + '.json'
        with open(filename) as file:
            pose = json.load(file)
            length = len(pose)
            for i in range(0, length):
                worksheet.write(i, row, pose[i])
        row += 1

    workbook.save('catkin_ws/src/pudong_gazebo/scripts/data/dates_xyz4.xls')


class PosesRecorder():
    """该类可以从Gazebo中记录所需要的数据，并分别写入json文件。包含：铲斗质心坐标，挖掘机底盘中心坐标。"""

    def __init__(self):
        rospy.init_node('poses_recorder')
        nodename = rospy.get_name()
        rospy.loginfo("%s started" % nodename)

        rospy.Subscriber('gazebo/model_states', ModelStates, self.twistCallback1)
	rospy.Subscriber('gazebo/link_states', LinkStates, self.twistCallback2)

        self.rate = rospy.get_param("~rate", 10)
        self.timeout_ticks = rospy.get_param("~timeout_ticks", 2)

	self.cheshen_pose_x = 0.0
	self.cheshen_pose_y = 0.0
	self.cheshen_pose_z = 0.0
	self.chandou_pose_x = 0.0
	self.chandou_pose_y = 0.0
	self.chandou_pose_z = 0.0
	
	self.cs_x = []
	self.cs_y = []
	self.cs_z = []
	self.cd_x = []
	self.cd_y = []
	self.cd_z = []

    def spin(self):
	"""该函数可以在ROS中无限循环，并通过spinOnce()函数实时接收数据"""
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
	self.cs_x.append(self.cheshen_pose_x)
	self.cs_y.append(self.cheshen_pose_y)
	self.cs_z.append(self.cheshen_pose_z)
	self.cd_x.append(self.chandou_pose_x)
	self.cd_y.append(self.chandou_pose_y)
	self.cd_z.append(self.chandou_pose_z)

	with open('catkin_ws/src/pudong_gazebo/scripts/data/cheshen_x.json', 'w') as filex1:
	    json.dump(self.cs_x, filex1)
	with open('catkin_ws/src/pudong_gazebo/scripts/data/cheshen_y.json', 'w') as filey1:
	    json.dump(self.cs_y, filey1)
	with open('catkin_ws/src/pudong_gazebo/scripts/data/cheshen_z.json', 'w') as filez1:
	    json.dump(self.cs_z, filez1)
	with open('catkin_ws/src/pudong_gazebo/scripts/data/chandou_x.json', 'w') as filex2:
	    json.dump(self.cd_x, filex2)
	with open('catkin_ws/src/pudong_gazebo/scripts/data/chandou_y.json', 'w') as filey2:
	    json.dump(self.cd_y, filey2)
	with open('catkin_ws/src/pudong_gazebo/scripts/data/chandou_z.json', 'w') as filez2:
	    json.dump(self.cd_z, filez2)

	data_write()
	self.ticks_since_target += 1

    def twistCallback1(self, msg):
        self.ticks_since_target = 0

	self.cheshen_pose_x = msg.pose[-1].position.x
	self.cheshen_pose_y = msg.pose[-1].position.y
	self.cheshen_pose_z = msg.pose[-1].position.z

    def twistCallback2(self, msg):
        self.ticks_since_target = 0

	self.chandou_pose_x = msg.pose[-8].position.x
	self.chandou_pose_y = msg.pose[-8].position.y
	self.chandou_pose_z = msg.pose[-8].position.z


if __name__ == '__main__':
    pp = PosesRecorder()
    pp.spin()

