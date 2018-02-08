#!/usr/bin/python

#    Authors: Srdan Ristic, Josh Schools
#    Date last modified: 05/10/2017
#    Copyright 2017, Louisiana State University Shreveport

import os

print('Copying Data.csv file to Graphs folder...')
#os.system('cp /home/pi/Payload/Data.csv /home/pi/Payload/Graphs')
print('Done moving Data.csv file to Graphs folder.')
print("Exporting all graphs...")
os.system('/home/pi/Payload/Graphs/Scripts/4Temp.sh')
os.system('/home/pi/Payload/Graphs/Scripts/AltitudePressure.sh')
os.system('/home/pi/Payload/Graphs/Scripts/BMPTemp.sh')
os.system('/home/pi/Payload/Graphs/Scripts/GPS.sh')
os.system('/home/pi/Payload/Graphs/Scripts/TempAltitude.sh')
os.system('/home/pi/Payload/Graphs/Scripts/TempAltPressure.sh')
os.system('/home/pi/Payload/Graphs/Scripts/TempPressure.sh')
os.system('/home/pi/Payload/Graphs/Scripts/TempPressureTime.sh')
os.system('/home/pi/Payload/Graphs/Scripts/TimeAltitude.sh')
os.system('/home/pi/Payload/Graphs/Scripts/TimePressure.sh')
os.system('/home/pi/Payload/Graphs/Scripts/CPM-Alt.sh')
os.system('/home/pi/Payload/Graphs/Scripts/CPM-Time.sh')
os.system('/home/pi/Payload/Graphs/Scripts/CPM-UV-Lux-Alt.sh')
os.system('/home/pi/Payload/Graphs/Scripts/Lat-Long.sh')
os.system('/home/pi/Payload/Graphs/Scripts/Lux-Time.sh')
os.system('/home/pi/Payload/Graphs/Scripts/UV-Lux-Alt.sh')
os.system('/home/pi/Payload/Graphs/Scripts/UV-Time.sh')
os.system('mv *.png PNG/')
# Add all bash scripts for exporting graphs here
print("Done exporting graphs. Check PNG files.")
