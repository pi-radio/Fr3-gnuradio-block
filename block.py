import numpy as np
import urllib.request
from gnuradio import gr
from gnuradio import blocks

class blk(gr.sync_block):
    
    def __init__(self, frequency=1000000, ip_address="0.0.0.0", lo1=0, lo1-=0, lo2=0, lo2-=0):
        gr.sync_block.__init__(
            self,
            name='FR3',   
            in_sig=None,
            out_sig=None
        )
        self.highlo = highlo
        self.lowlo = lowlo
        self.rx1gain = rx1gain
        self.rx2gain = rx2gain
        self.tx1gain = tx1gain
        self.tx2gain = tx2gain
        self.ip_address = ip_address

     def set_highlo(self, highlo):
        """Set the high lo frequency."""
        self.highlo = highlo
        url = f"http://{self.ip_address}:5111/high_lo?freq={self.highlo}"
        response = urllib.request.urlopen(url)
        if response.status == 200:
            print(f"High LO frequency set to {self.highlo}")

    def set_lowlo(self, lowlo):
        """Set the low lo frequency."""
        self.lowlo = lowlo
        url = f"http://{self.ip_address}:5111/low_lo?freq={self.lowlo}"
        response = urllib.request.urlopen(url)
        if response.status == 200:
            print(f"Low LO frequency set to {self.lowlo}")

    def set_rx1gain(self, rx1gain):
        """Set RX 1 gain."""
        self.rx1gain = rx1gain
        url = f"http://{self.ip_address}:5111/gain?trx=rx&chan=0&v={self.rx1gain}"
        response = urllib.request.urlopen(url)
        if response.status == 200:
            print(f"RX1 gain set to {self.rx1gain}")

    def set_rx2gain(self, rx2gain):
        """Set RX 2 gain."""
        self.rx2gain = rx2gain
        url = f"http://{self.ip_address}:5111/gain?trx=rx&chan=1&v={self.rx2gain}"
        response = urllib.request.urlopen(url)
        if response.status == 200:
            print(f"RX2 gain set to {self.rx2gain}")

    def set_tx1gain(self, tx1gain):
        """Set TX 1 gain."""
        self.tx1gain = tx1gain
        url = f"http://{self.ip_address}:5111/gain?trx=tx&chan=0&v={self.tx1gain}"
        response = urllib.request.urlopen(url)
        if response.status == 200:
            print(f"TX1 gain set to {self.tx1gain}")

    def set_tx2gain(self, tx2gain):
        """Set TX 2 gain."""
        self.tx2gain = tx2gain
        url = f"http://{self.ip_address}:5111/gain?trx=tx&chan=1&v={self.tx2gain}"
        response = urllib.request.urlopen(url)
        if response.status == 200:
            print(f"TX2 gain set to {self.tx2gain}")


      
