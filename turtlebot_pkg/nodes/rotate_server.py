#! /usr/bin/env python
import rospy
# custom service messsage
from turtlebot_pkg.srv import rotateResult, rotateResultResponse

def fun_callback(req):
    rospy.loginfo('%s' % (req.scan_sequence))
    # req.scan_sequence  # srv에 만들어놓은 변수 그대로.
    success = True
    message = 'This is success'
    return rotateResultResponse(success, message)

if __name__ == '__main__':
    # server 선언
    rospy.init_node('rotate_server')
    # server 기다리기
    rospy.Service('rotate_result',rotateResult,fun_callback)

    rospy.spin()
    pass