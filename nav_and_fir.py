
#installing packages for sensor https://github.com/adafruit/Adafruit_CircuitPython_AMG88xx
import busio
import board
import adafruit_amg88xx
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
SPR = 48   # Steps per Revolution (360 / 7.5)
MODE = (14, 15, 18)   # Microstep Resolution GPIO Pins
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(EN, GPIO.OUT)
GPIO.output(EN, GPIO.HIGH)#disable first
GPIO.setup(DIR, GPIO.OUT)
GPIO.output(DIR, CW)
GPIO.setup(MODE, GPIO.OUT)
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}
GPIO.output(MODE, RESOLUTION['1/4'])#smaller steps
delay = .0208 / 4

#initilize I2C bus
i2c_bus = busio.I2C(board.SCL, board.SDA)

#constants
threshold=30
distance=400
min_diff=2

###################### meybe this is the general structure ############################
target_found=0
fired=0
while fired==0:
    sensor = adafruit_amg88xx.AMG88XX(i2c_bus)
    #nevigate
    if GPIO.input(PIR_right) or GPIO.input(PIR_left) or GPIO.input(PIR_back):#should this be in nevigation?
        #rotate left/right
    if x_aimed(sensor.pixels):
        #stopbot
        while target_found==0:
            sensor = adafruit_amg88xx.AMG88XX(i2c_bus)
            if aim_y(sensor.pixels)==0:
                GPIO.output(EN, GPIO.LOW)
                GPIO.output(STEP, GPIO.HIGH)
                sleep(delay)
                GPIO.output(STEP, GPIO.LOW)
                sleep(delay)
            else:
                GPIO.output(EN, GPIO.HIGH)
                target_found=1
        GPIO.output(DC_EN, GPIO.HIGH)
        sleep(5)
        GPIO.output(DC_EN, GPIO.LOW)
        fired=1
        
if('''occupancy<99%'''):
    #nevigate
else #stopbot
 
GPIO.cleanup()

#######################################################################################

#check if aimed in x axis
def aim_x(grid):
    x_aimed=0
    if x_flag==0:
        for i in range(8):
            if(grid[i][3]>threshold and grid[i][4]>threshold and abs(grid[i][3]-grid[i][4])<min_diff):
                x_aimed=1
    return x_aimed
    
#check if aimed in y axis
def aim_y(grid):
    y_aimed=0
    if(abs(grid[3][3]-grid[3][4])<min_diff and abs(grid[4][3]-grid[4][4])<min_diff and abs(grid[3][3]-grid[4][4])<min_diff and abs(grid[3][4]-grid[4][3])<min_diff):
        if(grid[3][3]>threshold and grid[3][4]>threshold and grid[4][3]>threshold and grid[4][4]>threshold):
            y_aimed=1
    return y_aimed
    
    
