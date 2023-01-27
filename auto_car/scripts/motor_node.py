#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class control():
    def __init__(self):
        self.sub = rospy.Subscriber("cmd_vel", Twist, self.callback)
        self.writer = serial.Serial("/dev/ttyACM0", 9600, timeout = 1)

    def callback(self, data):
        if data.linear.x> 0:
            if data.angular.z >0:
                #steer left
                self.writer.write(5)
            elif data.angular.z <0:
                #steer right
                self.writer.write(6)
            else:
                #forward
                self.writer.write(2)
        elif data.linear.x <0:
            #backward
            self.writer.write(1)
        elif data.linear.x == 0 and data.angular.z>0:
            #turn left
            self.writer.write(4)
        elif data.linear.x == 0 and data.angular.z<0:
            #turn right
            self.writer.write(3)
        elif data.linear.x == 0 and data.angular.z ==0:
            # stop
            self.writer.write(7)

if __name__ == "__main__":
    c = control()
    rospy.spin()
