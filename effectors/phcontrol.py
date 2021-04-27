# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 19:03:39 2021

@author: Nat
"""

#pH Control
#uses an instance of the PID to control pH


from pid_control import PIDControl
from reactor import reactor
import microcontroller
from base import EffectorBase
from sensors.phsensor import phsensor

class phcontrol(EffectorBase, PIDControl):  #establishes class  #inherits from these classes 
                   #REMOVE EFFECTOR BASE IF YOU DELETE THE CLASS
    def __init__(self, reactor):    
            
        # EffectorBase.__init__(self)                 # DOES NOTHING!
        PIDControl.__init__(self)
        # self.label = "heaterPID"
        self.reactor = reactor                           # link to reactor
        self.phsensor = phsenssor(self.reactor) #link to thermocouple (link thermocouple to reactor)
                                                
        
    def set_target_temp(self, ph):                  # Get user's target temp
        self.set_setpoint(ph)
    
    def get_current_temp(self,ph):
        self.get_current_value(self.phsensor)
        
   
    def pass_the_value(self):
    if reactor.running():
    #value should already be in ph, but need to remember that it is limited, so calibration equation might be needed
        self.reactor.set_ph_input(self.target_value)
    #then pass it to the reactor
    
    else:
    #pass the value to the microcontroller to be converted inside it with C code.
        pass

# #test code for using functions defined in the parent class
# if __name__ == '__main__':
#     phcontrol = phcontrol(reactor()) #passes reactor to the ph pump, modules can now interact
#     print(phcontrol.phsensor.get_ph()) #refers to  self.phsensor = phsensor(reactor)

#now I need to pass the ph sensor into the reactor
 