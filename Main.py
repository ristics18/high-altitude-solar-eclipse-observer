#!/usr/bin/python

#    File name: Main.py
#    Authors: Srdan Ristic, Josh Schools
#    Date last modified: 05/10/2017
#    Copyright 2017, Louisiana State University Shreveport

import os
import time
import RPi.GPIO as GPIO
from datetime import datetime
from threading import Thread

outputFile = "/home/pi/Payload/Data.csv"

# Setup LED lightst
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)


class runSensors(Thread):
      def run(self):
	while True:
	  print time.strftime("%d %b %Y %H:%M:%S")+" Gathering Data"
	  GPIO.output(20, True)
	  os.system('python /home/pi/Payload/Sensors/BMP280/code/measure.py &')
	  os.system('python /home/pi/Payload/Sensors/BNO055.py &')
          os.system('python /home/pi/Payload/Sensors/geigerRead.py &')
	  os.system('python /home/pi/Payload/Sensors/3temp.py &')
	  os.system('python /home/pi/Payload/Sensors/SI1145/TestSI1145.py &')
	  os.system('python /home/pi/Payload/Sensors/TSL2561/tsl2561.py &')
	  os.system('/home/pi/Payload/Sensors/coreTemp.sh &')
	  os.system('/home/pi/Payload/Sensors/camera.sh &')
	  print time.strftime("%d %b %Y %H:%M:%S")+" Done gathering Data"
	  GPIO.output(20, False)
	  time.sleep(20)

class appendToDataCSV(Thread):
    def run(self):
      while True:
	print time.strftime("%d %b %Y %H:%M:%S")+" Updating Data.csv"
	GPIO.output(21, True)	
	with open(outputFile, "a") as f:
	  for filename in os.listdir('/home/pi/Payload/Output/'):
    	    if filename.endswith(".csv"): 
              with open('/home/pi/Payload/Output/' + filename, "r") as file:
                for line in file:
                  pass
                  rawData = line.strip()
		  f.close()
              with open(outputFile, "a") as f:
		if filename == 'BNO055.csv':
		  f.write(time.strftime("%d %b %Y %H:%M:%S") + ',')
		arrayData = rawData.split(",")
		arrayData.pop(0)
		for val in arrayData:
		  f.write(val + ',')
	  with open(outputFile, "a") as f:
	    f.write('\n')
	    f.close()
	  print time.strftime("%d %b %Y %H:%M:%S")+" Updated Data.csv"
	  GPIO.output(21, False)
    	  time.sleep(60)

try:
  if __name__=='__main__':
    os.system('/home/pi/Payload/Sensors/BNOCalibrate.py')
    os.system('/home/pi/Payload/Sensors/gps_startup.sh')
    a = runSensors()
    b = appendToDataCSV()
    a.start()
    time.sleep(10)
    with open(outputFile, "a") as f:
      f.write('Date,Heading,Roll,Pitch,Sys_cal,Gyro_cal,Accel_cal,Mag_cal,GPSLat,GPSLong,GPSAlt,ExternalTemperature,Pressure,Altitude,InsideTemperature,CPS,CPM,UsvHr,CoreTemperature1,CoreTemperature2,VisibleLight,IR,UVIndex,Luminosity, \n')
      f.close()
    b.start()
except Exception as e:
	errorFile = open("/home/pi/Payload/Errors.txt", "a")
	errorFile.write(str(e))
	errorFile.close()
	print('Exception thrown! Please check Errors.txt file.')
