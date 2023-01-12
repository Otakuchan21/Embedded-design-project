#!/usr/bin/env python

import rospy
from auto_car.msg import ObstacleMessage
from std_msgs.msg import Int32

class Master:
    def __init__(self):
        rospy.Subscriber("object_detection", ObstacleMessage, self.object_detection_callback)
        rospy.Publisher("navigation", Int32, queue_size=1)
        

    def start(self):
        pass

    def object_detection_callback(self):
        pass
    
    def logger(self):
        pass

    def clock_callback(self):
        pass
        
    
        


if __name__ == "__main__":
    rospy.init_node("master_node")
    master = Master()
    rospy.sleep(5)
    master.start()
    rospy.spin()