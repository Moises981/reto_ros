#! /usr/bin/env python

import rospy
from std_msgs.msg import String

class Publisher_DATA(object):

    def __init__(self):
        self._pub=rospy.Publisher("reto",String,queue_size=1)
        self.text=String()

       
    def launch(self):
        self.text.data="reto playtec"
        self._pub.publish(self.text)

if __name__=="__main__":
    rospy.init_node("topic_pub")
    topic_pub=Publisher_DATA()
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

