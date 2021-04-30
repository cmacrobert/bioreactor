# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 13:56:59 2021

@author: mirri
"""

from sensors.base import SensorBase 

class SensorCo2(SensorBase): 
 
    def __init__(self): 
        super().__init__() 
        self.label = 'co2 content'