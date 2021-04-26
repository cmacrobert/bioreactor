# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:59:25 2021

@author: Calum
"""
import thread_handler
import time
from inputs.input_returns import InputReturns as IR
import inputs.input_handler as IH
import effectors.heatercooler_redux as HC
import sys

class Main():
    
    def __init__(self):
        self.thread_handler = thread_handler.ThreadHandler()
        self.input_handler = IH.InputHandler()
        self.heatercooler = HC.heatercooler()
        self.running = False
        self.shutting_down = False
        
    def shut_down(self):
        """
        Stop all running threads before stopping main thread
        TODO: rename stop() functions? Only ending main loop, not thread
        """
        self.input_handler.stop()
        self.heatercooler.stop()
        self.thread_handler.stop_threads()
        self.running = False
        
    def handle_command(self, command):
        """
        Take appropriate action on receiving a command from input handler
        """
        if command == IR.NONE:
            """ TODO: throw error. We should't be able to get here"""
            print("Main: Error with command handling, received IR.NONE")
        elif command == IR.TEMPERATURE_SET_SETPOINT:
            new_setpoint = self.input_handler.get_return_value()
            self.input_handler.reset_return_value()
            self.heatercooler.set_setpoint(new_setpoint)
        elif command == IR.TEMPERATURE_SET_START:
            new_start = self.input_handler.get_return_value()
            self.input_handler.reset_return_value()
            self.heatercooler.set_start_value(new_start)
            print("Main: Start value applied, will take effect on reset")
        elif command == IR.TEMPERATURE_RESET:
            self.heatercooler.reset()
        elif command == IR.GET_TEMPERATURE:
            """ TODO: return call to get thermocouple temperature"""
            print("Main: command " + str(command) + "not implemented")
        elif command == IR.SET_TEMPERATURE:
            """ TODO: return call to set reactor temperature"""
            print("Main: command " + str(command) + "not implemented")
        elif command == IR.RESET_TEMPERATURE:
            """ TODO: return call to reset reactor temperature"""
            print("Main: command " + str(command) + "not implemented")
        elif command == IR.SHUT_DOWN:
            self.shut_down()
    
    def main(self):
        """
        Main loop starts threads for input handler and effectors
            then continually polls for input commands to handle
            Currently waiting 1 second between polling, to aid debugging
        """
        self.thread_handler.start_thread("input",
                                         self.input_handler.start)
        self.thread_handler.start_thread("heatercooler",
                                         self.heatercooler.start)
        
        self.running = True
        while (self.running == True):
            time.sleep(1)   # Delay when polling, mainly for debugging
            
            """ Check if we've recieved any input commands"""
            command = self.input_handler.get_command()
            if command != IR.NONE:
                """ Reset command, so we only handle it once"""
                self.input_handler.reset_command()                
                self.handle_command(command)
        
        self.shutting_down = True
        while (self.shutting_down == True):
            """ Check all other threaded processes have stopped"""
            if (self.input_handler.get_running() == False and 
                self.heatercooler.get_running() == False):
                self.shutting_down = False
        print("Main: Shutdown complete")

main = Main()
main.main()