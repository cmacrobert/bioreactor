# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 13:15:50 2021

@author: Calum
"""

from sensors.base import SensorBase

class SensorTemperature(SensorBase):
    
    #Functions
    def __init__(self, label, value):
        self.label = label
        self.value = value
    

        

