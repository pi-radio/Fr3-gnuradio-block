#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2026 Pi-Radio.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

import pmt
import serial
import numpy
from gnuradio import gr

class Octolo(gr.basic_block):
    def __init__(self, freqlo, freqlodrive, serialports):

        gr.sync_block.__init__(self,
            name="Octolo",
            in_sig=None,
            out_sig=None
        )
        self.lo = freqlo
        self.lodrive = freqlodrive
        self.lomes = 0
        self.lodrivemes = 0
        self.serials = serialports
        self.ser = serial.Serial(port=f"{self.serials}", baudrate=115200, timeout=1)

        #self.serialport = serial.serial(serials)
        
        lomes_port_id = pmt.intern("freq_lo")
        lodrivemes_port_id = pmt.intern("freq_lodrive")
    

        self.message_port_register_in(lomes_port_id)
        self.message_port_register_in(lodrivemes_port_id)
        
        self.set_msg_handler(lomes_port_id, self._handle_msg_lomes)
        self.set_msg_handler(lodrivemes_port_id, self._handle_msg_lodrivemes)
       

        self.set_lo(self.lo, self.lomes)
        self.set_lodrive(self.lodrive, self.lodrivemes)


        
    def _handle_msg_lomes(self, msg):
        if pmt.is_real(msg):
            self.lomes = pmt.to_python(msg)
            print(f"freqency: {self.lomes}")
            self.set_lo(self.lo, self.lomes)
        else:
            print("Error: RF freqency is not between 6.0-22.6.")
               
    def _handle_msg_lodrivemes(self, msg):
        if pmt.is_real(msg):
            self.lodrivemes = pmt.to_python(msg)
            print(f"Drive level: {self.lodrivemes}")
            self.set_lodrive(self.lodrive, self.lodrivemes)
        else:
            print("Error:Lo drive level not between 1-7.")
      
   
   
    def set_lo(self, lo, lomes=0):
        self.loSET = lo
        self.lomess = lomes
        if self.lomess >  0:
            command = f"\nlmx tune {self.lomes}\n"
            self.ser.write(command.encode('utf-8'))
            print(command)
        else:
            command = f"\nlmx tune {self.loSET}\n"
            self.ser.write(command.encode('utf-8'))
            print(command)
        


            
    def set_lodrive(self, lodrive, lodrivemes=0):
        self.lodrive = lodrive
        self.lodrivemess = lodrivemes
        if self.lodrivemes > 0:
            command = f"\nlmx drive {self.lodrivemes}\n"
            self.ser.write(command.encode('utf-8'))
            print(command)
        else:
            command = f"\nlmx drive {self.lodrive}\n"
            self.ser.write(command.encode('utf-8'))
            print(command)
          
       
    def stop(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
        return True
