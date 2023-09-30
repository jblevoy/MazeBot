#flash red (ch 23) for button 1 (ch 3)
import RPi.GPIO as GPIO
import time
import os
import subprocess
#flash red (channel 23) for button 1 (channel 3)
GPIO.setmode(GPIO.BOARD)
#GPIO.setup(XX, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.OUT)


for i in range(10):
    GPIO.output(23, GPIO.LOW)
    time.sleep(.1)
    GPIO.output(23, GPIO.HIGH)
    time.sleep(.1)

GPIO.cleanup()
exit()
