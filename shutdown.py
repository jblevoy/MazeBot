#shutdown 
import RPi.GPIO as GPIO
import time
import os
import subprocess

os.system("sudo shutdown -h now")

print("from shutdown.py, shutdown -h command issued")

exit(0)
