import RPi.GPIO as GPIO
import time



"""
    to get these pachages run 
    1) pip3 insatll 
    2) pip3 install 
"""
from board import SCL,SDA
import busio 

#import from PCA module 
from adafruit_pca9685 import PCA9685

from adafruit_motor import servo


class motor:
    def __init__(self,channel,offset):
        self.channel = channel
        self.i2c = busio.I2C(SCL,SDA)
        self.pca = PCA9685(self.i2c)
        self.pca.frequency = 50
        self.previos_angle = 90
        self.offset = offset
            
    def set_angle(self,direction):
        self.servo = servo.Servo(self.pca.channels[self.channel])
        self.servo.angle = direction
        self.previos_angle = direction
        time.sleep(0.5)