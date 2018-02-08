#! /usr/bin/python

import os
from gps import *
from time import *
import time
import threading

gpsd = None

class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd
    gpsd = gps(mode=WATCH_ENABLE)
    self.current_value = None
    self.running = True

  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next()

if __name__ == '__main__':
  gpsp = GpsPoller()
  try:
    gpsp.start()
    while True:
      f = open("/home/pi/Payload/Output/gps_data.csv", "a")
      f.write(time.strftime("%b %d %Y %H:%M:%S") + "," + str(gpsd.fix.latitude) + "," + str(gpsd.fix.longitude) + "," + str(gpsd.fix.altitude) +"\n")
      f.close()
      time.sleep(5)

  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing

