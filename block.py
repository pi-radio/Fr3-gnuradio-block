import numpy as np
import urllib.request
from gnuradio import gr
from gnuradio import blocks

class blk(gr.sync_block): 
    """
    GNU Radio block to control an SDR via HTTP requests.
    """

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
        self.lo_tx_1 = lo1
        self.lo_tx_1_ = lo1_
        self.lo_tx_2 = lo2
        self.lo_tx_2_ = lo2_
        self.ip_address = ip_address
        self.set_frequency(frequency) #set initial frequency

    def set_highlo(self, frequency):
        """Set the high lo frequency."""
        self.highlo = highlo
        url = f"http://{self.ip_address}:5111/high_lo?freq={self.highlo}"
    def set_low(self, frequency):
        """Set the low lo frequency."""
        self.lowlo = lowlo
        url = f"http://{self.ip_address}:5111/low_lo?freq={self.lowlo}"

    def set_rx1gain(self, Rx1gain):
        """set RX 1 gain"""
        self.rx1gain = rx1gain
        rxgain1 = f"http://{self.ip_address}:5111/{self.rx1gain}"
       
    def set_rx2gain(self, RX2gain):
        """set RX 2 gain"""
        self.rx2gain = rx2gain
        rxgain2 = f"http://{self.ip_address}:5111/{self.rx1gain}"
       
    def set_tx1gain(self, TX1gain):
        """set TX 1 gain"""
        self.tx1gain = tx1gain
        txgain1 = f"http://{self.ip_address}:5111/{self.tx1gain}"

     def set_tx2gain(self, tx2gain):
         """set TX 2 gain"""
         self.tx2gain = tx2gain
         txgain2 = f"http://{self.ip_address}:5111/{self.tx2gain}"

     def set_rx1gain(self, txlo1):
        """set tx 1 lo offset"""
        self.lo_tx_1 = lo1
        rxgain1 = f"http://{self.ip_address}:5111/{self.gain}"

     def set_rx1gain(self, txlo1_):
         """set tx1 lo - offset"""
         self.lo_tx_1_ = lo1_
         rxgain1 = f"http://{self.ip_address}:5111/{self.gain}"
       
     def set_rx1gain(self, txlo2):
        """set lo TX 2 offset"""
        self.lo_tx_2 = lo2
        rxgain1 = f"http://{self.ip_address}:5111/{self.gain}"

     def set_rx1gain(self, txlo2_):
        """set lo TX 2 - offset """
        self.lo_tx_2_ = lo2_
        rxgain1 = f"http://{self.ip_address}:5111/{self.gain}"
       

      
