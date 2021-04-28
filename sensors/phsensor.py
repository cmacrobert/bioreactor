# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 16:57:34 2021

@author: Nat
"""

#this is an example of the pH sensor 
#https://www.fieldkit.org/wp-content/uploads/2020/11/SpecsLabElectrodes-Plastic-pH.pdf


from sensors.base import SensorBase #imports functions from sensor class
class phsensor(SensorBase):     #establishes class thermocouple which inherits from sensor base

    def __init__(self):    #object is created from the class, initialize the attributes of a class.
        super().__init__()          #improved syntax, it means super(ChildB, self).__init__() 
        self.label = 'phsensor'     #this is the name of the object
 


#I need to set up ph simulation in the reactor 
#I need to make a PID control file for pH. 
