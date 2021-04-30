# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 16:42:12 2021

@author: mirri
"""

from effectors.base import EffectorBase


class PressureControl(EffectorBase):  #inherits class
    
    def __init__(self):     
        EffectorBase.__init__(self, "Pressure Sensor")
        self.initial_upper_range = 10
        self.initial_lower_range = 0
        self.title = "Pressure"
        self.y_axis_label = "Pressure (bars)"
        self.setpoint = 4.5
        
    #def set_target_pressure(self, pressure):    # receive target pressure
     #   self.set_setpoint(pressure)
    
 
    def start(self):
        print("Pressure Sensor: Starting")
        self.reset_scheduled = True        
        self.running = True
        
        while self.running:            
            self.update_pid()
        print("Pressure Sensor: Exited loop")