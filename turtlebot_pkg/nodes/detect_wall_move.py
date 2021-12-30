#! /usr/bin/env python

"""
Parking Assignment Answer
Try it out!!
"""

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from turtlebot_pkg.srv import rotateResult

def call_rotate_client(laser_range):
    rospy.wait_for_service('rotate_result')
    send_to_server = rospy.ServiceProxy('rotate_result',rotateResult)   #서버노드의 서비스열을 인스턴스화
    result = send_to_server(laser_range)  #2개이상이면 ,찍고 적으면 됨.
    print(result.success,',',result.message)
    rospy.sleep(3)
    return result

import numpy as np
def callback(data):
    laser_range = data.ranges[0:5]
    laser_arr = np.array(laser_range)
    # result = np.mean(laser_arr)
    result = np.count_nonzero((laser_arr >= 0.3))
    cmd_vel = Twist()
    
    if result > 0:
    # if result <= 0.3:
        cmd_vel.linear.x = 0.2
    else:
        cmd_vel.linear.x = 0.0
        pub.publish(cmd_vel)
        # client 벽을 만나서 멈췄을 때 도는 함수 호출
        result = call_rotate_client(laser_arr)


  
    pub.publish(cmd_vel)


rospy.init_node("detect_wall_move", disable_signals=True)
rospy.loginfo("==== parking node Started ====\n")

pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
sub = rospy.Subscriber("/scan", LaserScan, callback)

rospy.spin()