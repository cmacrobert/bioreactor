# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 17:53:02 2021

@author: Nat
"""

from sensors.base import SensorBase #imports functions from sensor class
class thermocouple(SensorBase):     #establishes class thermocouple which inherits from sensor base

    def __init__(self, reactor):    #object is created from the class, initialize the attributes of a class.
        super().__init__()          #improved syntax, it means super(ChildB, self).__init__() 
                                    #establishes architecture which allows inheritance from multiple classes
        self.label = 'thermocouple' #this is the name of the object
                                    #needs to expect to be attached to a reactor    
        self.reactor = reactor      #attaches to reactor
        
    def get_value(self):      #defines function, inherits from self(itself, the thermocouple?)
        if reactor.running:
            self.set_sensor_value(self.reactor.gettemperature()) #gets temperature from the reactor sets it as a value
        # else:
        #     self.set_sensor_value = microcontroller.get_temperature()
        return get_sensor_value()   #returns the value gotten using get_sensor_value
                                            #allows that to be a value that future modules can get
    
#test code for using fucntions defined in the parent class, not used by other programs
if __name__ == '__main__':
    thermocouple = thermocouple()           #sets global variable thermocouple sets equal to an instance of the class thermocouple 
                                            #brackets implicitly pass self, (only when used on a class)
    print(thermocouple.get_sensor_value())  #in the test code, prints the sensor value, not used by other modules
    #thermocouple.set_sensor_value(1000)     #example. sets value to 1000
    #print(thermocouple.get_sensor_value())  
    

