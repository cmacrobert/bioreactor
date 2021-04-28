# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 17:53:02 2021

@author: Nat
"""

from sensors.base import SensorBase #imports functions from sensor class
class thermocouple(SensorBase):     #establishes class thermocouple which inherits from sensor base

    def __init__(self):    #object is created from the class, initialize the attributes of a class.
        super().__init__()          #improved syntax, it means super(ChildB, self).__init__() 
        self.label = 'thermocouple' #this is the name of the object
         
   