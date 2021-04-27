# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 20:30:14 2021

@author: mirri
"""

from sensors.base import SensorBase 
class SensorPressure(SensorBase): 
 
    def __init__(self, label, sensor): 
        super().__init__() 
        self.label = 'pressure'   
        self.sensor = sensor 
         
    def get_pressure(self): 
        self.set_sensor_value(self.sensor.getpressure()) 
        return super().get_sensor_value() 
         
if __name__ == '__main__': 
    pressure = SensorPressure("pressure",0) 
    print(pressure.get_sensor_value()) 
    pressure.set_sensor_value(5) 
    print(pressure.get_sensor_value()) 