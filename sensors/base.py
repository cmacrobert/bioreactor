# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 12:15:19 2021

@author: Calum
"""
#Base definition for a sensor
class sensorBase():

    #Functions
    def __init__(self):    
        self.label = "unnamed sensor"  #name label of sensor
        self.sensorValue = float(0)    #value of sensor
    
    #getSensorValue: returns sensorValue
    def getSensorValue(self):
        return self.sensorValue;
    
    #setSensorValue: sets sensorValue
    def setSensorValue(self, newValue):
        self.sensorValue = newValue;
        
    def sayHello(self):
        print("Hello, I am " + self.label);
        