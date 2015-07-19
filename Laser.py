__author__ = 'root'
import RPi.GPIO as GPIO
import time

#make the laser fire

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