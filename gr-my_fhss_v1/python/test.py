import numpy as np
import cPickle

# /home/jx/Desktop/gr_origin/gr-my_fhss_v1/AM_FHSS.pkl



with open("AM_FHSS.pkl","rb") as f:
    data1 = cPickle.load(f)
with open("FM_FHSS.pkl","rb") as f:
    data2 = cPickle.load(f)
with open("2FSK_FHSS.pkl","rb") as f:
    data3 = cPickle.load(f)
with open("BPSK_FHSS.pkl","rb") as f:
    data4 = cPickle.load(f)
with open("QPSK_FHSS.pkl","rb") as f:
    data5 = cPickle.load(f)

data = np.vstack((data1,data2,data3,data4,data5))

cPickle.dump(data, file("RML-MOD-FHSS-DATA.pkl", "wb"))
print "please click [stop] button"

