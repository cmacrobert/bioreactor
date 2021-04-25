# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 00:09:15 2021

@author: Nat
"""
#i want to it run an instance of the PID, with a gettable funtion output, 
#this is the funtion in the pid_control

#   def get_target(self, value):
#        self.get_target(value) = 25                #using this value as a placeholder

#in the case that this is passed to the simulated reactor it is converted to a
#temperature. If not,the value is taken by the microcontroller file 

#from effectors.base import EffectorBase        #imported the thermocouple information 
#from sensors.thermocouple import thermocouple  #from folder.file import class
from pid_control import PIDControl
from reactor import reactor
import microcontroller
from base import EffectorBase
from sensors.thermocouple import thermocouple


class heatercooler(EffectorBase, PIDControl):  #establishes class  #inherites from these classes 
                   #REMOVE EFFECTOR BASE IF YOU DELETE THE CLASS
    def __init__(self, reactor):    
            
        # EffectorBase.__init__(self)                 # DOES NOTHING!
        PIDControl.__init__(self)
        # self.label = "heaterPID"
        self.reactor = reactor                   # link to reactor
        self.thermocouple = thermocouple(self.reactor) #link to thermocouple (link thermocouple to reactor)
                                                
        
    def set_target_temp(self, temp):                  # Get user's target temp
        self.set_setpoint(temp)
    
    def get_current_temp(self,temp):
        self.get_current_value(self.thermocouple)
        
   
    def pass_the_value(self):
    if reactor.running():
    #convert the value to a temperature by timesing it by 0.33 for example
        self.reactor.set_peltier_temp(self.target_value * 0.33)
    #then pass it to the reactor which GETS time step forward? 
    
    else:
    #pass the value to the microcontroller to be converted inside it with C code.
        pass

# #test code for using functions defined in the parent class
# if __name__ == '__main__':
#     heatercooler = heatercooler(reactor()) #passes reactor to the heatercooler, modules can now interact
#     print(heatercooler.thermocouple.get_temperature()) #refers to  self.thermocouple = thermocouple(reactor)
 