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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from add_fhss_cc import add_fhss_cc
from gnuradio import analog

class qa_add_fhss_cc (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
        src2 = analog.sig_source_c(32000, analog.GR_COS_WAVE, 10000, 1, 0)
        freq_s = add_fhss_cc(samp_ra=32000,base_freq=25000,freq_interval=25000,hop_times=8,hop_len=800)
        snk = final_sink(1, 5000,256)
        self.tb.connect(src2, freq_s)
        self.tb.connect(freq_s, snk)
        self.tb.run ()


        # check data


if __name__ == '__main__':
    gr_unittest.run(qa_add_fhss_cc, "qa_add_fhss_cc.xml")
