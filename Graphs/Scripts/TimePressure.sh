#!/bin/bash

#    Authors: Srdan Ristic, Josh Schools
#    Date last modified: 05/10/2017
#    Copyright 2017, Louisiana State University Shreveport

gnuplot -persist <<-EOFMarker

#Uncomment the following line if the first line of a data file is a header.
#set key autotitle columnhead
set title "Pressure vs. Time"
set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor rgb "white" behind
set term png
set terminal png size 1024,768
set output "TimePressure.png"
set datafile separator ","
set size 1,1
set xdata time
set timefmt '%d %b %Y  %H:%M:%S'
set xlabel 'Time '
set ylabel 'Pressure (kPa)'
#set term x11
plot 'Data.csv' using 1:13 title 'Pressure (kPa)' with lines lw 2
EOFMarker
