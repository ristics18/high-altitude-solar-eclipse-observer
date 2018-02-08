#!/usr/bin/python
 
import RPi.GPIO as GPIO
import time
import os

class keypad():
    #Define column count of keypad here
    def __init__(self, columnCount = 4):
        GPIO.setmode(GPIO.BCM)

        # CONSTANTS 
	# 3 column keypad
        if columnCount is 3:
            self.KEYPAD = [
                [1,2,3],
                [4,5,6],
                [7,8,9],
                ["*",0,"#"]
            ]

            self.ROW         = [18,23,24,25]
            self.COLUMN      = [4,17,22]

	# 4 column keypad
        elif columnCount is 4:
            self.KEYPAD = [
                [1,2,3,"A"],
                [4,5,6,"B"],
                [7,8,9,"C"],
                ["*",0,"#","D"]
            ]

            self.ROW         = [18,23,24,25] #BCM numering
            self.COLUMN      = [5,6,13,19] # Changed from [4,17,22,21]
        else:
            return
     
    def getKey(self):
         
        # Set all columns as output low
        for j in range(len(self.COLUMN)):
            GPIO.setup(self.COLUMN[j], GPIO.OUT)
            GPIO.output(self.COLUMN[j], GPIO.LOW)
         
        # Set all rows as input
        for i in range(len(self.ROW)):
            GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
         
        # Scan rows for pushed key/button
        # A valid key press should set "rowVal"  between 0 and 3.
        rowVal = -1
        for i in range(len(self.ROW)):
            tmpRead = GPIO.input(self.ROW[i])
            if tmpRead == 0:
                rowVal = i
                 
        # if rowVal is not 0 thru 3 then no button was pressed and we can exit
        if rowVal <0 or rowVal >3:
            self.exit()
            return
         
        # Convert columns to input
        for j in range(len(self.COLUMN)):
                GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
         
        # Switch the i-th row found from scan to output
        GPIO.setup(self.ROW[rowVal], GPIO.OUT)
        GPIO.output(self.ROW[rowVal], GPIO.HIGH)
 
        # Scan columns for still-pushed key/button
        # A valid key press should set "colVal"  between 0 and 2.
        colVal = -1
        for j in range(len(self.COLUMN)):
            tmpRead = GPIO.input(self.COLUMN[j])
            if tmpRead == 1:
                colVal=j
                 
        # if colVal is not 0 thru 2 then no button was pressed and we can exit
        if colVal <0 or colVal >2:
            self.exit()
            return
 
        # Return the value of the key pressed
        self.exit()
        return self.KEYPAD[rowVal][colVal]

        
    def exit(self):
        # Reinitialize all rows and columns as input at exit
        for i in range(len(self.ROW)):
                GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP) 
        for j in range(len(self.COLUMN)):
                GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_UP)

	#New edition to library file to turn off pins for removal of numeric pad
       # for i in range(len(self.ROW)):
       #         GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP) 
       # for j in range(len(self.COLUMN)):
       #         GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_UP)

"""EDITED LIBRARY SCRIPT ABOVE, SDJAN'S AND ASHTON'S SCRIPTS BELOW"""
#Resets digit  to zero
digit = None

try:         
	if __name__ == '__main__':
		# Initialize the keypad class
		kp = keypad()
		# Loop while waiting for a keypress unless * is pushed, then exits loop
		while digit != '*':	#while digit == None:
			digit = kp.getKey()
			# Print the result
			print digit
			# "*" is the Run-All button cancelling further input and exit()
			if digit == "*":				
				os.system('python /home/rthompson/Desktop/Sensors/Main.py')
				print(os.system('pgrep -f Main.py'))
				exit()
			elif digit == 0:
				#os.system('python /home/rthompson/Desktop/Sensors/')
				
				time.sleep(5)
			elif digit == 1:
				os.system('python /home/rthompson/Desktop/Sensors/BMP280/BMP280/examples/measure.py')
				time.sleep(5)
			elif digit == 2:
				os.system('python /home/rthompson/Desktop/Sensors/BNO055/BNO055.py')
				time.sleep(5)
			elif digit == 3:
				os.system('python /home/rthompson/Desktop/Sensors/DS18B20/3temp.py')
				time.sleep(5)
			elif digit == 4:
				os.system('python /home/rthompson/Desktop/Sensors/HMC5883L/HMC5883L.py')
				time.sleep(5)
			elif digit == 5:
				os.system('python /home/rthompson/Desktop/Sensors/SI1145/TestSI1145.py')
				time.sleep(5)
			elif digit == 6:
				os.system('python /home/rthompson/Desktop/Sensors/TSL2561/ts12561.py')
				time.sleep(5)
			elif digit == 7:
				os.system('python /home/rthompson/Desktop/Sensors/')
				time.sleep(5)
			elif digit == 8:
				os.system('python /home/rthompson/Desktop/Sensors/')
				time.sleep(5)
			elif digit == 9:
				#os.system('python /home/rthompson/Desktop/Sensors/')
				time.sleep(5)
			elif digit == "A":
				#os.system('python /home/rthompson/Desktop/Sensors/')
				time.sleep(5)
			elif digit == "B":
				#os.system('python /home/rthompson/Desktop/Sensors/')
				time.sleep(5)
			elif digit == "C":
				#os.system('python /home/rthompson/Desktop/Sensors/')
				time.sleep(5)
			elif digit == "D":
				#os.system('python /home/rthompson/Desktop/Sensors/')
				time.sleep(5)
			elif digit == "#":
				#os.system('python /home/rthompson/Desktop/Sensors/')
				time.sleep(5)
			#elif digit != None:
				#kp.getKey()
			#	print digit
		#exit()
		#Digit = None
#except digit != "*":
#	exit()
except KeyboardInterrupt:
	exit()
