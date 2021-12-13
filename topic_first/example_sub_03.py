#! /usr/bin/env python3

import rospy
from std_msgs.msg import String

def fun_callback(msg):
    rospy.loginfo('sub03%s',msg.data)
    return

def fun():
    return

if __name__ == "__main__":
    rospy.init_node('sample_sub_03') # 이 파일의 이름
    # 메시지 키
    rospy.Subscriber('hello_03', String, callback=fun_callback)
    rospy.Subscriber('hello_04', String, callback=fun_callback)
    rospy.spin()

    # 메시지 키
    pub = rospy.Publisher('exception', String, queue_size = 10)
     
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        # 메시지 내용
        str = "Lefa I love you : %s" % rospy.get_time()
        pub.publish(str)
        rate.sleep()
    pass
