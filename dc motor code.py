#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

# Set up the GPIO pins for the H-bridge
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) # Left motor forward
GPIO.setup(22, GPIO.OUT) # Left motor backward
GPIO.setup(23, GPIO.OUT) # Right motor forward
GPIO.setup(24, GPIO.OUT) # Right motor backward

# Set up PWM for the left and right motors
left_motor_forward = GPIO.PWM(17, 100)
left_motor_backward = GPIO.PWM(22, 100)
right_motor_forward = GPIO.PWM(23, 100)
right_motor_backward = GPIO.PWM(24, 100)


# Start the PWM at 0% duty cycle
left_motor_forward.start(0)
left_motor_backward.start(0)
right_motor_forward.start(0)
right_motor_backward.start(0)

# Function to set the speed of the left and right motors
def set_motor_speeds(left_speed, right_speed):
    left_motor_forward.ChangeDutyCycle(left_speed)
    left_motor_backward.ChangeDutyCycle(0)
    right_motor_forward.ChangeDutyCycle(right_speed)
    right_motor_backward.ChangeDutyCycle(0)

# Function to set the direction of the left and right motors
def set_motor_direction(left_direction, right_direction):
    if left_direction == "forward":
        left_motor_forward.ChangeDutyCycle(left_speed)
        left_motor_backward.ChangeDutyCycle(0)
    elif left_direction == "backward":
        left_motor_forward.ChangeDutyCycle(0)
        left_motor_backward.ChangeDutyCycle(left_speed)
    if right_direction == "forward":
        right_motor_forward.ChangeDutyCycle(right_speed)
        right_motor_backward.ChangeDutyCycle(0)
    elif right_direction == "backward":
        right_motor_forward.ChangeDutyCycle(0)
        right_motor_backward.ChangeDutyCycle(right_speed)

# Example usage:
# Set the left motor to go forward at 50% speed and the right motor to go backward at 25% speed
set_motor_speeds(50, 25)
set_motor_direction("forward", "backward")

# Wait for 5 seconds
time.sleep(5)

# Stop the motors
left_motor_forward.ChangeDutyCycle(0)
left_motor_backward.ChangeDutyCycle(0)
right_motor_forward.ChangeDutyCycle(0)
