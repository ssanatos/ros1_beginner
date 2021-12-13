#! /usr/bin/env python3

import rospy
from std_msgs.msg import String
# 로스에 있는 메시지 패키지에서 스트링 방식 가져옴

def fun():
    return

def fun_callback(msg):
    rospy.loginfo('pub01%s',msg.data)
    return

if __name__ == "__main__":
    rospy.init_node('sample_pub') # 이 파일의 이름
    # rospy.init_node('sample_pub_02')
    # 메시지 키
    pub = rospy.Publisher('hello', String, queue_size = 10)
    # pub02 = rospy.Publisher('hello_02', String, queue_size = 10)

    rospy.Subscriber('exception', String, callback=fun_callback)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        # 메시지 내용
        str = "hell_publisher : %s" % rospy.get_time()
        # str2 = "GO GO TESLA : %s" % rospy.get_time()
        pub.publish(str)
        # pub02.publish(str2)
        rate.sleep()
    pass

