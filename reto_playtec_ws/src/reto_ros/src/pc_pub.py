#! /usr/bin/env python

import rospy
from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import PointField
import random

class Publisher_pointcloud(object):

    def __init__(self):
        self._pub=rospy.Publisher("PointCloud",PointCloud2,queue_size=1)
        self.data=PointCloud2()
        self.data.data=self.randomData()
        

    def randomData(self):
        data_list=[]
        for i in range(0,256):
            data_list.append(random.randint(0,100))

        return data_list

        

       
    def launch(self):
        self.data.header.frame_id="waist_link"
        self.data.height=4
        self.data.width=64
        self.data.is_bigendian=False
        self.data.fields=[PointField("x",1,7,1),PointField("y",1,7,1),PointField("z",1,7,1)]
    
        self.data.point_step=1
        self.data.row_step=1
        self.data.is_dense=True
        self._pub.publish(self.data)

    

if __name__=="__main__":
    rospy.init_node("PC")
    topic_pub=Publisher_pointcloud()
    rate=rospy.Rate(10)

    ctrl_c=False

    def shutdownhook():
        global ctrl_c
        ctrl_c=True
        rospy.loginfo("Node cancelled")

    rospy.on_shutdown(shutdownhook)

    while not ctrl_c:
        topic_pub.launch()
        rate.sleep()

