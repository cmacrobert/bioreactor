# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 13:15:50 2021

@author: Calum
"""

from sensors.base import sensorBase

class sensorTemperature(sensorBase):
    
    #Functions
    def __init__(self, label):
        self.label = label