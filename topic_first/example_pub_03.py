#! /usr/bin/env python3

import rospy
from std_msgs.msg import String
# 로스에 있는 메시지 패키지에서 스트링 방식 가져옴

def fun():
    return

if __name__ == "__main__":
    rospy.init_node('sample_pub_03')
    # 메시지 키
    pub = rospy.Publisher('hello_04', String, queue_size = 10)
     
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        # 메시지 내용
        str = "Go Go Samsung : %s" % rospy.get_time()
        pub.publish(str)
        rate.sleep()
    pass

