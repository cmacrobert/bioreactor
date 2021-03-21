# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:19:29 2021

@author: Calum
"""

from sensors.temperature import SensorTemperature
from threadtest import ThreadTest
import time

new_threadtest = ThreadTest("5 second test", 5);

def main():   
    print("Starting main()")
    new_threadtest.start_thread()
    
    while True:
        print("Main thread - Waiting 1 second")
        time.sleep(1)

main()