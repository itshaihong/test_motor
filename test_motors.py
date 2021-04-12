import time
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#set up pins for PIR sensors
PIR_right=13
PIR_left=19
PIR_back=26
GPIO.setup(DC_EN, GPIO.IN)
GPIO.setup(DC_EN, GPIO.IN)
GPIO.setup(DC_EN, GPIO.IN)

#set up pins for DC motor
DC_EN=23
GPIO.setup(DC_EN, GPIO.OUT)

#set up pins for stepper motor
DIR = 16
STEP = 12
EN=25
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
MODE = (14, 15, 18)   # Microstep Resolution GPIO Pins
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(EN, GPIO.OUT)
GPIO.output(EN, GPIO.HIGH)#disable first
GPIO.setup(DIR, GPIO.OUT)
GPIO.output(DIR, CW)#clockwise
GPIO.setup(MODE, GPIO.OUT)
RESOLUTION = {'Full': (0, 0, 0),#7.5
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}
GPIO.output(MODE, RESOLUTION['1/4'])#smaller steps

#for testing
for i in range(48*4):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(0.208/4)
    GPIO.output(STEP, GPIO)
    sleep(0.208/4)

for i in range(5):
    GPIO.output(DC_EN, GPIO.HIGH)
    sleep(1)

if GPIO.input(PIR_right) or GPIO.input(PIR_left) or GPIO.input(PIR_back):
        GPIO.output(DC_EN, GPIO.HIGH)
        
GPIO.cleanup()

    

