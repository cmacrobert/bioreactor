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
        print("Temperature of The Reactor is " + str(self.temperature) + " degrees..." ) 
     
    def gettemperature(self): 
        print('Getting temperature') 
        return self.temperature 
 
    def settemperature(self, value): 
        print('Setting temperature to ' + value) 
        self.temperature = value 
     
    def resettemperature(self): 
        print('Resetting temperature') 
        self.temperature = self.initialtemperature 
        self.say() 
 
 
if __name__ == '__main__': 
    started = False 
    while started == False: 
        if input('>') == 'start reactor': 
            started = True 
    reactorone = reactor("reactor") 
    print('Reactor Started...') 
     
     
     
    running = True 
    while running:  
        command = input('>') 
        if command == "report": 
            reactorone.say() 
        if command == "set temperature":  
            reactorone.settemperature(input('Set Temperature >')) 
        if command == "reset temperature": 
            reactorone.resettemperature() 
        elif command == "turn off": 
            print('Shutting Down...') 
            running = False 
        else: 
            pass 
     