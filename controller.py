# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 19:13:33 2021

@author: User
"""

import keyboard

from reactor1 import reactor

class controller():
    def __init__(self):
        pass
    
    def get_reactor_temp(self, item):
        print(item.gettemperature())
        
control = controller()

reactorone = reactor("reactor")

running = True
while running: 
    command = input()
    if command == "report temp":
        control.get_reactor_temp(reactorone)
    elif command == "stop":
        running = False
    elif command == "change temp":
        reactorone.setNewValue(25)
        print("It works")
    else:
        pass
    
    if keyboard.read_key()=="p":
        print("You pressed p!")

