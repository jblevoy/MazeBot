import RPi.GPIO as GPIO
import time
import os
import subprocess

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #button 1
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #button 2
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #button 3
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #button 4
GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #direct ground from probe


b3pt=0
b3c=0
b5pt=0
b5c=0
b7pt=0
b7c=0
b11pt=0
b11c=0

#indicator light cascade intro
subprocess.Popen("python /home/pi/Documents/Manager/boot_up.py", shell=True)

while True:

    #print("manager.py: in main while")
    #short press:maze run, long press:kill. button:pin3 
    while GPIO.input(3)==0 and b3c<15 and time.time()-b3pt>3:
        time.sleep(.025)
        b3c+=1
        print("b3c ",b3c)
    if b3c >= 1 and b3c < 15:
        print("short press")
        b3c=0
        b3pt=time.time()
        subprocess.Popen("python /home/pi/Documents/Manager/maze_play.py", shell=True)      
        subprocess.Popen("python /home/pi/Documents/Manager/ylw_blnk_btn1.py", shell=True)      
        print("manager.py: short press: gpio3 run maze_play.py")
    if b3c >= 15:
        b3c=0
        b3pt=time.time()
        os.system("pkill -9 -f /home/pi/Documents/Manager/maze_play.py")
        subprocess.Popen("python /home/pi/Documents/Manager/red_flsh_btn1.py", shell=True)      
        print("manager.py: long press: gpio3 pkill maze_play.py")
        
    
    #short press:center x,y to walls, long press:kill. button:pin5 
    while GPIO.input(5)==0 and b5c<15 and time.time()-b5pt>3:
        time.sleep(.025)
        b5c+=1
        print("new b5c in while ",b5c)
    if b5c >= 1 and b5c < 15:
        b5c=0
        b5pt=time.time()
        subprocess.Popen("python /home/pi/Documents/Manager/center_xy.py", shell=True)
        subprocess.Popen("python /home/pi/Documents/Manager/ylw_blnk_btn2.py", shell=True)      
        print("manager.py: short press: gpio5 center_xy.py")
    if b5c >= 15:
        b5c=0
        b5pt=time.time()
        os.system("pkill -9 -f /home/pi/Documents/Manager/center_xy.py")
        subprocess.Popen("python /home/pi/Documents/Manager/red_flsh_btn2.py", shell=True)      
        print("manager.py: long press: gpio5 in pkill center_xy.py")
   
    #short press:raise z axis, long press:lower. button:pin7 
    while GPIO.input(7)==0 and b7c<15 and time.time()-b7pt>3:
        time.sleep(.025)
        b7c+=1
        print("b7c in while ",b7c)
    if b7c >= 1 and b7c < 15:
        b7c=0
        b7pt=time.time()
        subprocess.Popen("python /home/pi/Documents/Manager/raise_z.py", shell=True)
        subprocess.Popen("python /home/pi/Documents/Manager/ylw_blnk_btn3.py", shell=True)
        print("manager.py: short press: gpio7 run raise_z.p")
    if b7c >= 15:
        b7c=0
        b7pt=time.time()
        subprocess.Popen("python /home/pi/Documents/Manager/lower_z.py", shell=True)
        subprocess.Popen("python /home/pi/Documents/Manager/ylw_blnk_btn3.py", shell=True)
        print("manager.py: long press: gpio7 run lower_z.py")

    #short press:reboot, long press:shutdown. button:pin11 
    while GPIO.input(11)==0 and b11c<15 and time.time()-b11pt>3:
        time.sleep(.025)
        b11c+=1
        print("b11c in while ",b11c)
    if b11c >= 1 and b11c < 15:
        b11c=0
        b11pt=time.time()
        subprocess.Popen("python /home/pi/Documents/Manager/reboot.py", shell=True)
        os.system("pkill -9 -f /home/pi/Documents/Manager/status_btn4.py")
        subprocess.Popen("python /home/pi/Documents/Manager/ylw_blnk_btn4.py", shell=True)
        print("manager.py:short press: gpio11 run reboot.py")
    if b11c >= 15:
        b11c=0
        b11pt=time.time()
        subprocess.Popen("python /home/pi/Documents/Manager/shutdown.py", shell=True)
        os.system("pkill -9 -f /home/pi/Documents/Manager/status_btn4.py")
        subprocess.Popen("python /home/pi/Documents/Manager/ylw_blnk_btn4.py", shell=True)
        print("manager.py: long press: gpio11 run shutdown.py")





        
GPIO.cleanup()    
exit(0)
