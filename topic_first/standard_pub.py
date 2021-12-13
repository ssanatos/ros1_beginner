#! /usr/bin/env python3

import rospy
from std_msgs.msg import String

def fun():
    return

def fun_callback(msg):
    return

if __name__ == "__main__":
    rospy.init_node('sample_pub') # 이 파일의 이름
    pub = rospy.Publisher('hello', String, queue_size = 10)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        str = "hell_publisher : %s" % rospy.get_time()
        pub.publish(str)
        rate.sleep()
    pass

