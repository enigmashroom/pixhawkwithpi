#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO as GPIO
import time

RPi.GPIO.setmode(GPIO.BOARD)

RPi.GPIO.setup(3, GPIO.OUT)

for i in range(0, 10):

    print(i)

    RPi.GPIO.output(3, True)

    time.sleep(0.5)

    RPi.GPIO.output(3, False)

    time.sleep(2)

RPi.GPIO.cleanup()
