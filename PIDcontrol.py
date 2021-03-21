# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:37:10 2021

@author: Stefan Olsson
"""

import time
import matplotlib.pyplot as plt

xMax = 200
x=[]
y=[]
setPoint = 10
print('Reactor Started')
T = 0

def PID(Kp, Ki, Kd, SP, MV_bar):

    val = MV_bar
    e_prev = 0
    e = 0
    t_prev = 0
    t = 1
    I = 0
    x=np.ones(xMax)
    y=np.ones(xMax)
    
    prev_time = time.time()
    curr_time = 0
    
    while True:
        # PID calculations
        e = SP - val
        
        P = Kp*e
        I = I + Ki*e*(t - t_prev)
        D = Kd*(e - e_prev)/(t - t_prev)
        
        val = MV_bar + P + I + D
         
        # update stored data for next iteration
        e_prev = e
        t_prev = t
        
        t = t+1
                
        curr_time = time.time()
        if curr_time >= prev_time+2:
            print("PID thread - " + str(val))
            prev_time = curr_time
        
        x.append(t)
        y.append(val)
        
        plt.plot(x,y)
        plt.show()
        plt.clf()
        #print(val)
        
        time.sleep(0.25)
        """
        command = input('>')
        if command == "set T SP":
            setPoint = input('set Temperature SetPoint >')
        else:
            pass
        
        #if t==xMax:
           # plt.plot(x,y)
           # exit()
        """         
PID(0.05,0.05,0.05,setPoint,T)
        
    