#!/bin/bash

#    Authors: Srdan Ristic, Josh Schools
#    Date last modified: 05/10/2017
#    Copyright 2017, Louisiana State University Shreveport

CPU_CORE=$(</sys/class/thermal/thermal_zone0/temp)
GPU_CORE=`vcgencmd measure_temp | grep -Eo '[0-9]{1,3}\.[0-9]+'`

echo `date +"%d %B %Y %R:%S" `",$((CPU_CORE/1000)),$GPU_CORE" >> /home/pi/Payload/Output/coreTemperature.csv
