#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2026 PI-Radio.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy
from gnuradio import gr

class FR31Chan(gr.sync_block):
    """
    docstring for block FR31Chan
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="FR31Chan",
            in_sig=[<+numpy.float32+>, ],
            out_sig=[<+numpy.float32+>, ])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        out[:] = in0
        return len(output_items[0])
