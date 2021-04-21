# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:42:50 2021

@author: Calum
"""

import threading

class ThreadHandler():
        
    def __init__(self):
        self.threads = []
        
    def start_thread(self, thread_name, thread_target):
        print("ThreadHandler: Starting thread: " + thread_name)
        new_thread = threading.Thread(name=thread_name, target=thread_target,
                                      daemon=False)  
        self.threads.append(new_thread)
        new_thread.start()
        
    def stop_threads(self):
        print("ThreadHandler: stopping threads")
        main_thread = threading.currentThread()
        for t in threading.enumerate():
            if t is main_thread:
                continue
            print("ThreadHandler: Joining thread " + t.getName())
            t.join(5)