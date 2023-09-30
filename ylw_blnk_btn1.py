#blink yellow (ch 13 grn + ch 23 red) for button 1 (ch 3)
import RPi.GPIO as GPIO
import time
import os
import subprocess

GPIO.setmode(GPIO.BOARD)
#GPIO.setup(00, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)


for i in range(5):
    GPIO.output(13, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    time.sleep(.4)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    time.sleep(.4)

GPIO.cleanup()
exit()
