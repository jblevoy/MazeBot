import RPi.GPIO as GPIO
import time
import os
import subprocess

GPIO.setmode(GPIO.BOARD)

GPIO.setup(13, GPIO.OUT)  #button 1 green
GPIO.setup(15, GPIO.OUT)  #button 2 green
GPIO.setup(19, GPIO.OUT)  #button 3 green
GPIO.setup(21, GPIO.OUT)  #button 4 green

GPIO.setup(23, GPIO.OUT)  #button 1 red
GPIO.setup(29, GPIO.OUT)  #button 2 red
GPIO.setup(31, GPIO.OUT)  #button 3 red
GPIO.setup(33, GPIO.OUT)  #button 4 red
GPIO.setup(35, GPIO.OUT)  #button 5 red

GPIO.output(13, GPIO.HIGH)  #turn all channels off
GPIO.output(15, GPIO.HIGH)
GPIO.output(19, GPIO.HIGH)
GPIO.output(21, GPIO.HIGH)

GPIO.output(23, GPIO.HIGH)  #turn all channels off
GPIO.output(29, GPIO.HIGH)
GPIO.output(31, GPIO.HIGH)
GPIO.output(33, GPIO.HIGH)
GPIO.output(35, GPIO.HIGH)

d=.2   #delay between each light change

time.sleep(.1)


GPIO.output(35, GPIO.LOW)   #yellow cascade up
time.sleep(d)
GPIO.output(33, GPIO.LOW)
GPIO.output(21, GPIO.LOW)
time.sleep(d)
GPIO.output(35, GPIO.HIGH)
GPIO.output(31, GPIO.LOW)
GPIO.output(19, GPIO.LOW)
time.sleep(d)
GPIO.output(33, GPIO.HIGH)
GPIO.output(21, GPIO.HIGH)
GPIO.output(29, GPIO.LOW)
GPIO.output(15, GPIO.LOW)
time.sleep(d)
GPIO.output(31, GPIO.HIGH)
GPIO.output(19, GPIO.HIGH)
GPIO.output(23, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
time.sleep(d)
GPIO.output(29, GPIO.HIGH)
GPIO.output(15, GPIO.HIGH)
time.sleep(d)
GPIO.output(23, GPIO.HIGH)
GPIO.output(13, GPIO.HIGH)

GPIO.output(33, GPIO.LOW)   #red cascade up
time.sleep(d)
GPIO.output(31, GPIO.LOW)
time.sleep(d)
GPIO.output(33, GPIO.HIGH)
GPIO.output(29, GPIO.LOW)
time.sleep(d)
GPIO.output(31, GPIO.HIGH)
GPIO.output(23, GPIO.LOW)
time.sleep(d)
GPIO.output(29, GPIO.HIGH)
time.sleep(d)
GPIO.output(23, GPIO.HIGH)

GPIO.output(21, GPIO.LOW)   #green cascade up
time.sleep(d)
GPIO.output(19, GPIO.LOW)
time.sleep(d)
GPIO.output(21, GPIO.HIGH)
GPIO.output(15, GPIO.LOW)
time.sleep(d)
GPIO.output(19, GPIO.HIGH)
GPIO.output(13, GPIO.LOW)
time.sleep(d)
GPIO.output(15, GPIO.HIGH)
time.sleep(d)
GPIO.output(13, GPIO.HIGH)
time.sleep(d)

GPIO.cleanup()
subprocess.Popen("python /home/pi/Documents/Manager/status_btn4.py", shell=True)
exit(0)
