#raise_z.py
import serial
import RPi.GPIO as GPIO
import time

try:
    s = serial.Serial('/dev/ttyACM1',115200)
except:
    s = serial.Serial('/dev/ttyACM0',115200)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)

s.write(b"\r\n\r\n")
time.sleep(2)   # Wait for grbl to initialize
s.flushInput()  # Flush startup text in serial input
s.write(b'$x\n')
time.sleep(2)   # Wait for grbl to initialize
s.flushInput()  # Flush startup text in serial input

l = "G0 z" + str(25)
s.write(l.encode('utf-8') + b'\n')

print("z raise complete")

s.close()
GPIO.cleanup()
exit(0)
