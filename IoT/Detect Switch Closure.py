import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.IN)
GPIO.setup(16,GPIO.IN)
 
while True:
    reading = GPIO.input(19)
    if reading == 0:
	print "FIRST BUTTON Pressed"
		
    reading1= GPIO.input(16)
    if reading1 == 0:
	print "SECOND BUTTON Pressed"
    time.sleep(0.2)
