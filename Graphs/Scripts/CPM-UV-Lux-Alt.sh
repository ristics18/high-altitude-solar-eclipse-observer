#!/bin/bash

#    File name: reset.py
#    Authors: Srdan Ristic, Josh Schools
#    Date last modified: 05/10/2017
#    Copyright 2017, Louisiana State University Shreveport

gnuplot -persist <<-EOFMarker

#Uncomment the following line if the first line of a data file is a header.
#set key autotitle columnhead
set title "CPM vs UV vs Luminosity vs Altitude"
set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor rgb"white" behind
set term png
set terminal png size 1024,768
set output "CPMvsUVvsLuminosityvsAltitude.png"
set xdata time
set datafile separator ","
set timefmt '%d %b %Y  %H:%M:%S'
set size 1,1
set xlabel 'Time'
set ylabel 'Altitude'
#set term x11
set logscale y 1.1
plot 'Data.csv' using 1:14 title 'Altitude' with lines,\
     'Data.csv' using 1:17 title 'CPM' with lines,\
     'Data.csv' using 1:23 title 'UV Index' with lines,\
     'Data.csv' using 1:24 title 'Luminosity' with lines
#set log y
EOFMarker

