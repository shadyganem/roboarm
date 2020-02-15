from DistanceSensor import *
 
if __name__ == '__main__':
    DS = dist_sensor(4,17)
    while True:
        dist = DS.get_distance()
        print("Measured Distance = %.1f cm" % dist)
