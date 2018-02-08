#!/bin/bash

#    Authors: Srdan Ristic, Josh Schools
#    Date last modified: 05/10/2017
#    Copyright 2017, Louisiana State University Shreveport

gnuplot -persist <<-EOFMarker

#Uncomment the following line if the first line of a data file is a header.
#set key autotitle columnhead
set title "Temperature (BMP280 Sensor)/Pressure over Time"
#set grid x y2
set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor rgb "white" behind
set term png
set terminal png size 1024,768
set output "TempPressureTime.png"
set xdata time
set datafile separator ","
set timefmt '%d %b %Y  %H:%M:%S'
set size 1,1
set xlabel 'Time'
set ylabel 'Temperature (C)'
set y2label 'Pressure (kPa)'
#set term x11
set y2tics #nomirror
set yrange[0:50]
set y2range[75000:150000]
#set logscale y 10
#unset logscale y2
plot 'Data.csv' using 1:12 title 'Temperature (C)' with lines lw 2 axes x1y1,\
     'Data.csv' using 1:13 title 'Pressure (kPa)' with lines lw 2 axes x1y2
EOFMarker
