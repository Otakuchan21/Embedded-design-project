#!/usr/bin/env python

import RPi.GPIO as GPIO          
import time

def init():
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(17, GPIO.OUT)
   GPIO.setup(22, GPIO.OUT)
   GPIO.setup(23, GPIO.OUT)
   GPIO.setup(24, GPIO.OUT)

def forward(tf):
    init()
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, True)
    gpio.output(24, False)
    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):
    init()
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, False)
    gpio.output(24, True)
    time.sleep(tf)
    gpio.cleanup()

print ("forward")
forward(4)

print ("backward")
reverse(2)


