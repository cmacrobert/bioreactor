# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:45:20 2021

@author: Calum
"""

from inputs.input_returns import InputReturns as IR

class InputHandler():

    def __init__ (self):
        print("InputHandler: Initialising")
        self.reset_command()
        self.reset_return_value()
        self.running = False
        
    def get_command(self):
        return self.return_command
    
    def reset_command(self):
        self.return_command = IR.NONE
        
    def get_return_value(self):
        return self.return_value
    
    def reset_return_value(self):
        self.return_value = 0
        
    def get_running(self):
        return self.running
    
    def start(self):
        """
        Main loop for input handler
        Continually awaits input from user via console
        Sets return command on receiving recognised command
        """
        print("InputHandler: Starting thread")
        
        self.running = True
        while self.running == True:            
            command = input('>')
            print("InputHandler: Command recieved: " + command)
            if command == "set T SP":
                return_value = float(input('Set Temperature SetPoint >'))
                self.return_value = return_value
                self.return_command = IR.TEMPERATURE_SET_SETPOINT
            elif command == "set T start":
                return_value = float(input('Set Starting Temperature >'))
                self.return_value = return_value
                self.return_command = IR.TEMPERATURE_SET_START
            elif command == "reset":
                self.return_command = IR.TEMPERATURE_RESET
            elif command == "report": 
                self.return_command = IR.GET_TEMPERATURE
            elif command == "set temperature":  
                self.return_command = IR.SET_TEMPERATURE
            elif command == "reset temperature": 
                self.return_command = IR.RESET_TEMPERATURE
            elif command == "turn off" or command == "shut down":
                self.return_command = IR.SHUT_DOWN
                #TODO: prevent further input() in a better way
                #setting self.running=False works but it's a bit hacky
                #Have you tried sys.exit(0)?
                self.running = False                    
            else:
                print("InputHandler: Command not recognised: " + command)
                pass
        print("InputHandler: Exited loop")
            
    def stop(self):
        print("InputHandler: Stopping thread")
        self.running = False