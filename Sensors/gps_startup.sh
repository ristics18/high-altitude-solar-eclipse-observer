#!/bin/bash

#    Authors: Srdan Ristic, Josh Schools
#    Date last modified: 05/10/2017
#    Copyright 2017, Louisiana State University Shreveport

#echo "Killing any GPSD sockets"
sudo killall -9 gpsd
sudo killall -9 gps_service.py
#echo "Completed"
#echo "Creating GPSD socket on USB0"
sudo gpsd /dev/ttyS0 -F /var/run/gpsd.sock
#echo "Completed"
#echo "Starting GPS Python script"
cd /home/pi/Payload/Sensors
./gps_service.py &
#echo "Completed"

