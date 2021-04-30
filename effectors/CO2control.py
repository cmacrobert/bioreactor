# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 13:15:12 2021

@author: mirri
"""

from effectors.base import EffectorBase
class Co2Control(EffectorBase):  #inherits class 
     
    def __init__(self):      
        EffectorBase.__init__(self, "co2 Sensor") 
        self.initial_upper_range = 10
        self.initial_lower_range = 0
        self.title = "CO2 level"
        self.y_axis_label = "CO2 (%)"
        self.setpoint = 5
         
   # def set_target_co2(self, co2):    # receive target CO2 value 
    #    self.set_setpoint(co2) 
     
  
    def start(self): 
        print("co2 Sensor: Starting") 
        self.reset_scheduled = True         
        self.running = True 
         
        while self.running:             
            self.update_pid() 
        print("co2 Sensor: Exited loop")