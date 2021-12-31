#! /usr/bin/env python
import rospy
# custom service messsage
from turtlebot_pkg.srv import rotateResult, rotateResultResponse
from geometry_msgs.msg import Twist
#PI = 3.1415926535897
toRAD = 0.0174533

def rotate():
    # Starts a new node
    rospy.init_node('tb3_cleaner', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    msg = Twist()

    # Receiveing the user's input
    print("input speed within 0.0 ~ 160")
    speed     = input("Input your speed (degrees/sec):")
    print("input speed within 0 ~ 360")
    angle     = input("Type your distance (degrees):")
    print("direction cw:1, ccw:0")
    clockwise = input("Clockwise?: ")
    
    angular_speed  = speed * toRAD
    relative_angle = angle * toRAD

    msg.linear.x  = msg.linear.y  = msg.linear.z  = 0
    msg.angular.x = msg.angular.y = 0
    
    if clockwise:
        msg.angular.z = -abs(angular_speed)
    else:
        msg.angular.z =  abs(angular_speed)
        
    duration = relative_angle / angular_speed
    time2end = rospy.Time.now() + rospy.Duration(duration)
    
    pub.publish(msg)
    rospy.sleep(0.001)
        
    while rospy.Time.now() < time2end :
        pass    
        
    msg.angular.z = 0
    pub.publish(msg)


def fun_callback(req):
    # rospy.loginfo('%s' % (req.scan_sequence))
    # req.scan_sequence srv에 만들어놓은 변수 그대로.
    print('scan : ', req.scan_sequence)
    success = True
    message = 'This is success'
    rotate()
    return rotateResultResponse(success, message)

if __name__ == '__main__':
    # server 선언
    rospy.init_node('rotate_server')
    # server 기다리기
    rospy.Service('rotate_result',rotateResult,fun_callback)

    rospy.spin()
    pass