# -*- coding: utf-8 -*-
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