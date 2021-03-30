#inherit from base class
from effectors.base import EffectorBase
#imported the thermocouple information 
from sensors.thermocouple import thermocouple
from pid.natpid import stefanpid #from folder.file import class
from sensors.peltiermodule import peltiermodule
from reactor import reactor

class heatercooler(EffectorBase, stefanpid): #establishes class  #inherites from these classes
    def __init__(self, reactor):  #object is created from the class, initialize the attributes of a class.
    #def __init__(self, thermocouple, peltiermodule, reactor): # DO NOT DO THIS attaches thermo to heater 
    #def __init__(self, mainprogram): # DO NOT DO THIS, it will attach the wrong way around
        EffectorBase.__init__(self)   # run it's init fuction
        stefanpid.__init__(self)      # uses it's init, but does not attach anything
        self.thermocouple = thermocouple(reactor) #fully attaches reactor to the modules via thermocouple
        #self.peltiermodule = peltiermodule(reactor) # WHY IT NOT WORK?! # expects to be attached to peltier module now
        self.reactor = reactor    #^passed the reactor through to the modules. 
                                    #only want thermo and peltier to exist if have heatercooler. 
        
    def get_temp(self): # defines a fucntion for the class, get_temp
        self.thermocouple.get_temperature() #asking already attached thermocouple to get the temperature
        # print (self.get_temp())           #not needed
        return super().get_temp()           #tells to call it from the parent effector class
     

    # need to overirde MV_bar in the  def time_step_forward(self): function
    def time_step_forward(self):        #named the same as in the pid!
    # needs to be set for every loop, because it might be different. 
        #before running, need to pass MV_bar to the heater
        self.MV_bar = self.get_temp()
        #call function time step forward in the super class
        super().time_step_forward() 
        
 

        
#test code for using functions defined in the parent class
if __name__ == '__main__':
    heatercooler = heatercooler(reactor()) #passes reactor to the heatercooler, modules can now interact
    print(heatercooler.thermocouple.get_temperature()) #refers to  self.thermocouple = thermocouple(reactor)
 
    