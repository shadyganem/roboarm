from TempSensor import *

if __name__ == '__main__':
    DHT11 = temp_sensor(23)
    while True:
        Humidity , Temperature = DHT11.get_temp_and_hum()
        print("Temperature : {}C, Humidity : {}%".format(Temperature, Humidity))