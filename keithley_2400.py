 # -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 22:18:28 2020

@author: Crow108
"""

import numpy as np
import pyvisa
rm = pyvisa.ResourceManager()

def ramp_from_prev_value(target_value_mA, step_size_mA=0.01):
    addr = 'GPIB20::25::INSTR'
    try:
        keithley = rm.open_resource(addr)            
        last_value_mA = float( keithley.query("sour:curr?") )*1000
        
        num_steps = int(np.floor( abs((last_value_mA - target_value_mA))/ (step_size_mA))) +1
        # arange excludes last point; so use linspace
        for val in np.linspace(last_value_mA, target_value_mA, num_steps):
            keithley.write(f"sour:curr {np.round(val*1E-3,6)}")
    finally:     
        keithley.close()            
        
def get_currrent_mA():
    addr = 'GPIB20::25::INSTR'
    try:
        keithley = rm.open_resource(addr)            
        last_value_mA = float( keithley.query("sour:curr?") )*1000
    finally:     
        keithley.close()       
    return last_value_mA