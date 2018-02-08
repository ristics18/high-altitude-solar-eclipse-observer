#!/usr/bin/env python

import logging
import time
import os.path
import datetime
from Adafruit_BNO055 import BNO055

print "Assigning BNO055.BNO055() to bno"
bno = BNO055.BNO055()

# Initialize the BNO055 and stop if something went wrong.
print "Initializing BNO055"
if not bno.begin():
    raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')

# Print system status and self test result.
status, self_test, error = bno.get_system_status()
# Print out an error if system status is in error mode.
if status == 0x01:
    print('System error: {0}'.format(error))
    print('See datasheet section 4.3.59 for the meaning.')

print "Completed...exiting"
time.sleep(10)
