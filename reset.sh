#!/bin/bash

#    File name: reset.py
#    Authors: Srdan Ristic, Josh Schools
#    Date last modified: 05/10/2017
#    Copyright 2017, Louisiana State University Shreveport

cd /home/pi/Backup/
rm -f *.csv
cd /home/pi/Payload/
rm -f Data.csv
cd /home/pi/Payload/Output/
rm -f *.csv
cd /home/pi/Payload/Output/Images/
rm -f *.jpg
cd /home/pi/Payload/Graphs/PNG/
rm -f *.png
