#blink green (channel 21) for button 4 (channel 11)
import RPi.GPIO as GPIO
import time
import os
import subprocess

GPIO.setmode(GPIO.BOARD)
#GPIO.setup(00, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.OUT)


for i in range(5):
    GPIO.output(21, GPIO.LOW)
    time.sleep(.4)
    GPIO.output(21, GPIO.HIGH)
    time.sleep(.4)

GPIO.cleanup()
exit()
