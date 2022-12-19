#!/usr/bin/env python

import rospy
import actionlib 
from auto_car.msg import ObstacleDetectionFeedback, ObstacleDetectionResult, ObstacleDetectionAction
class ObstacleDetect(object):
    _feedback = ObstacleDetectionFeedback()
    _result = ObstacleDetectionResult()

    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name,
                                                ObstacleDetectionAction,
                                                execute_cb = self.execute_cb,
                                                auto_start = False)
        self._as.start()

    def execute_cb(self, goal):
        r = rospy.Rate(1)
        success = True
        
        # block for obstacle detection
        #########
        # all code here
        #########

        if success:
            self._result.message = "Obstacle detected initiate Avoidance sequence"
            rospy.loginfo('%s: Succedded', self._action_name)
            self._as.set_succeeded(self._result)

if __name__ == "__main__":
    rospy.init_node("Detection")
    server = ObstacleDetect(rospy.get_name())
    rospy.spin()