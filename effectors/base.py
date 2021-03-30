# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 10:37:10 2021

@author: Calum
"""

class EffectorBase(): #establishes class called EffectorBase

    def __init__(self):    # constructor, called when an object is created from the class
                            # and it allow the class to initialize the attributes of a class.
        self.label = "unnamed effector" # helps for debugging, we shoudn't
                                        # need to refer to its name
        self.effector_value = float(0)  # sets default effector to have a 
                                        # value, and for it to be 0 initially
        
    def set_effector_value(self, new_value): # allows a new effector value to be set
        self.effector_value = new_value;     # allow "new_value" to change the value
        
    def say_hello(self): # defines a new function
        print("Hello, I am " + self.label);  # never used
        