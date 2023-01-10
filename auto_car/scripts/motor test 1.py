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
    GPIO.output(17, True)
    GPIO.output(22, False)
    GPIO.output(23, True)
    GPIO.output(24, False)
    GPIO.sleep(tf)
    GPIO.cleanup()

def reverse(tf):
    init()
    GPIO.output(17, False)
    GPIO.output(22, True)
    GPIO.output(23, False)
    GPIO.output(24, True)
    time.sleep(tf)
    GPIO.cleanup()

print ("forward")
forward(4)

print ("backward")
reverse(2)


