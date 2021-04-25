# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:37:10 2021

@author: Stefan Olsson
"""

# Changed temperature to "value to make this PID more generic so it can be inherited by other PIDs"

import time
import matplotlib.pyplot as plt
import random

class PIDControl():    

    def __init__ (self):
        print("PIDControl: Initialising")
        self.setpoint = 37
        self.running = False
        self.start_value = 0
        self.target_value = 0

    def set_setpoint(self, new_setpoint):
        print("PIDControl: Changing setpoint to " + str(new_setpoint))
        self.setpoint = new_setpoint
        
    def set_start_value(self, new_start_value):
        print("PIDControl: Changing setpoint to " 
              + str(new_start_value))
        self.start_value = new_start_value
        
    def get_running(self):
        return self.running

    def reset(self):    
        print("PIDControl: Restarting")    
        self.reset_scheduled = True

    def draw_plot(self, x, y):
        #TODO: do plotting in separate file/thread with own timing?
            #currently the draw call is massively affecting the PID speed
        plt.close()
        plt.plot(x,y)
        plt.hlines(self.setpoint, 0, 5, 'C1', 'dashed')
        plt.xlim(0,1)
        plt.ylim(0,55)
        plt.show()   

    def get_target(self): # please get an output value for module to take (eg petlier module for temp)
        #return target
        pass

    def get_current_value(self, module):
            module.get_value()         #get current value of input (eg peltier module / pressure sensor) 
            #and apply to calculation

    def start(self):
        """
        Main loop for PID controller
        Continually updates PID, calling plot function each iteration
        """
        print("PIDControl: Starting")
        x=[]
        y=[]
        myplot = plt.plot(x,y)
        
        self.reset_scheduled = True        
        self.running = True
        
        while self.running:
            if self.reset_scheduled:
                print("PID controller: resetting")
                x=[]
                y=[]
                plt.clf()
                # T = 0
                val = self.start_value
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
            P = (Kp*e)*rate
            I = (I + Ki*e*(t - t_prev))*rate
            D = (Kd*(e - e_prev)/(t - t_prev))*rate                
            val = val + P + I + D
                 
            """ Update stored data for next iteration"""
            e_prev = e
            t_prev = t 
            t = (t+1)                
                        
            x.append(t*time_rate)
            y.append(val)                    
            self.draw_plot(x, y)
            self.target_value = val
            time.sleep(time_rate)
        print("PID controller: Exited loop")
    
    def stop(self):
        print("PID controller: Stopping thread")
        self.running = False