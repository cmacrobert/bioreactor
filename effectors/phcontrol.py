# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 19:03:39 2021

@author: Nat
"""

#pH Control
#uses an instance of the PID to control pH


from pid_control import PIDControl
from reactor import reactor
import microcontroller
from base import EffectorBase
from sensors.phsensor import phsensor

