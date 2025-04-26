#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2025 Pi-Radio.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

import numpy as np
import urllib.request
import pmt
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
        self.freqmes = 0
        self.lowfreqmes = 0
        self.RX_gainmes = 0
        self.RX1_gainmes = 0
        self.TX_gainmes = 0
        self.TX1_gainmes = 0


        freqmes_port_id = pmt.intern("freqmes")
        lowfreqmes_port_id = pmt.intern("lowfreqmes")
        rx_gainmes_port_id = pmt.intern("RX_gainmes")
        rx1_gainmes_port_id = pmt.intern("RX1_gainmes")
        tx_gainmes_port_id = pmt.intern("TX_gainmes")
        tx1_gainmes_port_id = pmt.intern("TX1_gainmes")
        

        self.message_port_register_in(freqmes_port_id)
        self.message_port_register_in(lowfreqmes_port_id)
        self.message_port_register_in(rx_gainmes_port_id)
        self.message_port_register_in(rx1_gainmes_port_id)
        self.message_port_register_in(tx_gainmes_port_id)
        self.message_port_register_in(tx1_gainmes_port_id)
        
        self.set_msg_handler(freqmes_port_id, self._handle_msg_freqmes)
        self.set_msg_handler(lowfreqmes_port_id, self._handle_msg_lowfreqmes)
        self.set_msg_handler(rx_gainmes_port_id, self._handle_msg_RX_gainmes)
        self.set_msg_handler(rx1_gainmes_port_id, self._handle_msg_RX1_gainmes)
        self.set_msg_handler(tx_gainmes_port_id, self._handle_msg_TX_gainmes)
        self.set_msg_handler(tx1_gainmes_port_id, self._handle_msg_TX1_gainmes)




        self.set_high_lo(freq, self.freqmes)
        self.set_low_lo(freq2, self.lowfreqmes)
        self.set_gain1(gain1, self.RX_gainmes)
        self.set_gain2(gain2, self.RX1_gainmes)
        self.set_gain3(gain3, self.TX_gainmes)
        self.set_gain4(gain4, self.TX1_gainmes)

    def _handle_msg_freqmes(self, msg):
        if pmt.is_real(msg):
            self.freqmes = pmt.to_python(msg)
            print(f"Received freqmes message: {self.freqmes}")
            self.set_high_lo(self._highlo, self.freqmes)
        else:
            print("Error: freqmes message is not an number.")
            
    def _handle_msg_lowfreqmes(self, msg):
        if pmt.is_real(msg):
            self.lowfreqmes = pmt.to_python(msg)
            print(f"Received lowfreqmes message: {self.lowfreqmes}")
            self.set_low_lo(self._lowlo, self.lowfreqmes)
        else:
            print("Error: lowfreqmes message is not an number.")


    def _handle_msg_RX_gainmes(self, msg):

        if pmt.is_real(msg):
            self.RXmes = pmt.to_python(msg)
            print(f"Received RX gain message: {self.RXmes}")
            self.set_gain1(self._rx1gain, self.RXmes) 
        else:
            print("Error: RX_gainmes message is not a float.")
        
    def _handle_msg_RX1_gainmes(self, msg):

        if pmt.is_real(msg):
            self.RX1mes = pmt.to_python(msg)
            print(f"Received RX gain message: {self.RX1mes}")
            self.set_gain2(self._rx2gain, self.RX1mes) 
        else:
            print("Error: RX1_gainmes message is not a float.")


    def _handle_msg_TX_gainmes(self, msg):

        if pmt.is_real(msg):
            self.TXmes = pmt.to_python(msg)
            print(f"Received TX gain message: {self.TXmes}")
            self.set_gain3(self._tx1gain, self.TXmes)
        else:
            print("Error: TX_gainmes message is not a float")
     
    def _handle_msg_TX1_gainmes(self, msg):

        if pmt.is_real(msg):
            self.TX1mes = pmt.to_python(msg)
            print(f"Received TX gain message: {self.TX1mes}")
            self.set_gain4(self._tx2gain, self.TX1mes) 
        else:
            print("Error: TX1_gainmes message is not a float")
      
        
    
    def set_high_lo(self, freq, freqmes):
        self._highlo = freq
        self.mes_high_lo = freqmes
        if freqmes > 0:
            freqhi = freqmes
            url = f"http://{self.ip_address}:5111/high_lo?freq={freqhi}"
            response = urllib.request.urlopen(url)
            url1 = response.read().decode('utf-8')
            print(url1)
        else:
             freqhi = self._highlo
             url = f"http://{self.ip_address}:5111/high_lo?freq={freqhi}"
             response = urllib.request.urlopen(url)
             url1 = response.read().decode('utf-8')
             print(url1)
    
    def set_low_lo(self, freq2, lowfreqmes):
        self._lowlo = freq2
        self.mes_low_lo = lowfreqmes
        if lowfreqmes > 0:
            freq21 = lowfreqmes
            ur2 = f"http://{self.ip_address}:5111/low_lo?freq={freq21}"
            response = urllib.request.urlopen(ur2)
            url2 = response.read().decode('utf-8')
            print(url2)  
        else:
            freq21 = freq2 
            ur2 = f"http://{self.ip_address}:5111/low_lo?freq={freq21}"
            response = urllib.request.urlopen(ur2)
            url2 = response.read().decode('utf-8')
            print(url2)  
            
    def set_gain1(self, gain1, RX_gainmes):
        self._rx1gain = gain1
        self._RX_gainmes = RX_gainmes
        if RX_gainmes > 0:
            gainrx = RX_gainmes
            url = f"http://{self.ip_address}:5111/gain?trx=rx&chan=0&v={gainrx}"
            response = urllib.request.urlopen(url)
            url1 = response.read().decode('utf-8')
            print(url1)
        else:
            gainrx = gain1
            url = f"http://{self.ip_address}:5111/gain?trx=rx&chan=0&v={gainrx}"
            response = urllib.request.urlopen(url)
            url1 = response.read().decode('utf-8')
            print(url1)

    
    def set_gain2(self, gain2, RX1_gainmes):
        self._rx2gain = gain2
        self.RX1_gainmes = RX1_gainmes
        if RX1_gainmes > 0:
            gainrx1 = RX_gainmes
            ur4 = f"http://{self.ip_address}:5111/gain?trx=rx&chan=1&v={gainrx1}"
            response = urllib.request.urlopen(ur4)
        else:
            gainrx1 = gain2
            ur4 = f"http://{self.ip_address}:5111/gain?trx=rx&chan=0&v={gainrx1}"
            response = urllib.request.urlopen(ur4)
            
    
    def set_gain3(self, gain3, TX_gainmes):
        self._txgain = gain3
        self.TX_gainmes = TX_gainmes
        if TX_gainmes > 0:
            gaintx = TX_gainmes
            ur5 = f"http://{self.ip_address}:5111/gain?trx=tx&chan=0&v={gaintx}"
            response = urllib.request.urlopen(ur5)
        else:
            gaintx = gain3
            ur5 = f"http://{self.ip_address}:5111/gain?trx=rx&chan=0&v={gaintx}"
            response = urllib.request.urlopen(ur5)
            


    
    def set_gain4(self, gain4, TX1_gainmes):
        self._tx2gain = gain4
        self.TX1gainmes = TX1_gainmes
        if TX1_gainmes > 0:
            gaintx1 = TX_gainmes
            ur6 = f"http://{self.ip_address}:5111/gain?trx=tx&chan=1&v={gaintx1}"
            response = urllib.request.urlopen(ur6)
            url6 = response.read().decode('utf-8')
            print(url6)
        else:
            gaintx1 = gain4
            ur6 = f"http://{self.ip_address}:5111/gain?trx=rx&chan=0&v={gaintx1}"
            response = urllib.request.urlopen(ur6)
            url6 = response.read().decode('utf-8')
            print(url6)


    def work(self, input_items, output_items):
        return 0
