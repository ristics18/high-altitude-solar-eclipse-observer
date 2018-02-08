#!/usr/bin/python

import re, os, time, json, os.path, datetime
from subprocess import call

pathes = (
  "/sys/bus/w1/devices/28-0000065d035a/w1_slave"
)
def read_sensor(path):
  value = ""
  try:
    cutPath = path
    sensorName = cutPath[20:35]
   
    f = open(path, "r")
    line = f.readline()
    if re.match(r"([0-9a-f]{2} ){9}: crc=[0-9a-f]{2} YES", line):
      line = f.readline()
      m = re.match(r"([0-9a-f]{2} ){9}t=([+-]?[0-9]+)", line)
      if m:
        value = str(float(m.group(2)) / 1000.0)
    f.close()
  except (IOError), e:
    print time.strftime("%x %X"), "Error reading", path, ": ", e
  return sensorName + "," + value

sensor1 = read_sensor("/sys/bus/w1/devices/28-0000065d035a/w1_slave").split(",")


fh = open("/home/pi/Payload/Output/insideTemp.csv",'a')
fh.write((time.strftime("%d %b %Y %H:%M:%S")+","+(str(sensor1[1]))+"\n"))
fh.close()


