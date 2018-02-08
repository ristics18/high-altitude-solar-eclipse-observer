#!/usr/bin/env python

import logging
import time
import os.path
import datetime
from Adafruit_BNO055 import BNO055

bno = BNO055.BNO055()


# Get Calibration status
sys, gyro, accel, mag = bno.get_calibration_status()
print "---------------------------------------------"
print "|Calibration: Sys:",sys,"Gyro:",gyro,"Accel:",accel,"Mag:",mag,"|"
print "---------------------------------------------"

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

# Read X Y Z W Quaternion values
x, y, z, w = bno.read_quaternion()
'''
print "X: ",x
print "Y: ",y
print "Z: ",z
print "W: ",w
'''


# Write to file
file = open("/home/pi/Payload/Output/BNO055.csv","a")
file.write((time.strftime("%d %b %Y %H:%M:%S"))+","+str(heading)+","+str(roll)+","+str(pitch)+","+str(x)+","+str(y)+","+str(z)+","+str(w)+"\n")
file.close()

