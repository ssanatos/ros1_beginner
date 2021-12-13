#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def fun():
    return

def fun_callback(msg):
    return

if __name__ == "__main__":
    rospy.init_node('simturtle_pub_rotate') # 이 파일의 이름
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)

    twist = Twist()

    speed = 40
    angle = 180

    angluar_speed = speed*2*3.14/180
    relative_angle = angle*2*3.14/180 

    time0 = rospy.Time.now().to_sec()
    current = 0
    twist.angular.z = angluar_speed
    while current < relative_angle:
        pub.publish(twist)
        time1 = rospy.Time.now().to_sec()
        current = current*(time1-time0)

    twist.angular.z = 0.0
    pub.publish(twist)
    pass
