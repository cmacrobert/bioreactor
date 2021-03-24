# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 17:53:02 2021

@author: Nat
"""

from sensors import peltiermodule
import numpy as np
import matplotlib.pyplot as plt
import time

class reactor():
     
    def __init__ (self, temperature=15): #name was delected, not reffered to
        #self.name = name #argument name is passed thorugh init statement)
        self.temperature = temperature 
        self.initialtemperature = temperature 
         
    def say(self): 
        print("Reactor - Temperature is " + str(self.temperature) + " degrees..." ) 
     
    def get_temperature(self): 
        print('Reactor - Getting temperature') 
        return self.temperature 
 
    def set_temperature(self, value): 
        print('Reactor - Setting temperature to ' + value) 
        self.temperature = value 
     
    def reset_temperature(self): 
        print('Reactor - Resetting temperature') 
        self.temperature = self.initialtemperature 
        self.say()
     
    
    def reactor_heating_cycle(self, T):
        t = np.arange(0, t_final, dt)
    
        for j in range(1, len(t)):  # looping for all elements in t
            plt.clf()  # clears for every for loop
            for i in range(1, n - 1):  # defines value of derivative for each spatial node
                dTdt[i] = alpha * (
                    -(T[i] - T[i - 1]) / dx ** 2 + (T[i + 1] - T[i]) / dx ** 2
                )  # end nodes have boundary condition, left side
            dTdt[0] = alpha * (
                -(T[0] - T1s) / dx ** 2 + (T[0 + 1] - T[0]) / dx ** 2
            )  # generic for inner nodes
            # dTdt[n-1] = alpha*(-(T[n-1]-T[n-1-1])/dx**2+(T2s-T[n-1])/dx**2) #the n-1 node
            T = T + dTdt * dt  # continuously update temp vector, gets overwritten each time
            plt.figure(1)  # for each cycle i want node T9 to become the reactor temperature
            plt.plot(x, T)
            plt.axis([0, L, 10, 35])
            plt.xlabel("Distance (m)")
            plt.ylabel("Temperature (C)")
            plt.show()
            plt.pause(0.05)
    
        # need to preserve Ts between cycles
        return T
    

L = 0.21  # radius of sphere in m
n = 10  # number of divisions
T0 = 15  # assumes start room temp but, water temperature need to be taken from last time interval
T1s = 27  # peltier temperature #needs to be setpoint{}{}{}{}{}
T2s = 15  # external temperature
dx = L / n
alpha = 0.00143
t_final = 1  # time interval lasts one second
dt = 0.1  # this is the time step
x = np.linspace(dx / 2, L - dx / 2, n)
T = np.ones(n) * T0  # start temperature vector
# but i want each to be taken from the last iteration
dTdt = np.empty(n)  # define empty vector

#warning, this runs forever while reactor is started/running
reactor = reactor(temperature=T0) #creates an instance of the reactor
running = True #so we can end the while loop at some point

while running: 
    T = reactor.reactor_heating_cycle(T) #function belongs to the reactor
    reactor.set_temperature = T[9]
    if __name__ == "__main__": #the if statement will not work in a thread
        time.sleep(0.2)         #in that case the overall program decides when sleeping happens
