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
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Main():
    
    def __init__(self):
        self.thread_handler = thread_handler.ThreadHandler()
        self.input_handler = IH.InputHandler()
        self.heatercooler = HC.heatercooler()
        self.running = False
        self.shutting_down = False
        self.update_delay = 500
        
    def shut_down(self):
        """
        Stop all running threads before stopping main thread
        TODO: rename stop() functions? Only ending main loop, not thread
        TODO: display "shutting down, please wait" message (with status?)
        """
        self.input_handler.stop()
        self.heatercooler.stop()
        self.thread_handler.stop_threads()
        self.running = False        
        self.m.destroy()
        
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
    
    def start_drawing(self):
        print("starting WindowTest")
        self.m = tk.Tk(className='Test Window')
        self.m.title("Test window")
        self.m.geometry("800x600")
        self.m['background']='white'
        
        ''' Canvas, used for drawing manually '''
        canvas = tk.Canvas(self.m, width=800, height=600)
        canvas.pack()
        
        ''' Text entry box '''
        tk.Label(canvas, text='Text Entry').grid(row=0)
        self.txtentry = tk.Entry(canvas)
        self.txtentry.grid(row=0, column=1)
        
        ''' Buttons '''
        btn_reset = tk.Button(self.m, text='Reset', width=25, 
                             command=self.button_pressed)
        btn_reset.pack()        
        btn_quit = tk.Button(self.m, text='Quit', width=25, 
                             command=self.shut_down)
        btn_quit.pack()        
                
        ''' Matplotlib plot'''        
        figure = plt.figure(figsize=(6,5), dpi=100)
        self.ax = figure.add_subplot(111)
        self.plot_canvas = FigureCanvasTkAgg(figure, master=self.m)
        self.plot_canvas.get_tk_widget().pack()
    
        ''' Call the check_for_updates function once, after set time has passed'''
        self.m.after(self.update_delay, self.check_for_updates)
    
        ''' Start main loop (do this last) '''
        self.m.mainloop()
        
    def draw_plot(self):
        x = self.heatercooler.get_x()
        y = self.heatercooler.get_y()
        
        self.ax.clear()
        self.ax.plot(x,y)
        self.ax.hlines(self.heatercooler.get_setpoint(), 0, 5, 'C1', 'dashed')
        plt.xlim(0,1)
        plt.ylim(0,55)
        self.plot_canvas.draw_idle()
        
    def check_for_updates(self):
        #TODO: ensure this gets cancelled when we want to shut down
        # currently having issue where it lingers on subsequent runs
        print("Checking for updates")
        self.draw_plot()
        
        ''' Schedule update function again'''
        self.m.after(self.update_delay, self.check_for_updates)
        
    def button_pressed(self):
        print("Button was pressed")
        print("Text entry contents = " + str(self.txtentry.get()))
        self.heatercooler.reset()
    
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
        self.thread_handler.start_thread("window",
                                         self.start_drawing)
        
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