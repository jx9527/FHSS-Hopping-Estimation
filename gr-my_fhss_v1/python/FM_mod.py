#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2020 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr
import numpy as np
import math
class FM_mod(gr.sync_block):
    """
    docstring for block FM_mod
    """
    def __init__(self, samp_rate,deviation,freq):
        gr.sync_block.__init__(self,
            name="FM_mod",
            in_sig=[np.float32],
            out_sig=[np.complex64])
        self.deviation = deviation
        self.samp_rate = samp_rate
        self.freq = freq

    def work(self, input_items, output_items):
        in0 = input_items[0]
        modulated_signal = [np.complex(math.cos(2 * math.pi * self.deviation * itr / self.samp_rate),
                                       math.sin(2 * math.pi * self.deviation * itr / self.samp_rate))
                            for itr in np.cumsum(in0)]
        C_signal = [np.complex(math.cos(2 * np.pi * self.freq * i / self.samp_rate),
                               math.sin(2 * np.pi * self.freq * i / self.samp_rate))
                    for i in range(len(in0))]

        Final_sig = [C_signal[i] * modulated_signal[i] for i in range(len(in0))]
        output_items[0][:] = Final_sig
        return len(output_items[0])

