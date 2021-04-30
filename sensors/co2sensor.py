# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 13:56:59 2021

@author: mirri
"""

from sensors.base import SensorBase 
class SensorCo2(SensorBase): 
 
    def __init__(self, label): 
        super().__init__() 
        self.label = 'co2 content'   
      #  self.sensor = sensor 
         
    #def get_o2(self): 
   #     if self.reactor.running:
     #       self.set_sensor_value(self.sensor.getco2()) 
     #   return super().get_sensor_value() 
         
     #test code
if __name__ == '__main__': 
    co2 = SensorCo2("co2",0) 
    print(co2.get_sensor_value()) 
    co2.set_sensor_value(5) 
    print(co2.get_sensor_value()) 