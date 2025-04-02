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
        self.highlo = freq
        self.lowlo = freq2
        self.rx1gain = gain1
        self.rx2gain = gain2
        self.tx1gain = gain3
        self.tx2gain = gain4
        self.ip_address = ip_address

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
        self.highlo = freq
        self.lowlo = freq2
        self.rx1gain = gain1
        self.rx2gain = gain2
        self.tx1gain = gain3
        self.tx2gain = gain4
        self.ip_address = ip_address
        self.freq = freq
        url = f"http://{self.ip_address}:5111/high_lo?freq={self.freq}"
        response = urllib.request.urlopen(url)
        if response.status == 200:
            print(f"High LO frequency set to {self.freq}")
        """Set the low lo frequency."""
        self.freq2 = freq2
        ur2 = f"http://{self.ip_address}:5111/low_lo?freq={self.freq2}"
        response = urllib.request.urlopen(url)
        if response.status == 200:
            print(f"Low LO frequency set to {self.freq2}")
        self.gain1 = gain1
        url3 = f"http://{self.ip_address}:5111/gain?trx=rx&chan=0&v={self.gain1}"
        response = urllib.request.urlopen(url)
        if response.status == 200:
            print(f"RX1 gain set to {self.gain1}")
        """Set RX 2 gain."""
        self.gain2 = gain2
        url4 = f"http://{self.ip_address}:5111/gain?trx=rx&chan=1&v={self.gain2}"
        response = urllib.request.urlopen(url)
        if response.status == 200:
            print(f"RX2 gain set to {self.gain2}")
        """Set TX 1 gain."""
        self.gain3 = gain3
        url5 = f"http://{self.ip_address}:5111/gain?trx=tx&chan=0&v={self.gain3}"
        response = urllib.request.urlopen(url)
        if response.status == 200:
            print(f"TX1 gain set to {self.gain3}")
        """Set TX 2 gain."""
        self.gain4 = gain4
        url6 = f"http://{self.ip_address}:5111/gain?trx=tx&chan=1&v={self.gain4}"
        response = urllib.request.urlopen(url)
        if response.status == 200:
            print(f"TX2 gain set to {self.gain4}")
