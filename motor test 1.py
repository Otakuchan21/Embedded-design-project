

import RPi.GPIO as GPIO          
import time

def init():
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(11, GPIO.OUT)
   GPIO.setup(15, GPIO.OUT)
   GPIO.setup(16, GPIO.OUT)
   GPIO.setup(18, GPIO.OUT)

def forward(tf):
    init()
    GPIO.output(11, True)
    GPIO.output(15, False)
    GPIO.output(16, True)
    GPIO.output(18, False)
    GPIO.sleep(tf)
    GPIO.cleanup()

def reverse(tf):
    init()
    GPIO.output(11, False)
    GPIO.output(15, True)
    GPIO.output(16, False)
    GPIO.output(18, True)
    time.sleep(tf)
    GPIO.cleanup()

print ("forward")
forward(4)

print ("backward")
reverse(2)


