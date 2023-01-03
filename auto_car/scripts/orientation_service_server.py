#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from auto_car.srv import orientationMessage, orientationMessageResponse
from nav_msgs.msg import Odometry as odom
from tf.transformations import euler_from_quaternion
import math

class orientationFixer():
    def __init__(self):
        self.pub = rospy.Publisher('cmd_vel', Twist, queue_size= 10)
        self.sub = rospy.Subscriber('odom', odom, self.subCallback)
        self.current_angular_z = 0
        self.target = 0
        self.velocity = Twist()
        self.velocityValue()

    def velocityValue(self):
        self.velocity.linear.x = 0
        self.velocity.linear.y = 0
        self.velocity.linear.z = 0
        self.velocity.angular.x = 0
        self.velocity.angular.y = 0
        self.velocity.angular.z = 0
    
    def subCallback(self, data):
        q_base = data.pose.pose.orientation
        q_list = [q_base.x, q_base.y, q_base.z, q_base.w]
        euler_x, euler_y, euler_z = euler_from_quaternion(q_list)
        self.current_angular_z = math.degrees(euler_z)

    def service_callback(self, request):
        self.target = request.target_z
        ul = self.target + 10.0
        ll = self.target - 10.0
        r = rospy.Rate(1)
        while not (self.current_angular_z < ul and self.current_angular_z> ll):
            if self.current_angular_z >ul:
                self.velocity.angular.z = -0.5
            else:
                self.velocity.angular.z = 0.5
            
        
            self.pub.publish(self.velocity)
            r.sleep()
        
        self.velocityValue()
        self.pub.publish(self.velocity)
        r.sleep()
        #print(self.current_angular_z)

        return orientationMessageResponse("orientation complete")

if __name__ == "__main__":
    rospy.init_node("orientation_server")
    o = orientationFixer()
    service = rospy.Service('orientation_fix', orientationMessage, o.service_callback)
    rospy.spin()

    





