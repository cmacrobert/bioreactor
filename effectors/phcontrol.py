# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 19:03:39 2021

@author: Nat
"""

#pH Control
#uses an instance of the PID to control pH


from effectors.base import EffectorBase
from sensors.phsensor import phsensor

class phcontrol(EffectorBase):
   
    def __init__(self):         
        EffectorBase.__init__(self, "pHController")                                             
        self.intUpperDomain = 14
        self.intLowerDomain = 0
        self.reset_vars()
        self.title = "pH"
        self.y_axis_label = "pH"
        self.setpoint = 7        
        
    def set_target_ph(self, ph):                  # Get user's target temp
        self.set_setpoint(ph)    

    def start(self):
        print("HeaterCooler: Starting")
        self.reset_scheduled = True        
        self.running = True
        
        while self.running:
            self.update_pid()
        print("HeaterCooler: Exited loop")
 
    
#now I need to pass the ph sensor into the reactor
 