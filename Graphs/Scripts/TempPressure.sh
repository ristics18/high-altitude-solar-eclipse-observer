#!/bin/bash

#    Authors: Srdan Ristic, Josh Schools
#    Date last modified: 05/10/2017
#    Copyright 2017, Louisiana State University Shreveport

gnuplot -persist <<-EOFMarker

#Uncomment the following line if the first line of a data file is a header.
#set key autotitle columnhead
set title "Temperature (BMP280) vs. Pressure"
set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor rgb "white" behind
set term png
set terminal png size 1024,768
set output "TempPressure.png"
#set xdata time
set datafile separator ","
#set timefmt '%d %b %Y  %H:%M:%S'
set size 1,1
set xlabel 'Temperature (C)'
set ylabel 'Pressure (kPa)'
#set term x11
plot 'Data.csv' using 12:13 #with lines lw 1.5
EOFMarker
