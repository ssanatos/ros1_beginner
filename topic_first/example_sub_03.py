#! /usr/bin/env python3

import rospy
from std_msgs.msg import String

def fun_callback(msg):
    rospy.loginfo('sub03%s',msg.data)
    pub = rospy.Publisher('exception', String, queue_size = 10)
    str = "sub03 : %s" % rospy.get_time()
    pub.publish(str)
    return

if __name__ == "__main__":
    rospy.init_node('sample_sub_03') # 이 파일의 이름

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        # 메시지 키
        rospy.Subscriber('hello_03', String, callback=fun_callback)
        rospy.Subscriber('hello_04', String, callback=fun_callback)
        rospy.spin()
     
    pass

