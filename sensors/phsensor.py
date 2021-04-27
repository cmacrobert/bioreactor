# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 16:57:34 2021

@author: Nat
"""

#this is an example of the pH sensor 
#https://www.fieldkit.org/wp-content/uploads/2020/11/SpecsLabElectrodes-Plastic-pH.pdf


from sensors.base import SensorBase #imports functions from sensor class
class phsensor(SensorBase):     #establishes class thermocouple which inherits from sensor base

    def __init__(self, reactor):    #object is created from the class, initialize the attributes of a class.
        super().__init__()          #improved syntax, it means super(ChildB, self).__init__() 
                                    #establishes architecture which allows inheritance from multiple classes
        self.label = 'phsensor'     #this is the name of the object
                                    #needs to expect to be attached to a reactor    
        self.reactor = reactor      #attaches to reactor
        
    def get_value(self):      #defines function, inherits from self(itself, the thermocouple?)
        if reactor.running:
            self.set_sensor_value(self.reactor.getph()) #gets ph from the reactor sets it as a value
        # else:
        #     self.set_sensor_value = microcontroller.get_ph()
        return get_sensor_value()   #returns the value gotten using get_sensor_value
        #allows that to be a value that future modules(for PID) can get
    
    
#test code for using fucntions defined in the parent class, not used by other programs
# if __name__ == '__main__':
#     phsensor = phsensor()           
                                         
#     print(phseonsor.get_sensor_value())  #in the test code, prints the sensor value, not used by other modules
#     #thermocouple.set_sensor_value(1000)     #example. sets value to 1000
#     #print(thermocouple.get_sensor_value())  
    

#I need to set up ph simulation in the reactor 
#I need to make a PID control file for pH. 
