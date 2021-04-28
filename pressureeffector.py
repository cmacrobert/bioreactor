# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 16:42:12 2021

@author: mirri
"""

from effectors.base import EffectorBase
from sensors.pressuresensor import pressure


class SensorPressure(EffectorBase):  #inherits class
    
    def __init__(self):     
        EffectorBase.__init__(self, "Pressure Sensor")
        
    def set_target_pressure(self, pressure):    # receive target pressure
        self.set_setpoint(pressure)
    
    def get_current_pressure(self,pressure):
        self.get_current_value(self.pressure)
        
   
    def pass_the_value(self):
        if reactor.running():
   
            self.reactor.set_pressure(self.target_value * 0.4)
    #then pressure value pass it to the reactor
    
        else:
    #pass the value to the microcontroller
            pass

# #test code for using functions defined in the parent class
 
    def start(self):
        print("Pressure Sensor: Starting")
        self.reset_scheduled = True        
        self.running = True
        
        while self.running:            
            self.update_pid()
        print("Pressure Sensor: Exited loop")