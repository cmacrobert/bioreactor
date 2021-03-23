# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:12:01 2021

@author: Calum
"""

from enum import Enum

class InputReturns(Enum):
    NONE = 1
    SET_SETPOINT = 2
    GET_TEMPERATURE = 3
    SET_TEMPERATURE = 4
    RESET_TEMPERATURE = 5
    SHUT_DOWN = 6