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

from gnuradio import gr
import cPickle
import time
import numpy as np
modulated_name = ["AM_FHSS","FM_FHSS","2FSK_FHSS","MSK_FHSS","GFSK_FHSS","BPSK_FHSS","QPSK_FHSS","8PSK_FHSS","16PSK_FHSS"]


class fhss_list_sink(gr.sync_block):
    """
    docstring for block fhss_list_sink
    """
    def __init__(self, modtype,vec_num,vec_len):
        gr.sync_block.__init__(self,
            name="fhss_list_sink",
            in_sig=[np.complex64],
            out_sig=None)
        self.modtype = modulated_name[modtype]
        self.vec_num = vec_num
        self.vec_len = vec_len
        self.dataset = {}
        self.position = -1
        self.dataset[self.modtype] = np.zeros([vec_num, 3, vec_len], dtype=np.float32)
        self.remain = []
        self.vec_index = 0
        self.freq_len_list = np.cumsum([1100, 900, 1000, 1020, 1130, 1024, 980, 920])
        self.hop_index = 0
        self.step = 0

    def work(self, input_items, output_items):
        in0 = input_items[0]
        raw_output_vector = in0.tolist() + self.remain
        len_in = len(raw_output_vector)
        print "receive data len: {}".format(len(in0))
        print "remain vector len:{}".format(len(self.remain))
        if (raw_output_vector != []):
            sample_index = 0
            # hop_index = 1
            while (len_in / self.vec_len > 0 and self.vec_index < self.vec_num):
                sample_vector = raw_output_vector[sample_index * self.vec_len:(sample_index + 1) * self.vec_len]

                # # Normalizehie the energy in this vector to be 1
                energy = np.sum((np.abs(sample_vector)))
                sample_vector = sample_vector / energy

                self.step += self.vec_len
                if (self.step > self.freq_len_list[self.hop_index]):
                    # self.position = self.hop_len*hop_index-sample_index*self.vec_len
                    self.position = self.freq_len_list[self.hop_index] - (self.step - self.vec_len)
                    if (self.hop_index == 7):
                        self.step = self.step - self.freq_len_list[self.hop_index]
                    # hop_index += 1
                    self.hop_index = (self.hop_index + 1) % 8
                    print "hop_dot_position:{}".format(self.position)
                else:
                    self.position = -1

                self.dataset[self.modtype][self.vec_index, 0, :] = np.real(sample_vector)
                self.dataset[self.modtype][self.vec_index, 1, :] = np.imag(sample_vector)
                self.dataset[self.modtype][self.vec_index, 2, 0] = self.position

                self.vec_index += 1
                sample_index += 1
                len_in -= self.vec_len

            if (self.vec_index == self.vec_num):
                print "all done. {}.pkl writting to disk".format(self.modtype)
                cPickle.dump(self.dataset, file("{}.pkl".format(self.modtype), "wb"))
                print "please click [stop] button"
                time.sleep(600000)

            if (len_in % self.vec_len != 0):
                self.remain = raw_output_vector[-len_in:]

        return len(input_items[0])

