import serial
import RPi.GPIO as GPIO
import time

try:
    s = serial.Serial('/dev/ttyACM0',115200)
except:
    s = serial.Serial('/dev/ttyACM1',115200)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)

s.write(b"\r\n\r\n")
time.sleep(2)   # Wait for grbl to initialize
s.flushInput()  # Flush startup text in serial input
s.write(b'$x\n')
time.sleep(2)   # Wait for grbl to initialize
s.flushInput()  # Flush startup text in serial input

x=0
y=0
z=0
yt=0  #y timer
xt=0  #x timer
t1=0
t2=0
#ydb=0  #y debounce (declared when used)
#xdb=0  #x debounce (declared when used)
contact=False
north=True
south=True
east=True
west=True

while contact==False:   #home y

    t1=time.time()
    while time.time()-t1 < .01 and contact==False: 
        #print("contact in y while", contact)
        ydb=0
        if GPIO.input(40):
            #print("y: 40 True")
            pass
        while GPIO.input(40)==False and ydb < 10: #false reading resiliency
            ydb+=1
            #print("ydb ",ydb) #misreads happen all the time!! ydb=1, ydb=1, etc
            if ydb>=10:
                contact=True

    if yt<=30 and north==True and contact==False:
        #print("y in north is True")
        south=False
        y+=1.5
        yt+=1
        if yt==30:
            north=False
            south=True
    if north==False and contact==False:
        #print("y in north is False")
        y-=1.5
        yt-=1
        south=True
        
    #print("y contact ",contact)
    #print("y,yt ",y,yt)
    l = "G0 y" + str(y)
    if contact==False:
        s.write(l.encode('utf-8') + b'\n')
    time.sleep(abs(.04-(time.time()-t1)))
    #print("(abs(.04-(time.time()-t2))) ",.04-(time.time()-t1))    
    #print("t1 elapsed ",time.time()-t1)
    
time.sleep(.1)
if north==True:
    y=y-18
if south==True:
    y=y+18
l = "G0 y"+str(y)
s.write(l.encode('utf-8') + b'\n')
time.sleep(.5)
contact=abs(GPIO.input(40)-1)
#print("contact on exit y ",contact)
print("y homed")


while contact==False:   #home x
    t2=time.time()
    
    while time.time()-t2 < .01 and contact==False:
        #print("contact in x while", contact)
        xdb=0
        if GPIO.input(40):
            #print("x: 40 True")
            pass
        while GPIO.input(40)==False and xdb < 10:  #false reading resiliency
            xdb+=1
            #print("xdb",xdb)
            if xdb>=10:
                contact=True
            
    if xt<=30 and east==True and contact==False:
        #print("x in east is True")
        west=False
        x+=1.5
        xt+=1
        if xt==30:
            east=False
            west=True
    if east==False and contact==False:
        #print("x in east is False")
        x-=1.5
        xt-=1
        west=True
    #print("x contact ",contact)
    #print("x,xt ",x,xt)
    l = "G0 x" + str(x)
    if contact==False:
        s.write(l.encode('utf-8') + b'\n')
    time.sleep(abs(.04-(time.time()-t2)))
    #print("(abs(.04-(time.time()-t2))) ",.04-(time.time()-t2))    
    #print("t2 elapsed ",time.time()-t2)
    
time.sleep(.1)
if east==True:
    x=x-18
    #print("x-18")
if west==True:
    x=x+18
    #print("x+18")
l = "G0 x"+str(x)
s.write(l.encode('utf-8') + b'\n')
time.sleep(.1)
print("x homed")

s.close()
GPIO.cleanup()
print("x,y homing complete")
exit(0)
