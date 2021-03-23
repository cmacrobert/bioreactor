# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:42:50 2021

@author: Calum
"""

class ThreadHandler():
    
    def __init__(self, label, sleep_time):
        self.label = label
        self.sleep_time = sleep_time
        
    def start_thread(self):
        print("starting thread")