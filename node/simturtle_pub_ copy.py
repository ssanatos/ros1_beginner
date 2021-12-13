#! usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
def fun_callback(msg):
    pass
if __name__=='__main__':
    rospy.init_node('simturtle_publisher',anonymous=False)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    msg = Twist()
    distance = 2.0
    current_distance = 0.0
    speed = 1
    rate = rospy.Rate(5)
    while current_distance < distance:
        msg.linear.x += 0.1
        pub.publish(msg)
        current_distance += 0.1
        print(current_distance)
        print(msg.linear.x)
        rate.sleep()
    pass