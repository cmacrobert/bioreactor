# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:45:20 2021

@author: Calum
"""

from inputs.input_returns import InputReturns as IR

class InputHandler():

    def __init__ (self):
        print("Input handler - Initialising")
        self.reset_command()
        self.reset_return_value()
        self.running = False
        
    def get_command(self):
        return self.return_command
    
    def reset_command(self):
        print("Input handler - Resetting command")
        self.return_command = IR.NONE
        
    def get_return_value(self):
        return self.return_value
    
    def reset_return_value(self):
        print("Input handler - Resetting value")
        self.return_value = 0
    
    def start_thread(self):
        print("Input handler - Starting thread")
        
        self.running = True
        while self.running == True:
            command = input('>')
            print("Command recieved: " + command)
            if command == "set T SP":
                return_value = float(input('set Temperature SetPoint >'))
                print("return value is " + str(return_value))
                self.return_value = return_value
                self.return_command = IR.PID_SET_SETPOINT
            elif command == "set T start":
                return_value = float(input('set Starting Temperature >'))
                print("return value is " + str(return_value))
                self.return_value = return_value
                self.return_command = IR.PID_SET_START
            elif command == "reset":
                self.return_command = IR.PID_RESET
            elif command == "report": 
                self.return_command = IR.GET_TEMPERATURE
            elif command == "set temperature":  
                self.return_command = IR.SET_TEMPERATURE
            elif command == "reset temperature": 
                self.return_command = IR.RESET_TEMPERATURE
            elif command == "turn off" or command == "shut down":
                self.return_command = IR.SHUT_DOWN                              
            else:
                pass
        print("Input handler - Exited loop")
            
    def stop_thread(self):
        print("Input handler - Stopping thread")
        self.running = False