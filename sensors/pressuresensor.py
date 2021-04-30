# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 20:30:14 2021

@author: mirri
"""

from sensors.base import SensorBase 

class SensorPressure(SensorBase): 
 
    def __init__(self):
        super().__init__()
        self.label = 'pressure sensor'
