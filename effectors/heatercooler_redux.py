# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 00:09:15 2021

@author: Nat
"""

#example of the Peltier Module
#https://www.cuidevices.com/product/resource/cp18-m.pdf
#i want to it run an instance of the PID, with a gettable funtion output, 
#this is the funtion in the pid_control

#   def get_target(self, value):

#in the case that this is passed to the simulated reactor it is converted to a
#temperature. If not,the value is taken by the microcontroller file 

#from reactor import reactor
#import microcontroller
from effectors.base import EffectorBase
from sensors.thermocouple import thermocouple


class heatercooler(EffectorBase):  #establishes class  #inherits from these classes 
    
    def __init__(self):#, reactor):       
        EffectorBase.__init__(self, "HeaterCooler")
        # self.label = "heaterPID"
        #self.reactor = reactor                           # link to reactor
        #self.thermocouple = thermocouple(self.reactor) #link to thermocouple (link thermocouple to reactor)
        
    def set_target_temp(self, temp):                  # Get user's target temp
        self.set_setpoint(temp)
    
    def get_current_temp(self,temp):
        self.get_current_value(self.thermocouple)
        
   
    def pass_the_value(self):
        if reactor.running():
    #value should already be a temperature, but need to remember that it has a limited range, so calibration equation might be needed
            self.reactor.set_peltier_temp(self.target_value * 0.4)
    #then pass it to the reactor
    
        else:
    #pass the value to the microcontroller to be converted inside it with C code.
            pass

# #test code for using functions defined in the parent class
# if __name__ == '__main__':
#     heatercooler = heatercooler(reactor()) #passes reactor to the heatercooler, modules can now interact
#     print(heatercooler.thermocouple.get_temperature()) #refers to  self.thermocouple = thermocouple(reactor)
 
    def start(self):
        print("HeaterCooler: Starting")
        self.reset_scheduled = True        
        self.running = True
        
        while self.running:            
            self.update_pid()
        print("HeaterCooler: Exited loop")