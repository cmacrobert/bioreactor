# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:37:10 2021

@author: Stefan Olsson
"""

import time
import matplotlib.pyplot as plt
import numpy as np

xMax = 200

def PID(Kp, Ki, Kd, SP, MV_bar=0):
    # initialize stored data
    val = MV_bar
    e_prev = 0
    e = 0
    t_prev = 0
    t = 1
    I = 0
    
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
        
        x[t] = t
        y[t] = val
        
        t = t+1
        
        print(val)
        
        if t==xMax:
            plt.plot(x,y)
            exit()
        
x=np.ones(xMax)
y=np.ones(xMax)
PID(0.05,0.05,0.05,37)