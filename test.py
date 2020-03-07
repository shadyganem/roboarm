from TempSensor import *
from servo import *
from DistanceSensor import *
import sys

if __name__ == '__main__':
    # ds = dist_sensor(4,17)
    # while True:
        
    #     distance = ds.get_distance()
    #     print(distance)




    angle = sys.argv[1]
    motor_i = sys.argv[2]


    m_to_c_dict = dict()
    m_to_c_dict['1'] = 0
    m_to_c_dict['2'] = 3
    m_to_c_dict['3'] = 6
    m_to_c_dict['4'] = 9
    m_to_c_dict['5'] = 12

    channel =  m_to_c_dict[motor_i]
    driver = servo_driver()
    motor1 = motor(driver, channel,0)

    motor1.set_angle(int(angle))





    # DHT11 = temp_sensor(23)
    # while True:
    #     Humidity , Temperature = DHT11.get_temp_and_hum()
    #     print("Temperature : {}C, Humidity : {}%".format(Temperature, Humidity))