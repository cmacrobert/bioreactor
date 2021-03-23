# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:12:01 2021

@author: Calum
"""

from enum import Enum

class InputReturns(Enum):
    NONE = 1
    PID_SET_SETPOINT = 2
    PID_SET_START = 3
    PID_RESET = 4
    GET_TEMPERATURE = 5
    SET_TEMPERATURE = 6
    RESET_TEMPERATURE = 7
    SHUT_DOWN = 8