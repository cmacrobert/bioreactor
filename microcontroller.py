# -*- coding: utf-8 -*- 
""" 
Created on Fri Apr 30 02:05:15 2021 
 
@author: Nat 
""" 
 
# SPDX-FileCopyrightText: 2018 Tony DiCola for Adafruit Industries 
# SPDX-License-Identifier: MIT 

 # -*- coding: utf-8 -*- 
""" 
Created on Fri Apr 30 02:05:15 2021 
 
@author: Nat 
""" 
 
#python can be used to control a microcontoller's ouput voltage to a component using DAC.
#This code is for an Arduino or Raspberry Pi microcontroller using CircuitPython and 
# the MCP4725 component, which has the circuit python library bundle for the MCP4725
 
import board 
import busio 
import adafruit_mcp4725 


i2c = busio.I2C(board.SCL, board.SDA) # Initialize I2C bus. 

dac = adafruit_mcp4725.MCP4725(i2c) # Initialize MCP4725. # Create a DAC instance.  #Using i2c 

#set the DAC output using: 
dac.raw_value = 4095  # The raw_value property to directly reads and writes 
# to the 12-bit DAC value.   

#takes an incoming peltier temperature value and converts it to the 12 bit DAC 
#value between # 0 (minimum/ground) to 4095 (maximum/Vout), which 
#corresponds to a Vout pin voltage between 0-3.3V. A heating range of 35 deg
#is used here https://www.cuidevices.com/product/resource/cp18-m.pdf 

class microcontoller():
    def __init__ (self):
        EffectorBase.__init__(self, "microcontroller")
        self.temperature = temperature
        self.set_peltier_temp = temperature
        
    def set_peltier_voltage(self, value=0):   
        (self.set_peltier_temp()/35)*4096 = value
        dac.write(value)
        value += 1
        value %= 4096
        
        