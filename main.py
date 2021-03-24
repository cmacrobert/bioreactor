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
        """
        Stop all running threads before stopping main thread
        TODO: move to thread_handler
        """
        self.input_handler.stop_thread()
        self.pid_controller.stop_thread()
        sys.exit()  #TODO: confirm other threads are closed first
        
    def handle_command(self, command):
        """
        Take appropriate action on receiving a command from input handler
        """
        if command == IR.NONE:
            """ TODO: throw error. We should't be able to get here"""
            print("Main - Error with command handling, received IR.NONE")
        elif command == IR.PID_SET_SETPOINT:
            new_setpoint = self.input_handler.get_return_value()
            self.input_handler.reset_return_value()
            self.pid_controller.set_setpoint(new_setpoint)
        elif command == IR.PID_SET_START:
            new_start = self.input_handler.get_return_value()
            self.input_handler.reset_return_value()
            self.pid_controller.set_start_temperature(new_start)
            print("Start value applied, will take effect on reset")
        elif command == IR.PID_RESET:
            self.pid_controller.reset()
        elif command == IR.GET_TEMPERATURE:
            """ TODO: return call to get thermocouple temperature"""
            print("Main - command " + str(command) + "not implemented")
        elif command == IR.SET_TEMPERATURE:
            """ TODO: return call to set reactor temperature"""
            print("Main - command " + str(command) + "not implemented")
        elif command == IR.RESET_TEMPERATURE:
            """ TODO: return call to reset reactor temperature"""
            print("Main - command " + str(command) + "not implemented")
        elif command == IR.SHUT_DOWN:
            self.shut_down()
    
    def main(self):
        """
        Main loop starts threads for input handler and PID
            then continually polls for input commands to handle
            Currently waiting 1 second between polling, to aid debugging
        """
        thread_input = threading.Thread(target=self.start_thread_input,
                                        daemon=True)  
        thread_input.start()
            
        thread_pid = threading.Thread(target=self.start_thread_pid, 
                                      daemon=True)  
        thread_pid.start()
        
        while True:
            time.sleep(1)   # Delay when polling, mainly for debugging
            
            """ Check if we've recieved any input commands"""
            command = self.input_handler.get_command()
            if command != IR.NONE:
                """ Reset command, so we only handle it once"""
                self.input_handler.reset_command()                
                self.handle_command(command)

main = Main()
main.main()