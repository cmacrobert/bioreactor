#inherit from base class
from effectors.base import EffectorBase
#imported the thermocouple information 
from sensors.thermocouple import thermocouple



class heatercooler(EffectorBase):
    def __init__(self):
    #def __init__(self, mainprogram):
        super().__init__()
        self.label = 'heatercooler'

    def get_temp(self):
        (self.thermocouple.getemperature())
        return super().get_temp()
        print (self.get_temp())

   # def getpidtemp(self, temp): 
   #     get_temperature() = temp
   #     PID(MV_bar=0) = temp
   #     print('changing MV_bar to temperature sensed by thermocouple which is: ' + temp) 
        
import time 
import matplotlib.pyplot as plt 
import random 
 
xMax = 200 
x=[] 
y=[] 
print('Reactor Started') 
T = 0 
MV_bar = heatercooler.get_temp(self) 
val = MV_bar 
e_prev = 0 
e = 0 
t_prev = 0 
t = 1 
I = 0 
Kp = 0.05 
Ki = 0.05 
Kd = 0.05 
SP = 37 
counter = 0 
     
while True: 
    # PID calculations 
    e = SP - val 
     
    if abs(e) < 1: 
        val = MV_bar = random.choice([10,20,40,50]) 
        P = I = D = 0 
     
    x.append(t) 
    y.append(val) 
         
    plt.cla() 
    plt.plot(x,y) 
    plt.show() 
    #print(val) 
         
    P = Kp*e 
    I = I + Ki*e*(t - t_prev) 
    D = Kd*(e - e_prev)/(t - t_prev) 
         
    val = MV_bar + P + I + D 
          
    # update stored data for next iteration 
    e_prev = e 
    t_prev = t     
    t = t+1 
         
    time.sleep(0.25) 
    counter += 1 
    print(counter) 
         
    #if t==xMax: 
        # plt.plot(x,y) 
        # exit()







        
#test code for using fucntions defined in the parent class
if __name__ == '__main__':
    heatercooler = heatercooler()
    print(thermocouple.get_temperature())
 
    