# -*- coding: utf-8 -*-
from reactor import reactor
from sensors.thermocouple import thermocouple

#you have to start the reactor first
if __name__ == '__main__': 
    started = False 
    while started == False: 
        command = input('>')
        if command == 'start reactor' or command == 'hello' or command =='hi' or command == 'start': 
            started = True 
    reactorone = reactor("reactor")
    thermocouple = thermocouple(reactorone) #attaches thermocouple to the reactor
    print('Reactor Started...') 
#the main program now has a reactor and a thermocouple attached
    
     
    running = True 
    while running:  
        command = input('>') 
        if command == "report": 
            print(thermocouple.get_temperature())
        if command == "set temperature":  
            reactorone.settemperature(input('Set Temperature >')) 
        if command == "reset temperature": 
            reactorone.resettemperature() 
        elif command == "turn off" or command == "shut down": 
            print('Shutting Down...') 
            running = False 
        else: 
            pass 
        
        