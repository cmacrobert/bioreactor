# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 20:30:14 2021

@author: mirri
"""

from sensors.base import SensorBase 
class SensorPressure(SensorBase): 
 
    def __init__(self, label):
        super().__init__()   
       # self.reactor = reactor   
        self.label = 'pressure sensor'
                
   # def get_pressure(self): 
    #    if self.reactor.running:
     #       self.set_sensor_value(self.sensor.getpressure()) 
      #  return super().get_sensor_value() 
       
      #test code
if __name__ == '__main__': 
    pressure = SensorPressure("pressure",1) 
    print(pressure.get_sensor_value()) 
    pressure.set_sensor_value(4.5) 
    print(pressure.get_sensor_value()) 