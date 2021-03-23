# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 17:53:02 2021

@author: Nat
"""
class reactor():
     
    def __init__ (self, temperature=10): #name was delected, not reffered to
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