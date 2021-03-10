# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 18:49:40 2021

@author: User
"""


class reactor():
    
    def __init__ (self, name, temperature=10):
        self.name = name
        self.temp = temperature
        
    def say(self):
        print("i am a " + self.name + ", my temperature is  " + str(self.temp) + " ..." )
    
    def gettemperature(self):
        return self.temp

    #def settemperature(self):
        #pass
        
    def setNewValue(self, newValue):
        self.temp = newValue
        print("changing temp to"+str(newValue))

    def changetemperature(self):
        pass


if __name__ == '__main__':
    reactorone = reactor("reactor")
    
    
    
    switch = 0;
    running = True
    while running: 
        command = input()
        if command == "report":
            reactorone.say()
        elif command == "stop":
                running = False
        else:
            pass
    

