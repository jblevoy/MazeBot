#!/etc/python3
#202008091000
#/home/pi/Documents/Maze/maze_play_06.py
#Author: Jasen Levoy. Co-author & Collaborator: Sam Ellis
#Abstract: This maze-navigation algorithm relies on building a run-time data structure comprised of information brought in through the sensory channels of the machine. These data are used to avoid walls, make decisions for exploration based on a cascading priority list including frequency of visitation and aversion of dead-ends. If a solution exists, once found, the most direct path taken will be retraced to its beginning. 
#Improvement: There is an open question of how the wall test sequence on an unvisited cell seems to be "rushed" and of lower accuracy when the previous cell or cells were pass-thru. The current solution is to detect those conditions and add a delay. An improvement would be to advance an understanding of how this occurs and retire the patch.
#Improvement: There are frequently pathways available from data collected that are more direct than any taken. An initial area of focus could be improving the return trip using these pathways. One possible method is to calculate all possible return paths (not just those taken), and choose the shortest. Another, more advanced method to reduce retrace time is through the use of distance optimized diagonal pathways within the chosen path.

import serial
import sys
import RPi.GPIO as GPIO
import time

try:   #serial port address to Arduino may end O or 1.
    s = serial.Serial('/dev/ttyACM0',115200)
except:
    s = serial.Serial('/dev/ttyACM1',115200)
    
GPIO.setmode(GPIO.BOARD)  #Set to physical pin numbering scheme.
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_UP) #init goal. Pullup resistor.
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #init wall. Pullup resistor.


s.write(b"\r\n\r\n")
time.sleep(2)   # Wait for GRBL to initialize.
s.flushInput()  # Flush startup text in serial input.
s.write(b'$x\n') #'$x' unlocks GRBL. Motors electrify with subtle audible jolt.
time.sleep(2)   # Wait for GRBL to initialize.
s.flushInput()  # Flush startup text in serial input. Channel ready.

goal=False
i=5  #strt cntr of 11x11, always (+), one cell border outside outer real wall.
j=5
x=0
y=0
log=[]

def matrix():    #build data struct (list of lists, 11x11x7, all zero's)
 
    m=[]         #[north,east,south,west,visits,no-go,unused]
    for w in range(11): 
        m.append([])
        for v in range(11):
            m[w].append([])
            for x in range(7):
                m[w][v].append(0)
    return(m)


def test_box(m,i,j,x,y,goal,log): #test for goal, dtrmine if cell needs wall...
    #...test. If so test cell. In any case update data struct as possible. 

    goal_checked=False
    wall_sum=0
    ip=0  #i-prev used to check prev cell data.
    jp=0
    log.append((x,y))  #add current cell x,y to log.

    try:   #if prev cell was pass-thru allow bot 2sec catchup pre wall test.
        log_len=len(log) #Area for imprvmnt; how can wall test time get rushed?
        if log_len>=2:
            prev_indx=log[((len(log))-2)]
            jp=prev_indx[0]
            ip=prev_indx[1]
            ip=(ip/-42)+5
            jp=(jp/42)+5
            if  m[ip][jp][4]>=2 and m[i][j][4]==0:
                for u in range(20):
                    time.sleep(.1)
                    goal_checked=True
                    if GPIO.input(38)==0:
                        goal=True
    except:
        pass
    
    if m[i][j][4]==0 and goal_checked==False:  #if first visit, test for goal.
        for u in range(20):
            time.sleep(.05)
            if GPIO.input(38)==0:
                goal=True
            
    if m[i][j][4]==0 and goal!=True:   #skip wall test if visited or goal found 
        if m[i-1][j][4]>=1:  #if north nhbr has >1 visit cp its south wall data
            m[i][j][0]=m[i-1][j][2]
            if m[i-1][j][2]==2:   #in leu of test, update wall_sum.
                wall_sum+=1
        else:    #test north
            y+=18
            l = "G0 x"+str(x)+" y"+str(y)  #builds G-Code string for north test
            s.write(l.encode('utf-8') + b'\n') #GCode to GRBL via serial obj 's'
            y-=18
            for u in range(16):   #first visit, check for north wall.
                time.sleep(.05)
                if GPIO.input(40)==0:   
                    m[i][j][0]=2 #0 = not tested, 1 = no wall, 2 = wall.
                else:
                    m[i][j][0]=1
            if m[i][j][0]==2:
                wall_sum+=1  #incr. wall_sum if wall found.
            print(m[i][j][0])
                
        if m[i][j+1][4]>=1:
            m[i][j][1]=m[i][j+1][3]
            if m[i][j+1][3]==2:
                wall_sum+=1
        else:   #test east
            x+=18
            l = "G0 x"+str(x)+" y"+str(y)
            s.write(l.encode('utf-8') + b'\n')
            x-=18
            for u in range(16):
                time.sleep(.05)
                if GPIO.input(40)==0:
                    m[i][j][1]=2
                else:
                    m[i][j][1]=1
            if m[i][j][1]==2:
                wall_sum+=1
            print(m[i][j][1])
                 
        if m[i+1][j][4]>=1:
            m[i][j][2]=m[i+1][j][0]
            if m[i+1][j][0]==2:
                wall_sum+=1
        else:    #test south
            y-=18
            l = "G0 x"+str(x)+" y"+str(y)
            s.write(l.encode('utf-8') + b'\n')
            y+=18
            for u in range(16):
                time.sleep(.05)
                if GPIO.input(40)==0:
                    m[i][j][2]=2
                else:
                    m[i][j][2]=1
            if m[i][j][2]==2:
                wall_sum+=1
            print(m[i][j][2])
                      
        if m[i][j-1][4]>=1:
            m[i][j][3]=m[i][j-1][1]
            if m[i][j-1][1]==2:
                wall_sum+=1
        else:    #test west
            x-=18
            l = "G0 x"+str(x)+" y"+str(y)
            s.write(l.encode('utf-8') + b'\n')
            x+=18
            for u in range(16):
                time.sleep(.05)
                if GPIO.input(40)==0:
                    m[i][j][3]=2
                else:
                    m[i][j][3]=1
            if m[i][j][3]==2:
                wall_sum+=1
            print(m[i][j][3])
           
        l = "G0 x"+str(x)+" y"+str(y)  
        s.write(l.encode('utf-8') + b'\n')
        if wall_sum>=3:
            m[i][j][5]=1 # >=3 walls => no-go
        if wall_sum==2 and m[i-1][j][5]==1 or m[i][j+1][5]==1 or  m[i+1][j][5]==1 or m[i][j-1][5]==1:
            m[i][j][5]==1   #assign no-go if wall_sum==2 and next to a no-go.  
    m[i][j][4]+=1 #add a visit to current cell.
    print(m[i][j])
    return(m,i,j,x,y,goal,log)


def choose_proceed(m,i,j,x,y,goal,log):  #determines next move.

    xp=x #x-prev, used at end to check if no sol.
    yp=y
    visits=[]
    if m[i][j][0]==1:  #builds 'visits' list used to compare open nhbr cells... 
        visits.append(m[i-1][j][4])  #...for number of visits, choose least.
    if m[i][j][1]==1:
        visits.append(m[i][j+1][4])
    if m[i][j][2]==1:
        visits.append(m[i+1][j][4])
    if m[i][j][3]==1:
        visits.append(m[i][j-1][4])
    visits.append(m[i][j][4])
    
    if m[i][j][0]==1 and m[i-1][j][4]<=min(visits) and m[i-1][j][5]==0:
        i-=1  #choose next move by open, <=least visits, not no-go.
        y+=42
    elif m[i][j][1]==1 and m[i][j+1][4]<=min(visits) and m[i][j+1][5]==0:
        j+=1
        x+=42
    elif m[i][j][2]==1 and m[i+1][j][4]<=min(visits) and m[i+1][j][5]==0:
        i+=1
        y-=42
    elif m[i][j][3]==1 and m[i][j-1][4]<=min(visits) and m[i][j-1][5]==0:
        j-=1
        x-=42
    elif m[i][j][0]==1 and m[i][j][5]==1 and m[i-1][j][5]==0:
        i-=1   #if conditions above fail, choose by open, current cell not...
        y+=42  #...no-go, nhbr not no-go.
    elif m[i][j][1]==1 and m[i][j][5]==1 and m[i][j+1][5]==0:
        j+=1
        x+=42
    elif m[i][j][2]==1 and m[i][j][5]==1 and m[i+1][j][5]==0:
        i+=1
        y-=42
    elif m[i][j][3]==1 and m[i][j][5]==1 and m[i][j-1][5]==0:
        j-=1
        x-=42
    l = "G0 x"+str(x)+" y"+str(y) #build Gcode string.
    s.write(l.encode('utf-8') + b'\n')  #Send Gcode.
    if xp==x and yp==y:  #if next cell==prev, no sol; blink red, exit.
        GPIO.setup(23, GPIO.OUT)  #Init red indicator light pin to out, LOW=on.
        for u in range(5):
            GPIO.output(23, GPIO.LOW)
            time.sleep(.4)
            GPIO.output(23, GPIO.HIGH)
            time.sleep(.4)
        s.close()
        GPIO.cleanup()
        exit(0)
    return(m,i,j,x,y,goal,log)


def retrace(m,i,j,log): #retrace to start. Area for improvement; often best...
    #..."known" route is not taken, diagonals could be used (cut out corners).

    indx_1=0  
    while indx_1<len(log):  #step thru log from left to right.
        indx_2=len(log)-1  #compare end of log entry.
        while log[indx_2]!=log[indx_1]:
            indx_2-=1   #step from right to left thru log.
        if indx_1!=indx_2:  #if not same entry..
            for n in range(indx_2-indx_1): 
                log.pop(indx_1)  #delete dup1 and b/w dups but leave last dup. 
        indx_1+=1  #step to next right entry in new log.
   
    log.reverse()  #reverse for retrace.
    for u in range(len(log)):
        pos=log[u]
        x=pos[0]
        y=pos[1]
        l = "G0 x"+str(x)+" y"+str(y)
        s.write(l.encode('utf-8') + b'\n')
    GPIO.setup(13, GPIO.OUT)  #Init green indicator light pin to out, LOW=on.
    for u in range(5):  #retrace complete, blink green, exit.
        GPIO.output(13, GPIO.LOW)
        time.sleep(.4)
        GPIO.output(13, GPIO.HIGH)
        time.sleep(.4)
    s.close()
    GPIO.cleanup()
    exit(0)

                
if __name__ == "__main__":  #all functions called from 'main'.
    m = matrix()   #build 'empty' matrix.
    while goal==False:  #test and decide until goal is found.
        m,i,j,x,y,goal,log = test_box(m,i,j,x,y,goal,log)
        if goal==False:
            m,i,j,x,y,goal,log = choose_proceed(m,i,j,x,y,goal,log)
    retrace(m,i,j,log)  #goal found, return to start.

