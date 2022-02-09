# -*- coding: utf-8 -*-
"""
Created on Tues Feb 8 16:17:58 2022

@author: Shilling Du
@date: Feb 8, 2022
"""

import numpy as np
from datetime import datetime
import os
import pyvisa, time

rm = pyvisa.ResourceManager()

vna_gpib='GPIB20::20::INSTR'
data_dir = r"C:\Data\2022\SDCPW"

def wisform(smith):
    outarray = np.column_stack((smith.freqs,smith.log_mag,smith.phase_rad,smith.real,smith.imag))
    return outarray

power_list = [0]
del_time = [0.1]


while 1:
    time.sleep(60)
    vna_handle = rm.open_resource(vna_gpib)
    vna_handle.write(f"SOUR:POW {power_list[0]}")
    vna_handle.write("sens:aver 0"); 
    vna_handle.write("sens:AVER 1")
    vna_handle.close()
    
    print(f"Averaging for {del_time[0]} minutes")
    
    time.sleep(60*del_time[i])
    
    vs=get_smith_data(vna_gpib)
    
    outarray = wisform(vs)
    
    file_name = f"vna_{np.min(vs.freqs)/1E9:0.6f},{np.max(vs.freqs)/1E9:0.6f}.txt"
    os.makedirs(data_dir+'\\'+datetime.now().strftime('%Y%m%d'),exist_ok=True)
    np.savetxt(data_dir+'\\'+datetime.now().strftime('%Y%m%d')+"/"+file_name,outarray, delimiter='\t')
    