#!/usr/bin/env python

from __future__ import print_function
import rospy
import actionlib
from auto_car.msg import ObstacleDetectionAction, ObstacleDetectionGoal

def ObstacleClient():
    client = actionlib.SimpleActionClient('Detection', ObstacleDetectionAction)
    client.wait_for_server()
    goal = ObstacleDetectionGoal(message = "initiate detection sequence")
    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()

if __name__=='__main__':
    try:
        rospy.init_node('ObstacleClient')
        result = ObstacleClient()
        print(result)
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
