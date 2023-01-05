#!/usr/bin/env python

import rospy
import RPi.GPIO as GPIO
from geometry_msgs.msg import Twist

# Set up the GPIO pins for the H-bridge
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

# Initialize the ROS node
rospy.init_node('motor_control')

# Set up the subscriber to the Twist message
def twist_callback(data):
    # Extract the linear and angular velocities
    linear_velocity = data.linear.x
    angular_velocity = data.angular.z

    # Calculate the desired speed of each motor
    motor1_speed = linear_velocity + angular_velocity
    motor2_speed = linear_velocity - angular_velocity
    motor3_speed = linear_velocity + angular_velocity
    motor4_speed = linear_velocity - angular_velocity

    # Set the direction of each motor based on the sign of the speed
    if motor1_speed > 0:
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(22, GPIO.LOW)
    else:
        GPIO.output(17, GPIO.LOW)
        GPIO.output(22, GPIO.HIGH)
    if motor2_speed > 0:
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.LOW)
    else:
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)
    if motor3_speed > 0:
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(22, GPIO.LOW)
    else:
        GPIO.output(17, GPIO.LOW)
        GPIO.output(22, GPIO.HIGH)
    if motor4_speed > 0:
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.LOW)
    else:
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)

# Set up the subscriber
sub = rospy.Subscriber('/cmd_vel', Twist, twist_callback)

# Run the ROS node
rospy.spin()
