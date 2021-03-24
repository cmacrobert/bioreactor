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
        self.start_temperature = 0

    def set_setpoint(self, new_setpoint):
        print("PIDControl - Changing setpoint to " + str(new_setpoint))
        self.setpoint = new_setpoint
        
    def set_start_temperature(self, new_start_temperature):
        print("PIDControl - Changing setpoint to " + str(new_start_temperature))
        self.start_temperature = new_start_temperature

    def reset(self):    
        print("PIDControl - Restarting")    
        self.reset_scheduled = True

    def draw_plot(self, x, y):
        plt.close()
        plt.plot(x,y)
        plt.hlines(self.setpoint, 0, 5, 'C1', 'dashed')
        plt.xlim(0,1)
        plt.ylim(0,55)
        plt.show()   

    def start_thread(self):
        
        print("PIDControl - Starting")
        x=[]
        y=[]
        myplot = plt.plot(x,y)
        
        self.reset_scheduled = True        
        self.running = True
        
        while self.running == True:
            if self.reset_scheduled == True:
                print("PID controller - resetting")
                x=[]
                y=[]
                plt.clf()
                T = 0
                val = self.start_temperature
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
                self.reset_scheduled = False
            
            # PID calculations
            e = self.setpoint - val
                        
            x.append(t*time_rate)
            y.append(val)
                    
            self.draw_plot(x, y)
            
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