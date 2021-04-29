# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:59:25 2021

@author: Calum
"""
import thread_handler
import time
import effectors.heatercooler as HC
import reactor
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Main():
    
    def __init__(self):
        self.thread_handler = thread_handler.ThreadHandler()
        self.heatercooler = HC.heatercooler()
        self.reactor = reactor.reactor()
        self.running = False
        self.shutting_down = False
        self.update_delay = 500
        
    def shut_down(self):
        """
        Stop all running threads before stopping main thread
        TODO: rename stop() functions? Only ending main loop, not thread
        TODO: display "shutting down, please wait" message (with status?)
        """
        self.m.after_cancel(self.window_update)
        self.window_update = None
        self.heatercooler.stop()
        self.reactor.stop()        
        self.thread_handler.stop_threads()
        self.running = False
        self.m.quit()
    
    def start_drawing(self):
        print("Main - Starting drawing")
        self.m = tk.Tk(className='Bioreactor Simulator')
        self.m.title("Bioreactor Simulator")
        self.m.geometry("800x600")
        self.m['background']='white'
        
        ''' Canvas, used for drawing manually '''
        canvas = tk.Canvas(self.m, width=800, height=600)
        canvas.pack()
        
        ''' Menu '''
        self.menu = tk.Menu(self.m)
        self.m.config(menu=self.menu)
        ''' File - Reset and Exit'''
        self.filemenu = tk.Menu(self.menu)
        self.menu.add_cascade(label='File', menu=self.filemenu)
        self.filemenu.add_command(label='Reset', command=self.button_pressed)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit', command=self.on_closing)
        ''' Help - About'''
        self.helpmenu = tk.Menu(self.menu)
        self.menu.add_cascade(label='Help', menu=self.helpmenu)
        self.helpmenu.add_command(label='About', command=self.show_about)
        
        #''' Text entry box '''
        #tk.Label(canvas, text='Text Entry').grid(row=0)
        #self.txtentry = tk.Entry(canvas)
        #self.txtentry.grid(row=0, column=1)
        
        #''' Buttons '''
        #btn_reset = tk.Button(self.m, text='Reset', width=25, 
        #                     command=self.button_pressed)
        #btn_reset.pack()        
        #btn_quit = tk.Button(self.m, text='Quit', width=25, 
        #                     command=self.on_closing)
        #btn_quit.pack()
                
        ''' Matplotlib plot '''        
        figure = plt.figure(figsize=(6,5), dpi=100)
        self.ax = figure.add_subplot(111)
        self.plot_canvas = FigureCanvasTkAgg(figure, master=canvas)#self.m)
        self.plot_canvas.get_tk_widget().pack()
    
        ''' Call the gui_update function once, after set time has passed '''
        self.window_update = self.m.after(self.update_delay, 
                                          self.gui_update)
    
        ''' Set up window functions '''
        self.m.protocol("WM_DELETE_WINDOW", self.on_closing)
    
        ''' Start main loop (do this last) '''
        self.m.mainloop()
        
    def on_closing(self):
        #TODO: clear display and replace with "shutting down" message
        #TODO: reimplement confirmation box, without breaking threading
        #if messagebox.askokcancel("Quit", "Do you want to quit?"):
        self.shut_down()
        
    def show_about(self):
        #this looks ugly, but multiline text takes tabs into account
        message_to_show = """text
across
multiple
lines"""
        self.messagebox = tk.messagebox.Message(self.m)
        self.messagebox.show(title="About", message=message_to_show)
        
    def draw_plot(self):
        ''' Draw plot on canvas after getting latest x and y values'''
        #TODO: make this more generic, not just for heatercooler
        x = self.heatercooler.get_x()
        y = self.heatercooler.get_y()
        
        self.ax.clear()
        self.ax.plot(x,y)
        self.ax.hlines(self.heatercooler.get_setpoint(), 0, 5, 'C1', 'dashed')
        plt.xlim(0,1)
        plt.ylim(0,55)
        self.plot_canvas.draw_idle()
        
    def gui_update(self):
        ''' Update GUI, refreshing plots '''
        self.draw_plot()
        
        ''' Schedule update function again'''
        self.window_update = self.m.after(self.update_delay,
                                          self.gui_update)
        
    def button_pressed(self):
        print("Main - Button was pressed")
        #print("Main - Text entry contents = " + str(self.txtentry.get()))
        self.heatercooler.reset()
    
    def updater(self):     #grabs values from reactor, passes them to places. 
        self.thermocouple.set_sensor_value(self.reactor.get_temperature())
        self.heatercooler.set_current_value(self.thermocouple.get_sensor_value())
        self.reactor.set_peltier_temp(self.heatercooler.get_current_value())

        self.phsensor.set_sensor_value(self.reactor.get_ph()) 
        self.phcontrol.set_current_value(self.phsensor.get_sensor_value())
        self.reactor.set_ph(self.phcontrol.get_current_value())
    
    def main(self):
        '''
        Main loop starts threads for window and effectors
            then continually runs own update function
            Currently waiting 1 second between updates, to aid debugging
        '''
        self.running = True
        
        self.thread_handler.start_thread("heatercooler",
                                         self.heatercooler.start)
        self.thread_handler.start_thread("reactor",
                                         self.reactor.start)        
        self.thread_handler.start_thread("window",
                                         self.start_drawing)
        
        while (self.running == True):
            time.sleep(1)   # Delay when polling, mainly for debugging
            #TODO: call main update function here
                    
        self.shutting_down = True
        while (self.shutting_down == True):
            """ Check all other threaded processes have stopped"""
            if (self.heatercooler.get_running() == False and
                self.reactor.get_running() == False):            
                self.shutting_down = False
        print("Main - Shutdown complete")

main = Main()
main.main()