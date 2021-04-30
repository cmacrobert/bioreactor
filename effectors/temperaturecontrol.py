# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 16:37:04 2021

@author: User
"""

#example of the Peltier Module
#https://www.cuidevices.com/product/resource/cp18-m.pdf

from effectors.base import EffectorBase

class TemperatureControl(EffectorBase):  
    
    def __init__(self):      
        EffectorBase.__init__(self, "TemperatureControl")
        self.initial_upper_range = 55
        self.initial_lower_range = 0
        self.title = "Temperature"
        self.y_axis_label = "Temperature (\xb0C)"
        self.setpoint = 37

    def start(self):
        print("TemperatureControl: Starting")
        self.reset_scheduled = True        
        self.running = True
        
        while self.running:
            self.update_pid()
        print("TemperatureControl: Exited loop")