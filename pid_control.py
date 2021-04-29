# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:37:10 2021

@author: Stefan Olsson
"""

import time

class PIDControl():    

    def __init__ (self):
        print("PIDControl: Initialising")
        self.setpoint = 37
        self.running = False
        self.start_value = 0
        self.target_value = 0
        self.current_value = 0
        self.x = 0
        self.y = 0
        self.intUpperRange = 1
        self.intLowerRange = 0
        self.intUpperDomain = 55
        self.intLowerDomain = 0
        self.rangeDiff = self.intUpperRange-self.intLowerRange

    def get_setpoint(self):
        return self.setpoint

    def set_setpoint(self, new_setpoint):
        print("PIDControl: Changing setpoint to " + str(new_setpoint))
        self.setpoint = new_setpoint
        
    def set_start_value(self, new_start_value):
        print("PIDControl: Changing setpoint to " 
              + str(new_start_value))
        self.start_value = new_start_value

    def reset(self):    
        print("PIDControl: Restarting")    
        self.reset_scheduled = True

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def reset_vars(self):
        print("PID controller: resetting")
        self.x=[]
        self.y=[]
        self.current_value = self.start_value
        self.e_prev = 0
        self.e = 0
        self.time_rate = 0.001
        self.t_prev = 0
        self.t = 1
        self.t_counter = 0
        self.upperRange = self.intUpperRange
        self.lowerRange = self.intLowerRange
        self.upperDomain = self.intUpperDomain
        self.lowerDomain = self.intLowerDomain
        self.rangeDiff = self.upperRange-self.lowerRange
        self.I = 0
        self.Kp = 0.9
        self.Ki = 0.1
        self.Kd = 0.01
        self.rate = 0.01
        self.reset_scheduled = False

    def update_pid(self):
        if self.reset_scheduled:
            self.reset_vars()
                
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
        self.t_counter = (self.t_counter+1)          
                    
        self.x.append(self.t*self.time_rate)
        self.y.append(self.current_value)
        self.target_value = self.current_value
        time.sleep(self.time_rate)