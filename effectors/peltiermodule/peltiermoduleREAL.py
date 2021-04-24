# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 16:37:34 2021

@author: Nat
"""
#peltier module second try
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

    

        
        
        

# -*- coding: utf-8 -*-
#from effectors.base import heatercooler DO NOT NEED TO DO THIS need to attach peltier to reactor and heatercooler

class peltiermoduleTREAL(): #inherited from 0 classes
    def __init__(self, reactor,): #reactor is passed in
        self.reactor = reactor # so it knows what reactor it is attached to
        #does not need to know which thermocouple it is attached to
        self.voltage = 0   #default should be 0
        #self.temperature = reactor.gettemperature() #default temp of peltier is the same as that of the reactor
                                                    #its a physical property.
        self.heatercooler = heatercooler                                            
                                                    
    def setvoltage(self, voltage): 
        self.voltage = voltage
        
    def time_step_forward():    #needs to apply to every step, each cycle
        pass                    #its not finished!
    
    #needs to convert the PID temp target to 
    #a useable voltage within the module
    


