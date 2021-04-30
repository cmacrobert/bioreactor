# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 13:15:12 2021

@author: mirri
"""

class EffectorCo2(EffectorBase):  #inherits class 
     
    def __init__(self):      
        EffectorBase.__init__(self, "co2 Sensor") 
         
    def set_target_co2(self, co2):    # receive target CO2 value 
        self.set_setpoint(co2) 
     
  
    def start(self): 
        print("co2 Sensor: Starting") 
        self.reset_scheduled = True         
        self.running = True 
         
        while self.running:             
            self.update_pid() 
        print("co2 Sensor: Exited loop")