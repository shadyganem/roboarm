from servo import *
from TempSensor import *
import time
import threading
import json

import urllib.request
from urllib.parse import urlencode


from programs import *

DHT11 = temp_sensor(23)

command = dict()
command["motor1"] = 0  #base left right
command["motor2"] = 0  #arm up down
command["motor3"] = 0  #arm forward backward
command["motor4"] = 0  #gripper clockwise counter clockwose
command["motor5"] = 90 #gripper open close
program = "manual"
program_flag = False

global Humidity
Humidity = 0
global Temperature
Temperature = 0

def update_sensor_vals():
    global Humidity
    global Temperature
    while(True):
        Humidity , Temperature = DHT11.get_temp_and_hum()

        time.sleep(0.2)

def polling_thread():
    response_dict = dict()
    global Temperature
    global Humidity
    while(True):
        print("humidity {}".format(Humidity))
        print("Temperature {}".format(Temperature))
        data = urlencode({"humidity":Humidity,"temperature":Temperature}).encode()
        url = 'http://shadyganem.com/dataExchange.php'
        try:
            with urllib.request.urlopen(url,data) as response:
                res = response.read(100)
                response_dict = json.loads(res.decode())

            mode = response_dict.get("mode","manual")
            global program_flag
            if mode == "manual":
                command["motor1"] = int(response_dict.get("motor1",90))
                command["motor2"] = int(response_dict.get("motor2",90))
                command["motor5"] = int(response_dict.get("motor5",90))
                command["motor3"] = int(response_dict.get("motor3",90))
                command["motor4"] = int(response_dict.get("motor4",90))
            elif program_flag == True:
                print("selected mode = {}".format(mode))
                program = mode
                program_flag = False

            for key,val in response_dict.items():
                print(key+" : "+val)
        except:
            print("\033[91mConnection with server is down\033[0m")


def main():

    get_commamds = threading.Thread(target=polling_thread)
    get_commamds.start()

    read_sensor = threading.Thread(target=update_sensor_vals)
    read_sensor.start()

    driver = servo_driver()
    motor1 = motor(driver,0,90)
    motor2 = motor(driver,3,0)
    motor3 = motor(driver,6,0)
    motor4 = motor(driver,9,0)
    motor5 = motor(driver,12,0)

    while(True):
        if program == "manual":
            motor1.set_angle(command["motor1"])
            motor2.set_angle(command["motor2"])
            motor3.set_angle(command["motor3"])
            motor4.set_angle(command["motor4"])
            motor5.set_angle(command["motor5"])
        elif program == "program1":
            if program_flag == False:
                program_list = programs_dict[program]
                print(prograam_list)
                for angle_list in program_list:
                    motor1.set_angle(angle_list[0])
                    motor2.set_angle(angle_list[1])
                    motor3.set_angle(angle_list[2])
                    motor4.set_angle(angle_list[3])
                    motor5.set_angle(angle_list[4])
                program_flag = True
    get_commamds.join()

if __name__=="__main__":
    main()
