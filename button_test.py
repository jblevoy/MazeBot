import RPi.GPIO as GPIO
import time
import os
import subprocess

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #button 1
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #button 2
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #button 3
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #button 4
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)

while True:
    if GPIO.input(5):
        print("true")
    if GPIO.input(5)==False:
        print("false")

        
GPIO.cleanup()    

