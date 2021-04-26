# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 10:37:10 2021

@author: Calum
"""

from pid_control import PIDControl

class EffectorBase(PIDControl):

    def __init__(self, name):        
        PIDControl.__init__(self)
        self.name = name
            
    def get_running(self):
        return self.running
    
    def stop(self):
        print(self.name + ": Stopping thread")
        self.running = False