# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 20:19:10 2021

@author: mirri
"""

from effectors.base import EffectorBase


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