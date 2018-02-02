# import modules
import RPi.GPIO as GPIO
import os
import time
import picamera
import picamera.array

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.IN)
while True:
    if GPIO.input(3) == GPIO.LOW:
        print "low voltage"
    else:
        print "high voltage"


GPIO.cleanup()