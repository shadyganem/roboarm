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


class servo_driver:
    def __init__(self):
        self.i2c = busio.I2C(SCL,SDA)
        self.pca = PCA9685(self.i2c)
        self.pca.frequency = 50

    def get_channel(self,channel):
        return self.pca.channels[channel]

class motor():
    def __init__(self,driver,channel,offset):
        self.offset = offset
        my_channel = driver.get_channel(channel)
        self.servo = servo.Servo(my_channel)
        
    def set_angle(self,direction):
        self.servo.angle = direction + self.offset
        time.sleep(0.5)