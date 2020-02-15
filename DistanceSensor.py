#Libraries
import RPi.GPIO as GPIO
import time

class dist_sensor:
    def __init__(self,GPIO_TRIGGER,GPIO_ECHO):
        #GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)
        #set GPIO direction (IN / OUT)
        GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(GPIO_ECHO, GPIO.IN)
        self.echo = GPIO_ECHO
        self.trigger = GPIO_TRIGGER
        self.time_limit = 0.002332361 # coresponds to 40 cm
        self.StartTime = 0
        self.StopTime = 0

    def __del__(self):
        print("dist sensor destroyed")
        GPIO.cleanup()

    def _send_trriger_pulse(self):
        GPIO.output(self.trigger, True)
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.trigger, False)

    def _start_time(self):
        time_elapsed = 0
        timer =  time.time()
        while GPIO.input(self.echo) == 0 and time_elapsed < 0.05:
            time_elapsed = time.time() - timer
        self.StartTime = time.time()

    def _stop_time(self):
        time_elapsed = 0
        timer =  time.time()
        while GPIO.input(self.echo) == 1 and time_elapsed < 0.02:
            time_elapsed = time.time() - timer
        self.StopTime = time.time()
        for x in range(100):
            if GPIO.input(self.echo) == 1:
                self.StopTime = time.time()

            


    def _calc_distance(self):
        TimeElapsed = abs(self.StopTime - self.StartTime)
        return (TimeElapsed * 34300) / 2

    def get_distance(self):

        distance = 0


        for i in range(20):
            self._send_trriger_pulse()
            self._start_time()
            self._stop_time()
            distance = self._calc_distance()
            if  5<= distance <= 100:
                break
        
        if distance < 5 :
            return -1
        else:
            return distance

        # while  distance < 5 or distance > 40:
        #     self._send_trriger_pulse()
        #     self._start_time()
        #     self._stop_time()
        #     distance = self._calc_distance()


        
        # print(distances_list)
        # final_list = list()
        # for dist in distances_list:
        #     if 5 <= dist <= 40:
        #         final_list.append(dist)




        # if len(final_list) == 0:
        #     return 0
        # else:
        #     return sum(final_list) / float(len(final_list))
        

        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        


