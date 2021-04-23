#i want to it run an instance of the PID, with a gettable funtion output, 
#this is the funtion in the pid_control

#   def get_target(self, value):
#        self.get_target(value) = 25                #using this value as a placeholder

#in the case that this is passed to the simulated reactor it is converted to a
#temperature. If not,the value is taken by the microcontroller file 

#from effectors.base import EffectorBase        #imported the thermocouple information 
#from sensors.thermocouple import thermocouple  #from folder.file import class
import pid_control
from reactor import reactor
import microcontroller


class heatercooler(EffectorBase, pid_control):  #establishes class  #inherites from these classes
    def __init__(self, reactor):                #????? object is created from the class, initialize the attributes of a class.
    def __init__(self, microcontroller):
        
    EffectorBase.__init__(self):                 # run it's init fuction
        pid_control.__init__(self):              # uses it's init, but does not attach anything
        self.reactor = reactor                   #^passes the reactor through to the modules. 
                                             
        
    def get_temp(self,value):                         #defines a function for the class, get_temp
        self.pid_control.get_target(value())    #asking already attached pid_control to get the temperature
        return super().value()                  #tells to call it from the parent class
   
        
    # need to overide value each time in the def time_step_forward(self): function
    def time_step_forward(self):      
    # needs to be set for every loop, because it might be different. 
        self.time_step_forward = self.get_temp()
        #call function time step forward in the super class
        super().time_step_forward() 
        
   
    def pass_the_value(self):
    if reactor = running:
    #convert the value to a temperature bytimesing it by 0.33 for example
         self.time_step_forward = self.get_temp()*0.3
    #then pass it to the reactor which GETS time step forward? 
    
    else
    #pass the value to the microcontroller to be converted inside it with C code.
    pass

# #test code for using functions defined in the parent class
# if __name__ == '__main__':
#     heatercooler = heatercooler(reactor()) #passes reactor to the heatercooler, modules can now interact
#     print(heatercooler.thermocouple.get_temperature()) #refers to  self.thermocouple = thermocouple(reactor)
 