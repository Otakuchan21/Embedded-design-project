#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry as odom
from geometry_msgs.msg import Twist
from tf.transformations import euler_from_quaternion
from auto_car.srv import orientationMessage
import math

class pathPlanning():
    def __init__(self):
        self.sub = rospy.Subscriber('/odom', odom, self.subCallback)
        self.pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
        self.request = rospy.ServiceProxy('orientation_fix', orientationMessage)
        self.current_x = 0.0
        self.current_y = 0.0
        self.current_angular_z = 0.0
        self.initial_x = 0.0
        self.initial_y = 0.0
        self.initial_angular_z = 0.0
        self.flag = True
        self.pub_msg = Twist()
        self.velocityValue()
        self.path = 2
        self.flag2 = True
        self.distance = 0.0
        self.rate = rospy.Rate(1)
        self.line = 'straight'
        self.flag3 = True
        self.flag4 = True
        self.flag5 = True

    def subCallback(self, data):
        # stores all position values in the relevant variables
        objLinear = data.pose.pose.position
        objOrient = data.pose.pose.orientation
        quaternion = [objOrient.x, objOrient.y, objOrient.z, objOrient.w]
        deg_x, deg_y, deg_z = euler_from_quaternion(quaternion)
        # flag is used to store the initial values.
        if self.flag == True:
            self.initial_x = objLinear.x 
            self.initial_y = objLinear.y
            self.flag = False
        else:
            self.current_x = objLinear.x 
            self.current_y = objLinear.y 
            self.current_angular_z = deg_z

    def pathDefinition(self):
        # this routine makes the car travel the shortest path
        if abs(self.distance)<0.2:
            self.carControl()
            self.distance = self.distanceCalculation(self.line)
            #print("distance during straight line traversal: ", self.distance)
            #print(self.line)
        elif abs(self.distance)>=0.2 and abs(self.distance)<0.4:
            if self.path == 1 and self.flag4 == True:
                self.service_call(self.current_angular_z+30)
                self.flag4 = False
            elif self.path == 2 and self.flag4 == True:
                self.service_call(self.current_angular_z-30)
                self.flag4 = False
            if self.flag3 == True:
                self.initial_x = self.current_x
                self.initial_y = self.current_y
                self.flag3 = False
            self.line = 'slant'
            self.distance = self.distanceCalculation(self.line)
            #print('linear distance of car on slant line: ', self.distance)
            self.carControl()
            #print('linear velocity: ', self.pub_msg.linear.x)
        elif self.path == 2 and abs(self.distance)>=0.4 and abs(self.distance)<0.6:
            if self.flag5 == True:
                self.service_call(90)
                self.initial_x = self.current_x
                self.initial_y = self.current_y
                self.flag5 = False
            self.carControl()
            self.distance = self.distance = self.distanceCalculation(self.line) + 0.2
            
        else:
            self.velocityValue()
            self.pub.publish(self.pub_msg)


    def carControl(self):
        # this function checks for deviation from line and send cmd velocity accordingly
        if self.flag2 == True:
            # this service call is for fixing the orientation of the car
            self.service_call(0.0)
            self.flag2 = False
            self.initial_angular_z = self.current_angular_z
        # this if block ensures that the right deviation is used for the line being traversed.
        if self.line == 'straight':
            travel_range_ul = self.initial_y+0.1
            travel_range_ll = self.initial_y-0.1
            distance = self.current_y
        elif self.line == 'slant' and self.path == 1:
            distance = self.distanceCalculation('deviation')
            #print("distance calculated from deviation" , distance)
            travel_range_ul = 0.10
            travel_range_ll = -0.10
        elif self.line == 'slant' and self.path == 2:
            distance = self.distanceCalculation('deviation2')
            travel_range_ul = 0.10
            travel_range_ll = -0.10
        # this if block checks if the car is moving in the correct direction.
        if distance < travel_range_ul and distance > travel_range_ll:
            self.pub_msg.linear.x = 0.1
            self.pub_msg.angular.z = 0.0
        elif distance>travel_range_ul:
            self.pub_msg.linear.x = 0.1
            self.pub_msg.angular.z = -0.2
        elif distance<travel_range_ll:
            self.pub_msg.linear.x = 0.1
            self.pub_msg.angular.z = 0.2
        print(self.pub_msg.angular.z)
        self.pub.publish(self.pub_msg)
        self.rate.sleep()

    def distanceCalculation(self, line):
        if self.path == 1:
            if line == 'deviation':
                c = self.equationOfLine()
                num = (self.current_x*math.sqrt(3)/3) + c -self.current_y
                print("numerator for diatance calculation: ", num)
                den = math.sqrt(4/3)
                print("denominator for diatance calculation: ", den)
                distance = num/den
        elif self.path == 2:
            # will define the second path later first need to fix the deviation calcultion of the lines.
            if line == 'deviation':
                c = self.equationOfLine()
                num = (self.current_x*math.sqrt(3)/3) - c +self.current_y
                print("numerator for diatance calculation: ", num)
                den = math.sqrt(4/3)
                print("denominator for diatance calculation: ", den)
                distance = num/den
            if line == 'deviation2':
                distance = abs(self.current_x) - abs(self.initial_x)
        if line == 'straight':
            distance = abs(self.current_x) - abs(self.initial_x)
        #y-roo3/3x+20root3/3
        elif line == 'slant':
            sq = (self.current_x - self.initial_x)*(self.current_x - self.initial_x)
            sq2 = (self.current_y - self.initial_y)*(self.current_y - self.initial_y)
            distance = math.sqrt(sq + sq2) + 0.2

            
        return distance 

    def equationOfLine(self):
        if self.path == 1:
            intercept  = self.current_y - math.sqrt(3)*self.current_x/3
        else:
            intercept = self.current_y + math.sqrt(3)*self.current_x/3
        print("intercept: ", intercept)
        return intercept

    def service_call(self, target):
        rospy.wait_for_service('orientation_fix')
        response = self.request(target)
        
    def velocityValue(self):
        self.pub_msg.linear.y = 0
        self.pub_msg.linear.x = 0
        self.pub_msg.linear.z = 0
        self.pub_msg.angular.x = 0
        self.pub_msg.angular.y = 0
        self.pub_msg.angular.z = 0

    
def main():
    rospy.init_node("path_planning")
    p = pathPlanning()
    while not rospy.is_shutdown():
        p.pathDefinition()

if __name__=="__main__":
    main()



