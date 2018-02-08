#!/usr/bin/env python

import logging
import time
import os.path
import datetime
from Adafruit_BNO055 import BNO055

bno = BNO055.BNO055()

while True:
# Get Calibration status
  sys, gyro, accel, mag = bno.get_calibration_status()

  print "------------------"
  print "Sys Cal",sys
  print "Gyro Cal",gyro
  print "Accel Cal",accel
  print "Mag Cal",mag
  print "------------------"


# Read the Euler angles for heading, roll, pitch (all in degrees).
  heading, roll, pitch = bno.read_euler()

# Read BNO055 Temperature
  temp = bno.read_temp()  

# Print out information
  '''
  print "Heading",heading
  print "Roll",roll
  print "Pitch",pitch
  print "Temp",temp
  '''
  x, y, z, w = bno.read_quaternion()
  print "X: ",x
  print "Y: ",y
  print "Z: ",z
  print "W: ",w

# Write to file
  file = open("/home/pi/Payload/Output/BNO055.csv","a")
  file.write((time.strftime("%d %b %Y %H:%M:%S"))+","+str(heading)+","+str(roll)+","+str(pitch)+","+str(temp)+","+str(gyro)+","+str(accel)+","+str(mag)+"\n")
  file.close()
  time.sleep(1)
