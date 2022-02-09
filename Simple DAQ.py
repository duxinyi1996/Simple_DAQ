# -*- coding: utf-8 -*-
"""
Created on Tues Feb 8 16:17:58 2022

@author: Shilling Du
@date: Feb 8, 2022
"""

import numpy as np
from datetime import datetime
import time, sys, os, pyvisa

folder_path = os.getcwd()
if folder_path not in sys.path:
    sys.path.append(folder_path)
from vna_analysis import get_smith_data
from SR830 import SR830_get_x, SR830_get_y

rm = pyvisa.ResourceManager()

vna_gpib = 'GPIB20::20::INSTR'
SR830_gpib = ""
data_dir = r"C:\Data\2022\SDCPW"


def my_form(smith, constant1, constant2):
    data = np.column_stack((smith.freqs, smith.log_mag, smith.phase_rad, smith.real, smith.imag,
                             np.full(len(smith.freqs), constant1), np.full(len(smith.freqs), constant2)))

    return data


power_list = [0]
del_time = [0.1]

while True:
    time.sleep(60)
    vna_handle = rm.open_resource(vna_gpib)
    vna_handle.write(f"SOUR:POW {power_list[0]}")
    vna_handle.write("sens:aver 0")
    vna_handle.write("sens:AVER 1")
    vna_handle.close()
    # print (f"Averaging for {del_time[0]} minutes")
    time.sleep(60 * del_time[0])

    vs = get_smith_data(vna_gpib)
    x = SR830_get_x(SR830_gpib)
    y = SR830_get_y(SR830_gpib)

    data = my_form(vs, x, y)

    file_name = f"vna_{np.min(vs.freqs) / 1E9:0.6f},{np.max(vs.freqs) / 1E9:0.6f}.txt"
    os.makedirs(data_dir + '\\' + datetime.now().strftime('%Y%m%d'), exist_ok=True)
    np.savetxt(data_dir + '\\' + datetime.now().strftime('%Y%m%d') + "/" + file_name, data, delimiter='\t')
