# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 00:09:15 2021

@author: Nat
"""

#this module needs to pass the temperature target to the simulated reactor 
#in the case that the simulated reactor is running
#if the simulated reactor is not running, it needs to instead communicate
#with a real live microcontroller. work on procols for this can be found 
#in the microcontroller file
#the peltier module actually is redundant, as in the simulation the PID can 
#be fed directly into the reacotr as a temperature. 

#from effectors.base import heatercooler DO NOT NEED TO DO THIS need to attach peltier to reactor and heatercooler

class peltiermodule(): #inherited from 0 classes
    def __init__(self, reactor,): #reactor is passed in
        self.reactor = reactor # so it knows what reactor it is attached to
        #does not need to know which thermocouple it is attached to
        self.voltage = 0   #default should be 0
        #self.temperature = reactor.gettemperature() #default temp of peltier is the same as that of the reactor
                                                    #its a physical property.
        self.heatercooler = heatercooler                                            
                                                    
    def setvoltage(self, voltage): 
        self.voltage = voltage
        
    def time_step_forward():    #needs to apply to every step, each cycle
        pass                    #its not finished!
    
    #needs to convert the PID temp target to 
    #a useable voltage within the module

