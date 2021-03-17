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

xMax = 200
x=[]
y=[]
print('Reactor Started')
T = 0
MV_bar = 0
val = MV_bar
e_prev = 0
e = 0
t_prev = 0
t = 1
I = 0
Kp = 0.05
Ki = 0.05
Kd = 0.05
SP = 37
counter = 0
    
while True:
    # PID calculations
    e = SP - val
    
    if abs(e) < 1:
        val = MV_bar = random.choice([10,20,40,50])
        P = I = D = 0
    
    x.append(t)
    y.append(val)
        
    plt.cla()
    plt.plot(x,y)
    plt.show()
    #print(val)
        
    P = Kp*e
    I = I + Ki*e*(t - t_prev)
    D = Kd*(e - e_prev)/(t - t_prev)
        
    val = MV_bar + P + I + D
         
    # update stored data for next iteration
    e_prev = e
    t_prev = t    
    t = t+1
        
    time.sleep(0.25)
    counter += 1
    print(counter)
        
    #if t==xMax:
        # plt.plot(x,y)
        # exit()
        
                  
        
    