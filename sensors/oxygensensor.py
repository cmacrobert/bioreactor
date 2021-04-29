# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 00:30:10 2021

@author: User
"""
#not even implemented at all yet

from sensors.base import SensorBase #imports functions from sensor class
class Oxysensor(SensorBase):     #establishes class thermocouple which inherits from sensor base

    def __init__(self):    #object is created from the class, initialize the attributes of a class.
        super().__init__()          #improved syntax, it means super(ChildB, self).__init__() 
        self.label = 'Oxysensor'    #this is the name of the object
 


#I need to set up O2 simulation in the reactor 
#I need to make a PID control file for O2. 
