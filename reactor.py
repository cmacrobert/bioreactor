# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 17:53:02 2021

@author: Nat
"""

import numpy as np
import time

class reactor():
     
    def __init__ (self, temperature=15, ph=7): 
        #self.name = name #argument name is passed thorugh init statement
        self.temperature = temperature 
        self.initialtemperature = temperature 
        self.peltier_temp = temperature #well, its an input, its not the reactor temperature
        self.running = False

        #i guess it needs more inits
        self.ph = ph
        self.initialph = ph
        self.ph_into_reactor = ph #i hope so
        #self.running = False
        self.name = "Reactor"
        self.P = ph
        self.T = temperature
        
    def get_running(self):
        return self.running
 #_________________________________________________    
    def get_temperature(self): 
        print('Reactor - Getting temperature') 
        return self.temperature 

    def set_peltier_temp(self, temp):
        self.peltier_temp = temp
        
#___________________________________________________________________        
    def get_ph(self): 
        print('Reactor - Getting ph') 
        return self.ph 
        
    
    def set_ph_input(self, phinput):
        self.ph_into_reactor = phinput #hhmmm
    
    
#___________________________________________________________________
    #MIRRIN
    
    #def get_pressure(pressure):
     #   pass
 
    def set_pressure_input(self, pressure):
        self.set_pressureinput = pressure
        #not yet used by reactor
        pass
#___________________________________________________________________    
    def reset_temperature(self): 
        print('Reactor - Resetting temperature') 
        self.temperature = self.initialtemperature     
    
    def reactor_heating_cycle(self):
        T = self.T
        
        L = 0.21  # radius of sphere in m
        n = 10  # number of divisions
        T0 = 15  # assumes start room temp but, water temperature need to be taken from last time interval
        dx = L / n
        alpha = 0.00143
        t_final = 1  # time interval lasts one second
        dt = 0.1  # this is the time step
        x = np.linspace(dx / 2, L - dx / 2, n)
        T = np.ones(n) * T0  # start temperature vector
        # each to be taken from the last iteration
        dTdt = np.empty(n)  # define empty vector

        t = np.arange(0, t_final, dt)
    
        for j in range(1, len(t)):  # looping for all elements in t
            for i in range(1, n - 1):  # defines value of derivative for each spatial node
                dTdt[i] = alpha * (
                    -(T[i] - T[i - 1]) / dx ** 2 + (T[i + 1] - T[i]) / dx ** 2
                )  # end nodes have boundary condition, left side
            dTdt[0] = alpha * (
                -(T[0] - self.peltier_temp) / dx ** 2 + (T[0 + 1] - T[0]) / dx ** 2
            )  # generic for inner nodes
            dTdt[n-1] = alpha*(-(T[n-1]-T[n-1-1])/dx**2+(self.peltier_temp*0.8-T[n-1])/dx**2) #the n-1 node
            T = T + dTdt * dt  # continuously update temp vector, gets overwritten each time
            # plt.figure(1) 
            # plt.plot(x, T)
            # plt.axis([0, L, 10, 35])
            # plt.xlabel("Distance (m)")
            # plt.ylabel("Temperature (C)")
            # plt.show()
            # plt.pause(0.05)
            
        # need to preserve Ts between cycles
        self.T = T
        self.temperature = T[5]

#_____________________________________________________________________________
#PH SIMULATION - initally a clone of the temp simulation... 
#could i make this into am inheritable class
#changing all the values is a faff

    def reset_ph(self): 
        print('Reactor - Resetting ph') 
        self.ph = self.initialph     
    
    def reactor_ph_cycle(self):
        P = self.P
        
        L = 0.21  # radius of sphere in m
        n = 10  # number of divisions
        P0 = 7  # assumes start reacotr temp is 7, tho needs to be taken from last time interval
        dx = L / n
        alpha = 0.00143
        t_final = 1  # time interval lasts one second
        dt = 0.1  # this is the time step
        x = np.linspace(dx / 2, L - dx / 2, n)
        P = np.ones(n) * P0  # start ph vector
        # each to be taken from the last iteration
        dPdt = np.empty(n)  # define empty vector
        
        t = np.arange(0, t_final, dt)
        
        for j in range(1, len(t)):  # looping for all elements in t
            for i in range(1, n - 1):  # defines value of derivative for each spatial node
                dPdt[i] = alpha * (
                    -(P[i] - P[i - 1]) / dx ** 2 + (P[i + 1] - P[i]) / dx ** 2
                )  # end nodes have boundary condition, left side
            dPdt[0] = alpha * (
                -(P[0] - self.ph_into_reactor) / dx ** 2 + (P[0 + 1] - P[0]) / dx ** 2
            )  # generic for inner nodes
            dPdt[n-1] = alpha*(-(P[n-1]-P[n-1-1])/dx**2+(self.ph_into_reactor*0.8-P[n-1])/dx**2) #the n-1 node
           
            P = P + dPdt * dt  # continuously update ph vector, gets overwritten each time
            # plt.figure(1) 
            # plt.plot(x, P)
            # plt.axis([0, L, 10, 35])
            # plt.xlabel("Distance (m)")
            # plt.ylabel("pH")
            # plt.show()
            # plt.pause(0.05)
                
        # need to preserve Ps between cycles
        self.P = P
        self.ph = P[5]   
        
    def start(self):
        self.running = True
       
        while (self.running == True):
            time.sleep(1)
            self.reactor_heating_cycle()                        
            self.reactor_ph_cycle()
           
    def stop(self):
        print(self.name + ": Stopping thread")
        self.running = False