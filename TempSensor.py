import Adafruit_DHT

class temp_sensor:
    def __init__(self,GPIO_PIN):
        self.pin = GPIO_PIN

    def get_temp_and_hum(self):
        return Adafruit_DHT.read_retry(Adafruit_DHT.DHT11 , self.pin)

    def get_temperature(self):
        temperature , humidity =  Adafruit_DHT.read_retry(Adafruit_DHT.DHT11 , self.pin)
        return humidity

    def get_humidity(self):
        temperature , humidity =  Adafruit_DHT.read_retry(Adafruit_DHT.DHT11 , self.pin)
        return temperature
