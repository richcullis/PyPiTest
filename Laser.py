__author__ = 'root'
import RPi.GPIO as GPIO
import time

#make the laser fire

#This is a test to see if i can edit the code in visual studio and run on the pi

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)


GPIO.output(40, GPIO.HIGH)

time.sleep(2)

GPIO.output(40, GPIO.LOW)

time.sleep(2)

GPIO.output(40, GPIO.HIGH)

time.sleep(2)

GPIO.output(40, GPIO.LOW)

time.sleep(2)

GPIO.output(40, GPIO.HIGH)

time.sleep(2)

GPIO.output(40, GPIO.LOW)

time.sleep(2)

GPIO.output(40, GPIO.HIGH)

time.sleep(2)