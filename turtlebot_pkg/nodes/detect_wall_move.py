#! /usr/bin/env python

"""
Parking Assignment Answer
Try it out!!
"""

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


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

  
    pub.publish(cmd_vel)


rospy.init_node("detect_wall_move", disable_signals=True)
rospy.loginfo("==== parking node Started ====\n")

pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
sub = rospy.Subscriber("/scan", LaserScan, callback)

rospy.spin()