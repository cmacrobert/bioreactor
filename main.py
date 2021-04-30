# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:59:25 2021

@author: Calum
"""
import thread_handler
import time
import effectors.temperaturecontrol as TC
import effectors.phcontrol as PHC
import effectors.pressurecontrol as PC
import effectors.CO2control as CC
import sensors.thermocouple as TCS
import sensors.phsensor as PHS
import sensors.pressuresensor as PS
import sensors.co2sensor as CS
import reactor
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Main():
    
    def __init__(self):
        self.thread_handler = thread_handler.ThreadHandler()
        self.temperature_control = TC.TemperatureControl()
        self.ph_control = PHC.PHControl()
        self.pressure_control = PC.PressureControl()
        self.co2_control = CC.Co2Control()
        self.reactor = reactor.reactor()        
        self.thermocouple = TCS.thermocouple()
        self.phsensor = PHS.phsensor()
        self.pressure_sensor = PS.SensorPressure()
        self.co2_sensor = CS.SensorCo2()
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
        self.temperature_control.stop()
        self.ph_control.stop()
        self.pressure_control.stop()
        self.co2_control.stop()
        self.reactor.stop()        
        self.thread_handler.stop_threads()
        self.running = False
        self.m.quit()
    
    def start_drawing(self):
        ''' Root '''
        self.m = tk.Tk(className='Bioreactor Simulator')
        self.m.title("Bioreactor Simulator")
        self.m.geometry("800x600")
        self.m['background']='white'
                
        ''' Menu '''
        self.menu = tk.Menu(self.m)
        self.m.config(menu=self.menu)
        ''' File - Reset and Exit'''
        self.menu_file = tk.Menu(self.menu)
        self.menu.add_cascade(label='File', menu=self.menu_file)
        self.menu_file.add_command(label='Reset', command=self.on_reset)
        self.menu_file.add_separator()
        self.menu_file.add_command(label='Exit', command=self.on_closing)
        ''' Help - About'''
        self.menu_help = tk.Menu(self.menu)
        self.menu.add_cascade(label='Help', menu=self.menu_help)
        self.menu_help.add_command(label='About', command=self.show_about)        
               
        ''' Canvas, used for drawing matplotlib plot '''
        canvas = tk.Canvas(self.m,
                           width=800, height=600)
        canvas.pack(side=tk.LEFT)        
        ''' Matplotlib plot '''        
        figure = plt.figure(figsize=(6,5), dpi=100)
        self.ax = figure.add_subplot(111)
        self.plot_canvas = FigureCanvasTkAgg(figure, master=canvas)
        self.plot_canvas.get_tk_widget().pack()
        
        ''' Controls frame, contains three sections:
            Setpoint control - Allows PID setpoints to be changed
            Effector selection - Allows plotted effector to be changed
            Labels for current values - Display current values from PIDs'''
        frame_controls = tk.Frame(self.m,
                                  width=200, height=200)
        frame_controls.pack(side=tk.RIGHT)   
        
        ''' Setpoint control '''
        frame_setpoint = tk.Frame(frame_controls,
                                  width=200, height=200)
        frame_setpoint.pack(pady=20)    
        lbl_setpoint = tk.Label(frame_setpoint, text="Setpoint:")
        lbl_setpoint.pack()
        self.spbx_setpoint = tk.Spinbox(frame_setpoint)
        self.spbx_setpoint.pack(side=tk.LEFT)
        btn_setpoint = tk.Button(frame_setpoint, text='Update',
                                 command=self.on_setpoint_changed)
        btn_setpoint.pack(side=tk.RIGHT)
        
        ''' Effector selection '''
        frame_plot_select = tk.Frame(frame_controls,
                                     width=200, height=200)
        frame_plot_select.pack(pady=20)        
        lbl_plot_select = tk.Label(frame_plot_select, text="Plot Shown:",
                                   justify=tk.LEFT)
        lbl_plot_select.pack()
        self.selected_plot = tk.IntVar(self.m)
        radbtn_temp = tk.Radiobutton(frame_plot_select, text="Temperature",
                                     variable=self.selected_plot, value=0,
                                     command=self.on_plot_source_changed,
                                     width=100, indicatoron=0)
        radbtn_temp.pack()
        radbtn_ph = tk.Radiobutton(frame_plot_select, text="pH",
                                   variable=self.selected_plot, value=1,
                                   command=self.on_plot_source_changed,
                                   width=100, indicatoron=0)
        radbtn_ph.pack()
        radbtn_pressure = tk.Radiobutton(frame_plot_select, text="Pressure",
                                   variable=self.selected_plot, value=2,
                                   command=self.on_plot_source_changed,
                                   width=100, indicatoron=0)
        radbtn_pressure.pack()
        radbtn_co2 = tk.Radiobutton(frame_plot_select, text="CO2",
                                   variable=self.selected_plot, value=3,
                                   command=self.on_plot_source_changed,
                                   width=100, indicatoron=0)
        radbtn_co2.pack()
        
        ''' Labels for current values '''     
        frame_curr_vals = tk.Frame(frame_controls,
                                   width=200, height=200)
        frame_curr_vals.pack(pady=20)
        ''' Label - Temperature '''        
        frame_lbl_temp = tk.Frame(frame_curr_vals,
                                  width=200, height=100)
        frame_lbl_temp.pack()
        label_temp = tk.Label(frame_lbl_temp,
                              text="Temperature (\xb0C):", justify=tk.LEFT)
        label_temp.pack(side=tk.LEFT)
        self.lbl_temp = tk.Label(frame_lbl_temp,
                                 text="0", justify=tk.LEFT)
        self.lbl_temp.pack(side=tk.RIGHT)
        ''' Label - pH '''
        frame_lbl_ph = tk.Frame(frame_curr_vals,
                                width=200, height=100)
        frame_lbl_ph.pack()
        lbl_ph = tk.Label(frame_lbl_ph,
                          text="pH:", justify=tk.LEFT)
        lbl_ph.pack(side=tk.LEFT)
        self.lbl_ph = tk.Label(frame_lbl_ph,
                               text="0", justify=tk.LEFT)
        self.lbl_ph.pack(side=tk.RIGHT)
        ''' Label - Pressure '''
        frame_lbl_pressure = tk.Frame(frame_curr_vals,
                                width=200, height=100)
        frame_lbl_pressure.pack()
        lbl_pressure = tk.Label(frame_lbl_pressure,
                          text="Pressure (bar):", justify=tk.LEFT)
        lbl_pressure.pack(side=tk.LEFT)
        self.lbl_pressure = tk.Label(frame_lbl_pressure,
                               text="0", justify=tk.LEFT)
        self.lbl_pressure.pack(side=tk.RIGHT)
        ''' Label - CO2 '''
        frame_lbl_co2 = tk.Frame(frame_curr_vals,
                                width=200, height=100)
        frame_lbl_co2.pack()
        lbl_co2 = tk.Label(frame_lbl_co2,
                          text="CO2 (%):", justify=tk.LEFT)
        lbl_co2.pack(side=tk.LEFT)
        self.lbl_co2 = tk.Label(frame_lbl_co2,
                               text="0", justify=tk.LEFT)
        self.lbl_co2.pack(side=tk.RIGHT)
    
        ''' Call the gui_update function once, after set time has passed '''
        self.window_update = self.m.after(self.update_delay, 
                                          self.update_gui)
    
        ''' Set up window functions '''
        self.m.protocol("WM_DELETE_WINDOW", self.on_closing)
    
        ''' Start main loop (do this last) '''
        self.m.mainloop()
        
    def on_plot_source_changed(self):
        ''' When changing the plot source, schedule spinbox to be updated '''
        self.should_update_spinbox = True
        
    def on_setpoint_changed(self):
        ''' When changing setpoint, schedule update for draw call '''
        self.should_update_setpoint = True
        
    def on_reset(self):
        ''' When reset uption is selcted, reset effectors '''
        self.temperature_control.reset()
        self.ph_control.reset()
        self.pressure_control.reset()
        self.co2_control.reset()
        
    def on_closing(self):
        #TODO: clear display and replace with "shutting down" message
        self.shut_down()
        
    def show_about(self):
        message_to_show = """Credits:
Calum MacRobert
Mirrin Gillespie
Natasha Sutherland
Stefan Olsson"""
        self.msgbx_about = tk.messagebox.Message(self.m)
        self.msgbx_about.show(title="About", message=message_to_show)
                        
    def draw_plot(self):
        ''' Draw selected plot on canvas from latest effector values'''
        if self.selected_plot.get() == 0:
            effector = self.temperature_control
        elif self.selected_plot.get() == 1:
            effector = self.ph_control      
        elif self.selected_plot.get() == 2:
            effector = self.pressure_control 
        elif self.selected_plot.get() == 3:
            effector = self.co2_control 
                    
        if(self.should_update_setpoint == True):
            new_setpoint = float(self.spbx_setpoint.get())
            if(new_setpoint <= effector.upper_range and
               new_setpoint >= effector.lower_range):
                effector.set_setpoint(new_setpoint)
                self.spbx_setpoint.config(background="White")
            else:
                self.spbx_setpoint.config(background="Red")
            self.should_update_setpoint = False
        
        setpoint = effector.get_setpoint()        
        lower_range = effector.lower_range
        upper_range = effector.upper_range        
        lower_domain = effector.lower_domain
        upper_domain = effector.upper_domain
        
        self.spbx_setpoint.config(from_=lower_range, to=upper_range)
        if(self.should_update_spinbox == True):
            self.spbx_setpoint.delete(0, 'end')
            self.spbx_setpoint.insert(0, setpoint)
            self.should_update_spinbox = False
        
        self.ax.clear()
        self.ax.plot(effector.get_x(),effector.get_y())
        self.ax.hlines(setpoint, lower_domain, upper_domain, 'C1', 'dashed')
        
        plt.xlim(lower_domain, upper_domain)
        plt.ylim(lower_range, upper_range)
        self.ax.set_title(effector.get_title())
        self.ax.set_ylabel(effector.get_y_label())
        self.ax.set_xlabel("Time (s)")
        self.plot_canvas.draw_idle()
                
    def update_gui(self):
        ''' Update GUI, refreshing plots '''
        self.draw_plot()
        
        self.lbl_temp.config(text=str(round(self.temperature_control.get_current_value(), 3)))
        self.lbl_ph.config(text=str(round(self.ph_control.get_current_value(), 1)))
        self.lbl_pressure.config(text=str(round(self.pressure_control.get_current_value(), 1)))
        self.lbl_co2.config(text=str(round(self.co2_control.get_current_value(), 1)))
        
        ''' Schedule update function again'''
        self.window_update = self.m.after(self.update_delay,
                                          self.update_gui)
    
    def update_reactor(self):
        ''' Grabs values from reactor, passes them to places '''
        self.thermocouple.set_sensor_value(self.reactor.get_temperature())
        #self.temperature_control.set_current_value(self.thermocouple.get_sensor_value())
        self.reactor.set_peltier_temp(self.temperature_control.get_current_value())

        self.phsensor.set_sensor_value(self.reactor.get_ph()) 
        #self.ph_control.set_current_value(self.phsensor.get_sensor_value())
        self.reactor.set_ph_input(self.ph_control.get_current_value())
        
        self.pressure_sensor.set_sensor_value(self.reactor.get_pressure()) 
        #self.pressure_control.set_current_value(self.pressure_sensor.get_sensor_value())
        self.reactor.set_pressure_input(self.pressure_control.get_current_value())
        
        self.co2_sensor.set_sensor_value(self.reactor.get_co2()) 
        #self.co2_control.set_current_value(self.co2_sensor.get_sensor_value())
        self.reactor.set_co2_input(self.co2_control.get_current_value())
    
    def main(self):
        '''
        Main loop starts threads for window and effectors
            then continually runs own update function
            Currently waiting 1 second between updates, to aid debugging
        '''
        self.running = True
        
        self.thread_handler.start_thread("temperaturecontrol",
                                         self.temperature_control.start)
        self.thread_handler.start_thread("PHcontroler",
                                         self.ph_control.start)
        self.thread_handler.start_thread("PressureControler",
                                         self.pressure_control.start)
        self.thread_handler.start_thread("CO2 Controler",
                                         self.co2_control.start)
        self.thread_handler.start_thread("reactor",
                                         self.reactor.start)
        self.thread_handler.start_thread("window",
                                         self.start_drawing)
        
        
        while (self.running == True):
            time.sleep(1)   # Delay when polling, mainly for debugging
            self.update_reactor()
                    
        self.shutting_down = True
        while (self.shutting_down == True):
            ''' Check all other threaded processes have stopped '''
            if (self.temperature_control.get_running() == False and
                self.ph_control.get_running() == False and
                self.pressure_control.get_running() == False and
                self.co2_control.get_running() == False and
                self.reactor.get_running() == False):            
                self.shutting_down = False
        print("Main - Shutdown complete")

main = Main()
main.main()