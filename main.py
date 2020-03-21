from servo import *
from TempSensor import *
from DistanceSensor import *
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

global program
program = "manual"
global program_flag
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

# def polling_thread():
#     response_dict = dict()
#     global Temperature
#     global Humidity
#     global program
#     global program_flag
#     while(True):
#         data = urlencode({"humidity":Humidity,"temperature":Temperature}).encode()
#         url = 'http://shadyganem.com/dataExchange.php'
#         try:
#             with urllib.request.urlopen(url,data) as response:
#                 res = response.read(100)
#                 response_dict = json.loads(res.decode())

#             mode = response_dict.get("mode","manual")
#             global program_flag
#             if mode == "manual":
#                 command["motor1"] = int(response_dict.get("motor1",90))
#                 command["motor2"] = int(response_dict.get("motor2",90))
#                 command["motor5"] = int(response_dict.get("motor5",90))
#                 command["motor3"] = int(response_dict.get("motor3",90))
#                 command["motor4"] = int(response_dict.get("motor4",90))
#             else:
#                 print("selected mode = {}".format(mode))
#                 program = mode
                

#             for key,val in response_dict.items():
#                 print(key+" : "+val)
#         except Exception as e:
#             print("\033[91mConnection with server is down\033[0m {}".format(str(e)))

def main2():
    global Temperature
    global Humidity
    global program
    global program_flag
    import socket
    Host = "160.153.249.247"
    Port = 1234
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((Host,Port))
        print("connected")

        while True:
            out_msg = '{"humidity":"' + str(Humidity) +'","temperature":"' + str(Temperature) + '"}'
            client_socket.send(bytes(out_msg,'utf-8'))
            msg = client_socket.recv(1024)
            print(msg.decode('utf-8'))
            response_dict = json.loads(msg.decode('utf-8'))
            mode = response_dict.get("mode","manual")
            if mode == "manual":
                command["motor1"] = int(response_dict.get("motor1",90))
                command["motor2"] = int(response_dict.get("motor2",90))
                command["motor5"] = int(response_dict.get("motor5",90))
                command["motor3"] = int(response_dict.get("motor3",90))
                command["motor4"] = int(response_dict.get("motor4",90))
            else:
                print("selected mode = {}".format(mode))
                program = mode
    except Exception as e:
        client_socket.close()
        print("socket closed")
        raise e
    except KeyboardInterrupt:
        print("FUCK YOU ALL")
    finally:
        client_socket.close()





def main():
    global program
    global program_flag
    get_commamds = threading.Thread(target=main2)
    get_commamds.start()

    read_sensor = threading.Thread(target=update_sensor_vals)
    read_sensor.start()

    distance_sensor = dist_sensor(4,17)
    driver = servo_driver()
    motor1 = motor(driver,0,90)
    motor2 = motor(driver,3,0)
    motor3 = motor(driver,6,0)
    motor4 = motor(driver,9,0)
    motor5 = motor(driver,12,0)
    virtual_motor = motor(driver,15,0)

    while(True):
        if program == "manual":
            motor1.set_angle(command["motor1"])
            motor2.set_angle(command["motor2"])
            motor3.set_angle(command["motor3"])
            motor4.set_angle(command["motor4"])
            motor5.set_angle(command["motor5"])
            virtual_motor.set_angle(90)
            
        elif program == "program1":
            program_flag = True


            print("running program1")
            


            program = "manual"


    get_commamds.join()

if __name__=="__main__":
    main()
