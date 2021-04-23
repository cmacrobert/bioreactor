# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 00:09:15 2021

@author: Nat
"""

#Microcontroller

#The real-life microcontroller carries within it a C file which 
#converts the value to a voltage. It takes this value and using it's C code, 
#runs the petier module at the equivalent voltage to give precise and 
#variable heating to the peltier module. 
#this C program has not been written or" flashed" onto a microcontroller at this 
#stage as im getting the discting impression we are not supposed to use hardware
#this means a functional program cannot be written in the python code to 
#accomodate the microchip as this requires back and forth communication. 

#this program here, just uses python code to shortcut what the microcontroller 
#would do, by providing a code which essentially does the same thing. 

#takes voltage target output from the PID, and converts it to a voltage. 

#however, we can simply bypass this stage if both the PID output and the
#reactor both use a temperated based control system. 

#the peltier module and the thermocouple's microcontrollor communication
#functions, should both come into play when the simulated reactor is chosen 
#not to be run. 

#below is some work based on communicating with a microcontroller, 
#which cannot be completed at this time.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
Created on Thu Apr 22 16:37:34 2021

@author: Nat
"""
#work is based on this tutorial and setup:
#https://maker.pro/pic/tutorial/introduction-to-python-serial-ports
#          USE COM PORT 4 !!!

#pip install PySerial -need to have PySerial to run this. 

#below configures the PySerial Parametersand imports the serial module
#THESE ARE instructions on how to pass commands to the microcontoller

import serial

serialPort = serial.Serial(port = "COM4", baudrate=115200,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)


        
serialString = ""                           # Used to hold data coming over UART


#below this only works if connected to a real microcontroller 
# while(1):

#     # Wait until there is data waiting in the serial buffer
#     if(serialPort.in_waiting > 0):

#         # Read data out of the buffer until a carraige return / new line is found
#         serialString = serialPort.readline()

#         # Print the contents of the serial data
#         print(serialString.decode('Ascii'))

#         # Tell the device connected over the serial port that we recevied the data!
#         # The b at the beginning is used to indicate bytes!
#         serialPort.write(b"Thank you for sending data \r\n")
        
        
// CONFIG1
#pragma config FOSC = INTOSC pin)
#pragma config WDTE = OFF       
#pragma config PWRTE = OFF      
#pragma config MCLRE = ON       
#pragma config CP = OFF        
#pragma config CPD = OFF        
#pragma config BOREN = OFF      
#pragma config CLKOUTEN = OFF   
#pragma config IESO = 
#pragma config FCMEN = ON       

// CONFIG2
#pragma config WRT = OFF        
#pragma config PLLEN = OFF      
#pragma config STVREN = ON      
#pragma config BORV = LO       
#pragma config LVP = ON

       
void main(void)
{
    // Configure pins as digital
    ANSELA = 0;
    ANSELC = 0;
    
    OSCCONbits.IRCF = 0b1110;

    configUART();
    
    while(1)
    {
        sendStringUART("Hello, this is the PIC16F1825");
        readStringUART(stringBuffer); 
    }
}


       
void configUART(void);
void sendByteUART(char data);
void sendStringUART(const char *string);
void readStringUART(char *buffer);

    