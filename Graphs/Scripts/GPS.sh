#!/bin/bash

#    File name: reset.py
#    Authors: Srdan Ristic, Josh Schools
#    Date last modified: 05/10/2017
#    Copyright 2017, Louisiana State University Shreveport

gnuplot -persist <<-EOFMarker

#Uncomment the following line if the first line of a data file is a header.
#set key autotitle columnhead

set term png
set title 'Latitude vs. Longitude'
set output "GPS.png"
set datafile separator ","
set size 1,1
set xlabel 'Latitude'
set ylabel 'Longitude'
#set term x11
plot 'Data.csv' using 9:10 title 'Location' with lines
EOFMarker
