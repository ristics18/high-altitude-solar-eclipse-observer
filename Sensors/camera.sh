#!/bin/bash

#    Authors: Srdan Ristic, Josh Schools
#    Date last modified: 05/10/2017
#    Copyright 2017, Louisiana State University Shreveport

DATE=$(date +"%H-%M-%S")
raspistill -o /home/pi/Payload/Output/Images/$DATE.jpg -n
