#blink yellow (ch 15 grn + ch 29 red) for button 2 (ch 5)
import RPi.GPIO as GPIO
import time
import os
import subprocess

GPIO.setmode(GPIO.BOARD)
#GPIO.setup(00, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)


for i in range(5):
    GPIO.output(15, GPIO.LOW)
    GPIO.output(29, GPIO.LOW)
    time.sleep(.4)
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(29, GPIO.HIGH)
    time.sleep(.4)

GPIO.cleanup()
exit()
