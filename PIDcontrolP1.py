# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 11:09:20 2021

@author: Stefan Olsson
"""
setPoint = float(0)

while True:
    command = input('>')
    if command == "set T SP":
        setPoint = float(input('set Temperature SetPoint >'))
    else:
        pass