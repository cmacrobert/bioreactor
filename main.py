# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:59:25 2021

@author: Calum
"""
import threading
import time
from inputs.input_returns import InputReturns as IR
import inputs.input_handler as IH
import pid_control
import sys

class Main():
    
    def __init__(self):
        self.input_handler = IH.InputHandler()
        self.pid_controller = pid_control.PIDControl()
    
    def start_thread_input(self):
        self.input_handler.start_thread()
        
    def start_thread_pid(self):
        self.pid_controller.start_thread()
    
    def shut_down(self):
        self.input_handler.stop_thread()
        self.pid_controller.stop_thread()
        sys.exit()
        
    def handle_command(self, command):
        if command == IR.NONE:
            print("Main - Error with command handling, received IR.NONE")
            #TODO: throw error. We should't be able to get here with a value of IR.NONE
        elif command == IR.SET_SETPOINT:            
            print("Main - handling command " + str(command))
            new_setpoint = self.input_handler.get_return_value()
            print("new setpoint is " + str(new_setpoint))
            self.input_handler.reset_value()
            self.pid_controller.set_setpoint(new_setpoint)
        elif command == IR.GET_TEMPERATURE:
            print("Main - handling command " + str(command))
            #TODO: return call to get thermocouple temperature
        elif command == IR.SET_TEMPERATURE:
            print("Main - handling command " + str(command))
            #TODO: return call to set reactor temperature
        elif command == IR.RESET_TEMPERATURE:
            print("Main - handling command " + str(command))
            #TODO: return call to reset reactor temperature
        elif command == IR.SHUT_DOWN:
            print("Main - handling command " + str(command))
            self.shut_down()
    
    def main(self):      
        print("Main - starting input thread")        
        thread_input = threading.Thread(target=self.start_thread_input, daemon=True)  
        thread_input.start()
        
        print("Main - starting PID thread")        
        thread_pid = threading.Thread(target=self.start_thread_pid, daemon=True)  
        thread_pid.start()
        
        while True:
            time.sleep(5)
            print("Main - 5 seconds passed")
            
            # Check if we've recieved any input commands
            command = self.input_handler.get_command()
            if command != IR.NONE:
                print("Main - command received, handle it")
                # Reset command, so we only handle it once
                self.input_handler.reset_command()                
                self.handle_command(command)                
            else:
                print("Main - no command received")

main = Main()
main.main()