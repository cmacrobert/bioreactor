# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 09:28:24 2021

@author: Calum
"""

import threading
import time
import PIDcontrol
import concurrent.futures
import logging

class ThreadTest():
    
    def __init__(self, label, sleep_time):
        self.label = label
        self.sleep_time = sleep_time
        
    def oneshot_thread(self)   :        
        print('Starting thread: ' + self.label + ' ')
        print('Waiting for ' + str(self.sleep_time) + ' seconds')
        time.sleep(self.sleep_time)
        print('Done with thread: ' + self.label + ' ')
        
    def looping_thread(self):
        print('Starting looping thread ' + self.label)
        
        PIDcontrol.PID(0.05,0.05,0.05,37)
        
        '''
        running = True
        while running == True:
            time.sleep(self.sleep_time)
            print(str(self.sleep_time) + ' seconds passed in thread')
            if input() == "quit":
                print('Quitting thread')
                running = False
        '''
                  
    def start_thread(self):
        print('starting thread')
        #thread = threading.Thread(target=self.oneshot_thread, daemon=True)   
        thread = threading.Thread(target=self.looping_thread, daemon=True)  
        thread.start()      
        
    #TODO: make sure threads are closed properly, especially when using loops
    
    def start_thread_pool(self):
        print('Starting thread pool')
        #format = "%(asctime)s: %(message)s"
        #logging.basicConfig(format=format, level=logging.INFO,
        #                    datefmt="%H:%M:%S")
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            executor.map(self.looping_thread, range(3))