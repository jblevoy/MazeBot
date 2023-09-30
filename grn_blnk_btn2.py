#blink green (channel 15) for button 2 (channel 5)
import RPi.GPIO as GPIO
import time
import os
import subprocess

GPIO.setmode(GPIO.BOARD)
#GPIO.setup(00, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.OUT)


for i in range(5):
    GPIO.output(15, GPIO.LOW)
    time.sleep(.4)
    GPIO.output(15, GPIO.HIGH)
    time.sleep(.4)

GPIO.cleanup()
exit()
