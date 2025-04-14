#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2025 Pi-Radio.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

import numpy as np
import urllib.request
from gnuradio import gr
from gnuradio import blocks

class FR3(gr.sync_block):
    
    def __init__(self, freq, freq2, gain1, gain2, gain3, gain4, ip_address="0.0.0.0"):
        gr.sync_block.__init__(
            self,
            name='FR3',
            in_sig=None,
            out_sig=None
        )
        self.ip_address = ip_address
        
        self._highlo = freq
        self._lowlo = freq2
        self._rx1gain = gain1
        self._rx2gain = gain2
        self._tx1gain = gain3
        self._tx2gain = gain4
        
        self.set_high_lo(freq)
        self.set_low_lo(freq2)
        self.set_gain1(gain1)
        self.set_gain2(gain2)
        self.set_gain3(gain3)
        self.set_gain4(gain4)
    
    def set_high_lo(self, freq):
        self._highlo = freq
        url = f"http://{self.ip_address}:5111/high_lo?freq={freq}"
        response = urllib.request.urlopen(url)
        url1 = response.read().decode('utf-8')
        print(url1)
    
    def set_low_lo(self, freq):
        self._lowlo = freq
        ur2 = f"http://{self.ip_address}:5111/low_lo?freq={freq}"
        response = urllib.request.urlopen(ur2)
        url2 = response.read().decode('utf-8')
    
    def set_gain1(self, gain):
        self._rx1gain = gain
        url = f"http://{self.ip_address}:5111/gain?trx=rx&chan=0&v={gain}"
        response = urllib.request.urlopen(url)
        url1 = response.read().decode('utf-8')
        print(url1)
       
    def set_gain2(self, gain):
        self._rx2gain = gain
        ur4 = f"http://{self.ip_address}:5111/gain?trx=rx&chan=1&v={gain}"
        response = urllib.request.urlopen(ur4)
    
    def set_gain3(self, gain):
        self._tx1gain = gain
        ur5 = f"http://{self.ip_address}:5111/gain?trx=tx&chan=0&v={gain}"
        response = urllib.request.urlopen(ur5)
    
    def set_gain4(self, gain):
        self._tx2gain = gain
        ur6 = f"http://{self.ip_address}:5111/gain?trx=tx&chan=1&v={gain}"
        response = urllib.request.urlopen(ur6)
        url6 = response.read().decode('utf-8')
        print(url6)

    def work(self, input_items, output_items):
        return 0
