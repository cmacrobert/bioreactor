# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 10:43:19 2021

@author: Stefan Olsson
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:37:10 2021

@author: Stefan Olsson
"""

import time
import matplotlib.pyplot as plt
import random

x=[]
y=[]
myplot = plt.plot(x,y)
print('Reactor Started')
T = 0
val = 0
e_prev = 0
e = 0
time_rate = 0.001
t_prev = 0
t = 1
I = 0
Kp = 0.9
Ki = 0.1
Kd = 0.01
SP = 37
rate = 0.01

while True:
    # PID calculations
    e = SP - val
    
    '''if abs(e) < 1:
        SP = random.choice([20,40])
        P = I = D = 0'''
    
    x.append(t*time_rate)
    y.append(val)
    
    plt.plot(x,y)
    plt.hlines(SP, 0, 5, 'C1', 'dashed')
    plt.xlim(0,1)
    plt.ylim(0,55)
    plt.show()
    #print(val)
        
    P = (Kp*e)*rate
    I = (I + Ki*e*(t - t_prev))*rate
    D = (Kd*(e - e_prev)/(t - t_prev))*rate
        
    val = val + P + I + D
         
    # update stored data for next iteration
    e_prev = e
    t_prev = t 
    t = (t+1)
        
    time.sleep(time_rate)

        
                  
        
    