
import RPi.GPIO as GPIO

# Define the GPIO pins for the OSOYOO Model-X Motor Driver Module
motor1_pinn1 = 17 # set 1
motor2_pinn2 = 22 # set 1
motor3_pinn3 = 5 # set 2
motor4_pinn4 = 19 # set 2

#enable pins are defined to control the amount of power supply to the motors 
motor1_enable = 23
motor2_enable = 24

# Set the GPIO pins as output
def setup():

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(motor1_pinn1, GPIO.OUT)
    GPIO.setup(motor2_pinn2, GPIO.OUT)
    GPIO.setup(motor3_pinn3, GPIO.OUT)
    GPIO.setup(motor4_pinn4, GPIO.OUT)

    GPIO.setup(motor1_enable, GPIO.OUT)
    GPIO.setup(motor2_enable, GPIO.OUT)

try:

    while True:

        # Function to set the motor's direction
        def set_motor_direction(direction):

            if direction == " forward":
                GPIO.output(motor1_enable, 100)
                GPIO.output(motor2_enable, 100) #pwm pins
                
                GPIO.output(motor1_pinn1, GPIO.HIGH) # these control left 2 motors
                GPIO.output(motor2_pinn2, GPIO.LOW)

                GPIO.output(motor3_pinn3, GPIO.HIGH) # these control right 2 motors
                GPIO.output(motor4_pinn4, GPIO.LOW)


            if direction == "backward":
                GPIO.output(motor1_enable, 100)
                GPIO.output(motor2_enable, 100) #pwm pins
                
                GPIO.output(motor1_pinn1, GPIO.LOW) #these control left 2 motors 
                GPIO.output(motor2_pinn2, GPIO.HIGH)

                GPIO.output(motor3_pinn3, GPIO.LOW) # these control right 2 motors
                GPIO.output(motor4_pinn4, GPIO.HIGH)


            if direction == "left":
                GPIO.output(motor1_enable, 100)
                GPIO.output(motor2_enable, 100) #pwm pins
                
                GPIO.output(motor1_pinn1, GPIO.LOW) # these control left 2 motors
                GPIO.output(motor2_pinn2, GPIO.HIGH)

                GPIO.output(motor3_pinn3, GPIO.HIGH) # these control right 2 motors
                GPIO.output(motor4_pinn4, GPIO.LOW)


            if direction == "right":
                GPIO.output(motor1_enable, 100)
                GPIO.output(motor2_enable, 100) #pwm pins
                
                GPIO.output(motor1_pinn1, GPIO.HIGH) # these control left 2 motors
                GPIO.output(motor2_pinn2, GPIO.LOW)

                GPIO.output(motor3_pinn3, GPIO.LOW) # these control right 2 motors
                GPIO.output(motor4_pinn4, GPIO.HIGH)

          
#disable power to all motors
except KeyboardInterrupt:
    GPIO.output(motor1_enable, GPIO.LOW)
    GPIO.output(motor2_enable, GPIO.LOW)

#clean up the GPIO pins 
    GPIO.cleanup()
