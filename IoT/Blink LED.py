import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT)
while True:
    GPIO.output(21,1)
    time.sleep(0.2)
    GPIO.output(21,0)
    time.sleep(0.2)
