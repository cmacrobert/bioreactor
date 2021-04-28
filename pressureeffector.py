# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 16:42:12 2021

@author: mirri
"""

from effectors.base import EffectorBase


class EffectorPressure(EffectorBase):  #inherits class
    
    def __init__(self):     
        EffectorBase.__init__(self, "Pressure Sensor")
        
    def set_target_pressure(self, pressure):    # receive target pressure
        self.set_setpoint(pressure)
    
 
    def start(self):
        print("Pressure Sensor: Starting")
        self.reset_scheduled = True        
        self.running = True
        
        while self.running:            
            self.update_pid()
        print("Pressure Sensor: Exited loop")