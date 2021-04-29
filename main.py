# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:59:25 2021

@author: Calum
"""
import thread_handler
import time
import effectors.heatercooler as HC
import effectors.phcontrol as PH
import sensors.thermocouple as TC
import sensors.phsensor as PS
import reactor
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Main():
    
    def __init__(self):
        self.thread_handler = thread_handler.ThreadHandler()
        self.heatercooler = HC.heatercooler()
        self.phcontrol = PH.phcontrol()
        self.reactor = reactor.reactor()        
        self.thermocouple = TC.thermocouple()
        self.phsensor = PS.phsensor()        
        self.running = False
        self.shutting_down = False
        self.update_delay = 250
        self.should_update_setpoint = False
        self.should_update_spinbox = False
        
    def shut_down(self):
        """
        Stop all running threads before stopping main thread
        TODO: rename stop() functions? Only ending main loop, not thread
        TODO: display "shutting down, please wait" message (with status?)
        """
        self.m.after_cancel(self.window_update)
        self.window_update = None
        self.heatercooler.stop()
        self.phcontrol.stop()
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
                
        ''' Menu '''
        self.menu = tk.Menu(self.m)
        self.m.config(menu=self.menu)
        ''' File - Reset and Exit'''
        self.filemenu = tk.Menu(self.menu)
        self.menu.add_cascade(label='File', menu=self.filemenu)
        self.filemenu.add_command(label='Reset', command=self.on_reset)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit', command=self.on_closing)
        ''' Help - About'''
        self.helpmenu = tk.Menu(self.menu)
        self.menu.add_cascade(label='Help', menu=self.helpmenu)
        self.helpmenu.add_command(label='About', command=self.show_about)
            
               
        ''' Canvas, used for drawing manually '''
        canvas = tk.Canvas(self.m, width=800, height=600)
        canvas.pack(side=tk.LEFT)
        
        ''' Matplotlib plot '''        
        figure = plt.figure(figsize=(6,5), dpi=100)
        self.ax = figure.add_subplot(111)
        self.plot_canvas = FigureCanvasTkAgg(figure, master=canvas)#self.m)
        self.plot_canvas.get_tk_widget().pack()
        
        
        '''Controls frame '''
        frame_controls = tk.Frame(self.m, width=200, height=200)
        frame_controls.pack(side=tk.RIGHT)
        
        ''' Setpoint control '''
        frame_setpoint = tk.Frame(frame_controls, width=200, height=200)
        frame_setpoint.pack(pady=20)
        btn_setpoint = tk.Button(frame_setpoint, text='Set Setpoint', width=25, 
                             command=self.set_setpoint)
        btn_setpoint.pack()
        self.spinbox = spinbox=tk.Spinbox(frame_setpoint)
        spinbox.pack()
        
        ''' Effector selection '''
        frame_plot_select = tk.Frame(frame_controls, width=200, height=200)
        frame_plot_select.pack(pady=20)        
        label_plot_select = tk.Label(frame_plot_select, text="Plot Shown:", justify=tk.LEFT)
        label_plot_select.pack()
        self.selected_plot = tk.IntVar(self.m)
        radbtn_temp = tk.Radiobutton(frame_plot_select, text="Temperature", indicatoron=0,
                                     variable=self.selected_plot, value=0,
                                     command=self.change_plot_source)
        radbtn_temp.pack()
        radbtn_ph = tk.Radiobutton(frame_plot_select, text="pH", indicatoron=0,
                                   variable=self.selected_plot, value=1,
                                   command=self.change_plot_source)
        radbtn_ph.pack()
        
        ''' Labels for current values'''     
        frame_labels = tk.Frame(frame_controls, width=200, height=200)
        frame_labels.pack(pady=20)
        
        frame_label_temp = tk.Frame(frame_labels, width=200, height=100)
        frame_label_temp.pack()
        label_temp = tk.Label(frame_label_temp, text="Temperature:", justify=tk.LEFT)
        label_temp.pack(side=tk.LEFT)
        self.label_temp = tk.Label(frame_label_temp, text="0", justify=tk.LEFT)
        self.label_temp.pack(side=tk.RIGHT)
        
        frame_label_ph = tk.Frame(frame_labels, width=200, height=100)
        frame_label_ph.pack()
        label_ph = tk.Label(frame_label_ph, text="pH:", justify=tk.LEFT)
        label_ph.pack(side=tk.LEFT)
        self.label_ph = tk.Label(frame_label_ph, text="0", justify=tk.LEFT)
        self.label_ph.pack(side=tk.RIGHT)
    
    
        ''' Call the gui_update function once, after set time has passed '''
        self.window_update = self.m.after(self.update_delay, 
                                          self.update_gui)
    
        ''' Set up window functions '''
        self.m.protocol("WM_DELETE_WINDOW", self.on_closing)
    
        ''' Start main loop (do this last) '''
        self.m.mainloop()
        
    def change_plot_source(self):
        print("Main: radio button " + str(self.selected_plot.get()) + " selected")
        self.should_update_spinbox = True
        
    def on_closing(self):
        #TODO: clear display and replace with "shutting down" message
        self.shut_down()
        
    def show_about(self):
        #this looks ugly, but multiline text takes tabs into account
        message_to_show = """text
across
multiple
lines"""
        self.messagebox = tk.messagebox.Message(self.m)
        self.messagebox.show(title="About", message=message_to_show)
        
    def set_setpoint(self):
        print("Main: Setting setpoint")
        self.should_update_setpoint = True
                
    def draw_plot(self):
        ''' Draw plot on canvas after getting latest x and y values'''
        if self.selected_plot.get() == 0:
            effector = self.heatercooler
        elif self.selected_plot.get() == 1:
            effector = self.phcontrol            
                    
        if(self.should_update_setpoint == True):
            newsetpoint = float(self.spinbox.get())
            print("Main: Setting setpoint to " + str(newsetpoint))
            effector.set_setpoint(newsetpoint)
            self.should_update_setpoint = False
        
        setpoint = effector.get_setpoint()        
        lowerRange = effector.lowerRange
        upperRange = effector.upperRange        
        lowerDomain = effector.lowerDomain
        upperDomain = effector.upperDomain
        
        self.spinbox.config(from_=lowerDomain, to=upperDomain)
        if(self.should_update_spinbox == True):
            self.spinbox.delete(0, 'end')
            self.spinbox.insert(0, setpoint)
            self.should_update_spinbox = False
        
        self.ax.clear()
        self.ax.plot(effector.get_x(),effector.get_y())
        self.ax.hlines(setpoint, lowerRange, upperRange, 'C1', 'dashed')
        
        plt.xlim(lowerRange,upperRange)
        plt.ylim(lowerDomain,upperDomain)
        self.ax.set_title(effector.get_title())
        self.ax.set_ylabel(effector.get_y_label())
        self.ax.set_xlabel("Time (s)")
        self.plot_canvas.draw_idle()
        
    def on_reset(self):
        self.heatercooler.reset()
        self.phcontrol.reset()
        
    def update_gui(self):
        ''' Update GUI, refreshing plots '''
        self.draw_plot()
        
        self.label_temp.config(text=str(round(self.heatercooler.get_current_value(), 3)))
        self.label_ph.config(text=str(round(self.phcontrol.get_current_value(), 1)))
        
        ''' Schedule update function again'''
        self.window_update = self.m.after(self.update_delay,
                                          self.update_gui)
    
    def update_reactor(self):     #grabs values from reactor, passes them to places. 
        self.thermocouple.set_sensor_value(self.reactor.get_temperature())
        #self.heatercooler.set_current_value(self.thermocouple.get_sensor_value())
        self.reactor.set_peltier_temp(self.heatercooler.get_current_value())

        self.phsensor.set_sensor_value(self.reactor.get_ph()) 
        #self.phcontrol.set_current_value(self.phsensor.get_sensor_value())
        self.reactor.set_ph_input(self.phcontrol.get_current_value())
    
    def main(self):
        '''
        Main loop starts threads for window and effectors
            then continually runs own update function
            Currently waiting 1 second between updates, to aid debugging
        '''
        self.running = True
        
        self.thread_handler.start_thread("heatercooler",
                                         self.heatercooler.start)
        self.thread_handler.start_thread("PHcontroler",
                                         self.phcontrol.start)
        self.thread_handler.start_thread("reactor",
                                         self.reactor.start)
        self.thread_handler.start_thread("window",
                                         self.start_drawing)
        
        
        while (self.running == True):
            time.sleep(1)   # Delay when polling, mainly for debugging
            #TODO: call main update function here
            self.update_reactor()
                    
        self.shutting_down = True
        while (self.shutting_down == True):
            ''' Check all other threaded processes have stopped '''
            if (self.heatercooler.get_running() == False and
                self.phcontrol.get_running() == False and
                self.reactor.get_running() == False):            
                self.shutting_down = False
        print("Main - Shutdown complete")

main = Main()
main.main()