# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 16:37:04 2021

@author: User
"""

#example of the Peltier Module
#https://www.cuidevices.com/product/resource/cp18-m.pdf


from effectors.base import EffectorBase

class heatercooler(EffectorBase):  
    
    def __init__(self):      
        EffectorBase.__init__(self, "HeaterCooler")
         
    def set_target_temp(self, temp):  # Get user's target temp
        self.set_setpoint(temp)
        
    #please check!
    #def peltier_value(self):
    #    self.get_current_value() #using the function in pid_control. 
    # equivalent to heatercooler.get_current_value

    def start(self):
        print("HeaterCooler: Starting")
        self.reset_scheduled = True        
        self.running = True
        
        while self.running:            
            self.update_pid()
        print("HeaterCooler: Exited loop")
 