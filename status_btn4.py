#solid green (ch 21) for button 4 (ch 11)
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
#GPIO.setup(00, GPIO.IN, pull_up_down=GPIO.PUD_UP)

time.sleep(1)
GPIO.setup(21, GPIO.OUT)
while True:
    GPIO.output(21, GPIO.LOW)

GPIO.cleanup()
exit()
