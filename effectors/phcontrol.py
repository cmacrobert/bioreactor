# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 19:03:39 2021

@author: Nat
"""

from effectors.base import EffectorBase

class PHControl(EffectorBase):
   
    def __init__(self):         
        EffectorBase.__init__(self, "pHController")                                             
        self.initial_upper_range = 14
        self.initial_lower_range = 0
        self.title = "pH"
        self.y_axis_label = "pH"
        self.setpoint = 7 

    def start(self):
        print("PHControl: Starting")
        self.reset_scheduled = True        
        self.running = True
        
        while self.running:
            self.update_pid()
        print("PHControl: Exited loop")