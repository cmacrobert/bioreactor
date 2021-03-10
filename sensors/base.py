# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 12:15:19 2021

@author: Calum
"""

class SensorBase():

    def __init__(self):    
        self.label = "unnamed sensor"
        self.sensor_value = float(0)
    
    def get_sensor_value(self):
        return self.sensor_value;
    
    def set_sensor_value(self, new_value):
        self.sensor_value = new_value;
        
    def say_hello(self):
        print("Hello, I am " + self.label);
        
    def sayValue(self):
        print(self.value)
        
