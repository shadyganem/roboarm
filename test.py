from servo import *
import time
import threading
import json

# generate random integer values
from random import seed
from random import randint
import urllib.request

command = dict()

 
command["motor1"] = 0  #base left right
command["motor2"] = 0  #arm up down
command["motor3"] = 0  #arm forward backward
command["motor4"] = 0  #gripper clockwise counter clockwose
command["motor5"] = 90 #gripper open close



def main():

    motor1 = motor(14,0)
    motor2 = motor(0,0)
    motor3 = motor(13,0)

    while(True):
        # motor1.set_angle(0)
        # motor1.set_angle(90)
        # motor1.set_angle(180)
        # motor2.set_angle(0)
        # motor2.set_angle(90)
        motor2.set_angle(90)
        # motor3.set_angle(0)
        # motor3.set_angle(90)
        # motor3.set_angle(180)


if __name__=="__main__":
    main()
