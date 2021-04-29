# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 19:03:39 2021

@author: Nat
"""

#pH Control
#uses an instance of the PID to control pH


from effectors.base import EffectorBase

class phcontrol(EffectorBase):
   
    def __init__(self):         
        EffectorBase.__init__(self, "pHController")                                             
        
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
 