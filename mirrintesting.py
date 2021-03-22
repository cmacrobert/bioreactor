# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 18:57:15 2021

@author: mirri
"""

from sensors.base import SensorBase 
class SensorTemp(SensorBase): 
 
    def __init__(self, label, sensor): 
        super().__init__() 
        self.label = 'temperature' 
        self.sensor = sensor
         
    def get_temperature(self): 
        self.set_sensor_value(self.sensor.gettemperature()) 
        return super().get_sensor_value() 
         
if __name__ == '__main__': 
    temperature = SensorTemp("temperature",0) 
    print(temperature.get_sensor_value()) 
    temperature.set_sensor_value(1000) 
    print(temperature.get_sensor_value()) 