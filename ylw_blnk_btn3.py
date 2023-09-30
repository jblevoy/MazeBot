#blink yellow (channel 19/grn+31/red) for button 3 (channel 7)
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
#GPIO.setup(00, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)


GPIO.output(31, GPIO.HIGH)
GPIO.output(19, GPIO.HIGH)


for i in range(5):
    
    GPIO.output(31, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    time.sleep(.4)
    GPIO.output(31, GPIO.HIGH)
    GPIO.output(19, GPIO.HIGH)
    time.sleep(.4)

        
GPIO.cleanup()
exit()
