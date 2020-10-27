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

import numpy as np
from gnuradio import gr
import math

class addlist_fhss_cc(gr.sync_block):
    """
    docstring for block addlist_fhss_cc
    """
    def __init__(self, samp_rate,base_freq,freq_interval,hop_times):
        gr.sync_block.__init__(self,
            name="addlist_fhss_cc",
            in_sig=[np.complex64],
            out_sig=[np.complex64])
        self.samp_rate = samp_rate
        self.base_freq = base_freq
        self.freq_interval = freq_interval
        self.hop_times = hop_times
        self.freq_series = []
        self.remain = 0
        self.freq_sel = 0
        self.freq_len_list = [1100, 900, 1000, 1020, 1130, 1024, 980, 920]
        self.hop_len = self.freq_len_list[self.freq_sel]
        for index in range(hop_times):
            self.freq_series.append(index * self.freq_interval + self.base_freq)

    def work(self, input_items, output_items):

        in0 = input_items[0]
        out = output_items[0]
        len_vector = len(in0)
        carrier_sig = []

        if (self.remain != 0):
            carrier_sig = [np.complex(math.cos(2 * np.pi * self.freq_series[self.freq_sel] * i / self.samp_rate),
                                      math.sin(2 * np.pi * self.freq_series[self.freq_sel] * i / self.samp_rate)) for i
                           in range(self.remain)]
            len_vector -= self.remain
            self.freq_sel = (self.freq_sel + 1) % self.hop_times
            self.hop_len = self.freq_len_list[self.freq_sel]

        while (len_vector / self.hop_len > 0):
            C_signal = [np.complex(math.cos(2 * np.pi * self.freq_series[self.freq_sel] * i / self.samp_rate),
                                   math.sin(2 * np.pi * self.freq_series[self.freq_sel] * i / self.samp_rate)) for i in
                        range(self.hop_len)]
            carrier_sig += C_signal
            len_vector -= self.hop_len
            self.freq_sel = (self.freq_sel + 1) % self.hop_times
            self.hop_len = self.freq_len_list[self.freq_sel]

        if (len_vector % self.hop_len != 0):
            C_signal = [np.complex(math.cos(2 * np.pi * self.freq_series[self.freq_sel] * i / self.samp_rate),
                                   math.sin(2 * np.pi * self.freq_series[self.freq_sel] * i / self.samp_rate)) for i in
                        range(len_vector % self.hop_len)]
            carrier_sig += C_signal
            self.remain = self.hop_len - len_vector

        Final_sig = [carrier_sig[i] * in0[i] for i in range(len(in0))]
        output_items[0][:] = Final_sig

        print ("prev remain hop len: {}".format(self.remain))
        return len(output_items[0])

