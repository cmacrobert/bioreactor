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
        self.current_value = 0

    def set_setpoint(self, new_setpoint):
        print("PIDControl: Changing setpoint to " + str(new_setpoint))
        self.setpoint = new_setpoint
        
    def set_start_value(self, new_start_value):
        print("PIDControl: Changing setpoint to " 
              + str(new_start_value))
        self.start_value = new_start_value

    def set_current_value(self, new_current_value):
        self.current_value = new_current_value
        
    def get_current_value(self):
        return self.current_value    
        
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

    '''def get_target(self): # please get an output value for module to take (eg petlier module for temp)
        #return target
        pass

    def get_current_value(self, module):
            module.get_value()         #get current value of input (eg peltier module / pressure sensor) 
            #and apply to calculation'''

    def reset_vars(self):
        print("PID controller: resetting")
        self.x=[]
        self.y=[]
        plt.clf()
        self.current_value = self.start_value
        self.e_prev = 0
        self.e = 0
        self.time_rate = 0.001
        self.t_prev = 0
        self.t = 1
        self.I = 0
        self.Kp = 0.9
        self.Ki = 0.1
        self.Kd = 0.01
        self.rate = 0.01
        self.reset_scheduled = False

    def update_pid(self):
        if self.reset_scheduled:
            self.reset_vars()
            '''print("PID controller: resetting")
            x=[]
            y=[]
            plt.clf()
            # T = 0
            self.current_value = self.start_value
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
            self.reset_scheduled = False'''
                
        # PID calculations
        self.e = self.setpoint - self.current_value            
        self.P = (self.Kp*self.e)*self.rate
        self.I = (self.I + self.Ki*self.e*(self.t - self.t_prev))*self.rate
        self.D = (self.Kd*(self.e - self.e_prev)/(self.t - self.t_prev))*self.rate                
        self.current_value = self.current_value + self.P + self.I + self.D
        
        """ Update stored data for next iteration"""
        self.e_prev = self.e
        self.t_prev = self.t 
        self.t = (self.t+1)                
                    
        self.x.append(self.t*self.time_rate)
        self.y.append(self.current_value)                    
        self.draw_plot(self.x, self.y)
        self.target_value = self.current_value
        time.sleep(self.time_rate)