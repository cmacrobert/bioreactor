# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 10:37:10 2021

@author: Calum
"""

class EffectorBase():

    def __init__(self):    
        self.label = "unnamed effector"
        self.effector_value = float(0)
        
    def set_effector_value(self, new_value):
        self.effector_value = new_value;
        
    def say_hello(self):
        print("Hello, I am " + self.label);
        