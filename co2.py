# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 13:56:59 2021

@author: mirri
"""

from sensors.base import SensorBase 
class SensorCo2(SensorBase): 
 
    def __init__(self, label, sensor): 
        super().__init__() 
        self.label = 'CO2 content'   
        self.sensor = sensor 
         
    def get_co2(self): 
        self.set_sensor_value(self.sensor.getco2()) 
        return super().get_sensor_value() 
         
if __name__ == '__main__': 
    co2 = SensorCo2("CO2",0) 
    print(co2.get_sensor_value()) 
    co2.set_sensor_value(5) 
    print(co2.get_sensor_value()) 