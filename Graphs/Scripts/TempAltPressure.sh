#!/bin/bash

#    Authors: Srdan Ristic, Josh Schools
#    Date last modified: 05/10/2017
#    Copyright 2017, Louisiana State University Shreveport

gnuplot -persist <<-EOFMarker

#Uncomment the following line if the first line of a data file is a header.
#set key autotitle columnhead
set title "Temperature/Altitude/Pressure vs. Time" tc lt 4
set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor rgb"white" behind
set terminal pngcairo size 1024,768 font 'Courier,15'
set key below
set output "TempAltPressure.png"
set xdata time
set datafile separator ","
set timefmt '%d %b %Y  %H:%M:%S'
set size 1,1
set xlabel 'Time'
set ylabel 'Temp (C)/ Altitude (m)/ Pressure (kPa)'
#set term x11
set logscale y 1.1
plot 'Data.csv' using 1:12 title 'External Temperature (Celsius)' with lines,\
     'Data.csv' using 1:14 title 'Altitude (m)' with lines,\
     'Data.csv' using 1:13 title 'Pressure (kPa)' with lines

#set log y
EOFMarker
