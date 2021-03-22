# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 12:15:19 2021

@author: Calum
"""

class SensorBase(): #establishes class called SensorBase

    def __init__(self):    # constructor, called when an object is created from the class
                            # and it allows the class to initialize the attributes of a class
        self.label = "unnamed sensor"   # helps for debugging, we shouldn't need to refer to its name
                                         
        self.sensor_value = float(0)    # sets default effector to have a 
                                        # value, and for it to be 0 initially
    
    def get_sensor_value(self):     # defines function which allows a new sensor value to be set
        return self.sensor_value;    # allow "new_value" to change the value
                                        # these funtions can be used in inheriting sensor modules
    
    def set_sensor_value(self, new_value):  # defines function that allows a new sensor value to be set
        self.sensor_value = new_value;      # allow "new_value" to change the value
        
    def say_hello(self):                    # defines a new function
        print("Hello, I am " + self.label); # never used, but can print its name in the console
        