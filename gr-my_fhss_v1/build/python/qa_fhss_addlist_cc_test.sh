#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/jx/Desktop/gr_origin/gr-my_fhss_v1/python
export PATH=/home/jx/Desktop/gr_origin/gr-my_fhss_v1/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/jx/Desktop/gr_origin/gr-my_fhss_v1/build/swig:$PYTHONPATH
/usr/bin/python2 /home/jx/Desktop/gr_origin/gr-my_fhss_v1/python/qa_fhss_addlist_cc.py 
