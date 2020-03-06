from TempSensor import *
from servo import *
import sys

if __name__ == '__main__':
    angle = sys.argv[1]
    motor_i = sys.argv[2]


    m_to_c_dict = dict()
    m_to_c_dict['1'] = 7
    m_to_c_dict['2'] = 1
    m_to_c_dict['3'] = 2
    m_to_c_dict['4'] = 3
    m_to_c_dict['5'] = 4

    channel =  m_to_c_dict[motor_i]

    motor1 = motor(channel,90)

    motor1.set_angle(int(angle))





    # DHT11 = temp_sensor(23)
    # while True:
    #     Humidity , Temperature = DHT11.get_temp_and_hum()
    #     print("Temperature : {}C, Humidity : {}%".format(Temperature, Humidity))