# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:37:10 2021

@author: Stefan Olsson
"""

import time

class PIDControl():    

    def __init__ (self):
        print("PIDControl: Initialising")
        self.running = False
        self.start_value = 0
        self.target_value = 0
        self.current_value = 0
        self.x = 0
        self.y = 0
        self.initial_upper_range = 55
        self.initial_lower_range = 0
        self.initial_upper_domain = 50
        self.initial_lower_domain = 0
        self.domain_diff = self.initial_upper_domain-self.initial_lower_domain

    def get_setpoint(self):
        return self.setpoint

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
        self.time_rate = 0.1
        self.t_prev = 0
        self.t = 1
        self.t_counter = 0
        self.upper_range = self.initial_upper_range
        self.lower_range = self.initial_lower_range
        self.upper_domain = self.initial_upper_domain
        self.lower_domain = self.initial_lower_domain
        self.domain_diff = self.upper_domain-self.lower_domain
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
        
        if self.t_counter >= (self.domain_diff/self.time_rate):
            self.lower_domain = self.upper_domain
            self.upper_domain += self.domain_diff
            self.t_counter = 0
                    
        self.x.append(self.t*self.time_rate)
        self.y.append(self.current_value)
        self.target_value = self.current_value
        time.sleep(self.time_rate)