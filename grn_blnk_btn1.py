#blink green for button 1; gpio channel 13
import RPi.GPIO as GPIO
import time
import os
import subprocess

GPIO.setmode(GPIO.BOARD)
#GPIO.setup(00, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.OUT)


for i in range(5):
    GPIO.output(13, GPIO.LOW)
    time.sleep(.4)
    GPIO.output(13, GPIO.HIGH)
    time.sleep(.4)

GPIO.cleanup()
exit()
