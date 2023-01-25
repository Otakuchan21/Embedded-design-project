import os
import time
from datetime import datetime

file_path_on_pi = '/home/pi/sensor_data.csv'
file_on_pi = open(file_path_on_pi, "a")

flash_drive = '/media/pi/My Drive/'
file_path_on_flash = flash_drive + 'sensor_data.csv'
file_on_flash = open(file_path_on_flash, "a")

if os.stat(file_path_on_pi).st_size == 0:
    file_on_pi.write("Time,Sensor1,Sensor2,Sensor3\n")
    file_on_flash.write("Time,Sensor1,Sensor2,Sensor3\n")

while True:
    now = datetime.now()
    # read sensor data
    sensor1 = 1
    sensor2 = 2
    sensor3 = 3
    file_on_pi.write(str(now)+","+str(sensor1)+","+str(sensor2)+","+str(sensor3)+"\n")
    file_on_flash.write(str(now)+","+str(sensor1)+","+str(sensor2)+","+str(sensor3)+"\n")
    file_on_pi.flush()
    file_on_flash.flush()
    time.sleep(1)

file_on_pi.close()
file_on_flash.close()

