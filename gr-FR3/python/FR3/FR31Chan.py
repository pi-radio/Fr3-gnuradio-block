#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2026 PI-Radio.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
import pmt
import serial
import numpy
from gnuradio import gr

class FR31Chan(gr.sync_block):

   def __init__(self, freqRF, freqIF, RXgain, TXgain):

        gr.sync_block.__init__(self,
            name="FR31Chan",
            in_sig=None,
            out_sig=None
        )
        self._RF = freqRF
        self._IF = freqIF
        self._RX = RXgain
        self._TX = TXgain
        self.RFMES = 0
        self.IFMES = 0
        self.RXMES = 0
        self.TXMES = 0

        
        #RFMES_port_id = pmt.intern("RF")
        #IFMES_port_id = pmt.intern("IF")
        #RXMES_port_id = pmt.intern("RX")
        #TXMES_port_id = pmt.intern("TX")
        

        #self.message_port_register_in(RFMES_port_id)
        #self.message_port_register_in(IFMES_port_id)
        #self.message_port_register_in(RXMES_port_id)
        #self.message_port_register_in(TXMES_port_id)
        #self.set_msg_handler(RFMES_port_id, self._handle_msg_RF)
        #self.set_msg_handler(IFMES_port_id, self._handle_msg_IF)
        #self.set_msg_handler(RXMES_port_id, self._handle_msg_RXgain)
        #self.set_msg_handler(TXMES_port_id, self._handle_msg_TXgain)


        self.set_RF(self._RX, self.RFMES)
        self.set_IF(self._IF, self.IFMES)
        self.set_RX(self._RX, self.RXMES)
        self.set_TX(self._TX, self.TXMES)


        
        def _handle_msg_RF(self, msg):
            if pmt.is_real(msg):
                self.RFMES = pmt.to_python(msg)
                print(f"freqency: {self.RFMES}")
                self.set_RF(self._RF, self.RFMES)
            else:
                print("Error: RF freqency is not between 6e9-22e9.")
               
        def _handle_msg_IF(self, msg):
            if pmt.is_real(msg):
                self.IFMES = pmt.to_python(msg)
                print(f"IF freqency: {self.IFMES}")
                self.set_IF(self._IF, self.IFMES)
            else:
                print("Error: IF freqency is not between 4e8-1.8e9.")


        def _handle_msg_RXgain(self, msg):
            if pmt.is_real(msg):
                self.RXMES = pmt.to_python(msg)
                print(f"RX gain: {self.RXMES}")
                self.set_RX(self._RX, self.RXMES) 
            else:
                print("Error: RX gain is not between 1-60.")
               
        def _handle_msg_TXgain(self, msg):
            if pmt.is_real(msg):
                self.TXMES = pmt.to_python(msg)
                print(f"TX gain: {self.TXMES}")
                self.set_TX(self._TX, self.TXMES) 
            else:
                print("Error: TX gain is not between 1-60.")



      
        
   def set_RF(self, _RF, RFMES= 0):
       return f"pigs"


            
   def set_IF(self, _IF, IFMES= 0):
       return f"Moon"


            
   def set_RX(self, _RX, RXMES= 0):
       return f"echos"


            
   def set_TX(self, _TX, TXMES= 0):
       return f"brick"
