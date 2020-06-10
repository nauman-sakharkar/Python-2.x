import time
import serial
ser=serial.Serial('/dev/serial0',9600)
while True:
	ser.write('HI STUDENTS I AM XXXX')
           time.sleep(10)
