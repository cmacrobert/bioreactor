from sensors.base import SensorBase

class thermocouple(SensorBase):

    def __init__(self, reactor):
        super().__init__()
        self.label = 'thermocouple'
#needs to expect to be attached to a reactor    
        self.reactor = reactor 
        
    def get_temperature(self):
        self.set_sensor_value(self.reactor.gettemperature())
        return super().get_sensor_value()
        
#test code for using fucntions defined in the parent class
if __name__ == '__main__':
    thermocouple = thermocouple()
    print(thermocouple.get_sensor_value())

