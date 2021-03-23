# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:37:10 2021

@author: Stefan Olsson
"""

import time
import matplotlib.pyplot as plt
import random

class PIDControl():

    def __init__ (self):
        print("PIDControl - Initialising")
        self.setpoint = 37
        self.running = False

    def set_setpoint(self, new_setpoint):
        print("PIDControl - changing setpoint to " + str(new_setpoint))
        self.setpoint = new_setpoint

    def start_thread(self):
        print("Starting PID")    
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
        rate = 0.01
        
        self.running = True
        
        while self.running == True:
            # PID calculations
            e = self.setpoint - val
                        
            x.append(t*time_rate)
            y.append(val)
            
            plt.close()
            plt.plot(x,y)
            plt.hlines(self.setpoint, 0, 5, 'C1', 'dashed')
            plt.xlim(0,1)
            plt.ylim(0,55)
            plt.show()                
            
            P = (Kp*e)*rate
            I = (I + Ki*e*(t - t_prev))*rate
            D = (Kd*(e - e_prev)/(t - t_prev))*rate
                
            val = val + P + I + D
                 
            # update stored data for next iteration
            e_prev = e
            t_prev = t 
            t = (t+1)
                
            time.sleep(time_rate)
        print("PID controller - Exited loop")
    
    def stop_thread(self):
        print("PID controller - Stopping thread")
        self.running = False