# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 11:51:58 2021

@author: User
"""

import time 
import matplotlib.pyplot as plt 
import random 

class stefanpid():
    #in a class beacause different effectors need "thier own instance" of the class
         
    def __init__(self):    
        #gather ingredients
        self.label = "pidcontroller"
        self.sensor_value = float(0)
        self.xMax = 200 
        self.x=[] 
        self.y=[] 
        #print('Reactor Started') 
        self.T = 0 
        self.MV_bar = 0 
        self.val = self.MV_bar 
        self.e_prev = 0 
        #self.e = 0 
        self.t_prev = 0 
        self.t = 1 
        self.I = 0 
        self.Kp = 0.05 
        self.Ki = 0.05 
        self.Kd = 0.05 
        self.SP = 37 
        self.counter = 0  
 
        
    def time_step_forward(self):
        #mix the ingredients
        # PID calculations 
        e = self.SP - self.val #always set e at function start
         
        if abs(e) < 1: 
            self.val = self.MV_bar = random.choice([10,20,40,50]) 
            self.P = self.I = self.D = 0 
         
        self.x.append(self.t) 
        self.y.append(self.val) 
             
        plt.cla() 
        plt.plot(self.x,self.y) 
        plt.show() 
        #print(val) 
             
        self.P = self.Kp*e 
        self.I = self.I + self.Ki*e*(self.t - self.t_prev) 
        self.D = self.Kd*(e - self.e_prev)/(self.t - self.t_prev) 
             
        self.val = self.MV_bar + self.P + self.I + self.D 
              
        # update stored data for next iteration 
        self.e_prev = e 
        self.t_prev = self.t     
        self.t = self.t+1 
             
        time.sleep(0.25) 
        self.counter += 1 
        print(self.counter) 
             
        #if t==xMax: 
            # plt.plot(x,y) 
            # exit()
            
#test code, not part of class or function
if __name__ == '__main__': #magic things
    testobjectforpid = stefanpid()
    while True:
        testobjectforpid.time_step_forward()
        time.sleep(0.25)
    