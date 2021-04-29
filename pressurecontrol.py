# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 16:57:53 2021

@author: mirri
"""

from pid_control import PIDControl
from reactor import reactor
import microcontroller
from base import EffectorBase
from sensors.pressure import pressure

class phcontrol(EffectorBase, PIDControl):  #establishes class  #inherits from these classes 
                   
    def __init__(self, reactor):    
            
        PIDControl.__init__(self)
        
        self.reactor = reactor                           # link to reactor
        self.pressuresensor = pressuresenssor(self.reactor) #link to pressure to reactor)
                                                
        
    def set_target_pressure(self, pressure):                  # receive target pressure
        self.set_setpoint(pressure)
    
    def get_current_pressure(self,pressure):
        self.get_current_value(self.pressure)
        
   
    def pass_the_value(self):
        if reactor.running():
            self.reactor.set_pressure(self.target_value)
    #pass value to reactor
    
        else:
            pass