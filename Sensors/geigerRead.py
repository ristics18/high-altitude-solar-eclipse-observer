#!/usr/bin/python

#    Authors: Srdan Ristic, Josh Schools
#    Date last modified: 05/10/2017
#    Copyright 2017, Louisiana State University Shreveport

import time, os
from timeout import timeout
import errno
import signal

@timeout(5, os.strerror(errno.ETIMEDOUT))
def geigerRead():
  f = open("/dev/ttyUSB0", "r")
  a = f.readline()
  f.close()
  return a

b = geigerRead()
b = b.replace(" ","").split(',')
b[0] = b[0].replace('\x00','')
if "FAST\n" in b:
  b.remove("FAST\n")
b.remove("CPS")
b.remove("CPM")
b.remove("uSv/hr")
b.remove("SLOW\n")


g = open("/home/pi/Payload/Output/geiger.csv","a")
g.write(time.strftime("%d %b %Y %H:%M:%S")+","+str(b[0])+","+str(b[1])+","+str(b[2])+"\n")
g.close()
