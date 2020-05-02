#! /usr/bin/env python
import rospy
from std_msgs.msg import String



class Topic_Sub(object):

    def __init__(self):
        self._sub=rospy.Subscriber("/reto",String,self.callback)
        self._data=String()

    def callback(self,msg):
        self._data=msg

    def get_data(self):
        return self._data

if __name__=="__main__":
    rospy.init_node("topic_sub")
    data=Topic_Sub()
    rate=rospy.Rate(10)
    ctrl_c=False

    def shutdownhook():
        global ctrl_c
        ctrl_c=True
        rospy.loginfo("Node cancelled")

    rospy.on_shutdown(shutdownhook)

    while not ctrl_c:
        rospy.loginfo(data.get_data())
        rate.sleep()


