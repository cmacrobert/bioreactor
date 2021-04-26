# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 11:29:40 2021

@author: Calum
"""

#Colour hex values
#Cellexus green #00B388
#Cellexus dark blue #071D49

import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

class WindowTest():
        
    def __init__(self):
        self.update_delay = 5000    #time to wait between update calls
        self.freq = 5               #frequency for test sinewave
        
    def shut_down(self):
        print("Shutting down")
        self.m.destroy()
    
    def start(self):
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
        
        ''' Check buttons, with variables for tracking check state'''
        self.opt1 = tk.IntVar()
        self.opt2 = tk.IntVar()
        checkbtn1 = tk.Checkbutton(canvas, text='Option A', variable=self.opt1)
        checkbtn1.grid(row=1, sticky=tk.W)
        checkbtn2 = tk.Checkbutton(canvas, text='Option B', variable=self.opt2)
        checkbtn2.grid(row=2, sticky=tk.W)
        
        ''' Buttons '''
        btn_test = tk.Button(self.m, text='Test', width=25, 
                             command=self.button_pressed)
        btn_test.pack()        
        btn_quit = tk.Button(self.m, text='Quit', width=25, 
                             command=self.shut_down)
        btn_quit.pack()    
        
                
        ''' Matplotlib plot'''        
        figure = plt.figure(figsize=(6,5), dpi=100)
        self.ax = figure.add_subplot(111)
        self.plot_canvas = FigureCanvasTkAgg(figure, master=self.m)
        self.plot_canvas.get_tk_widget().pack()
        self.plot_sine_wave()
        
    
        ''' Call the check_for_updates function once, after set time has passed'''
        self.m.after(self.update_delay, self.check_for_updates)
    
        ''' Start main loop (do this last) '''
        self.m.mainloop()
        
    def plot_sine_wave(self):
        print("Plotting sinewave with frequency " + str(self.freq))
        
        ''' Define sine wave for testing'''
        x = np.arange(8000)
        y = np.sin(2*np.pi*self.freq*x / 8000)
        
        ''' Matplotlib plot'''
        self.ax.clear()
        self.ax.plot(x,y)
        self.plot_canvas.draw_idle()
        
    def check_for_updates(self):
        #TODO: ensure this gets cancelled when we want to shut down
        # currently having issue where it lingers on subsequent runs
        print("Checking for updates")
        
        ''' Schedule update function again'''
        self.m.after(self.update_delay, self.check_for_updates)

    def button_pressed(self):
        print("Button was pressed")
        print("opt1 = " + str(self.opt1.get()))
        print("opt2 = " + str(self.opt2.get()))
        print("text entry contents = " + str(self.txtentry.get()))
        self.freq = int(self.txtentry.get())
        self.plot_sine_wave()
      
window_test = WindowTest()
window_test.start()