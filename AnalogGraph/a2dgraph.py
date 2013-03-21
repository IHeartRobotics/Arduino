#!/usr/bin/python
import sys
from pylab import *
import numpy as np
data = np.loadtxt('out.txt', dtype ='string').T
print data

# x:y
t = []
v = []
for i in range (0, len(data)):

    sample = data[i].split(":")

    if len(sample) == 2 and sample[0].isdigit() and sample[1].isdigit():
        t.append(int(sample[0]))
        v.append(int(sample[1]))
        print "previous t: " + str(t[i-1])
#        print str(i)
#        print "current t: " + str(t[i])
        print "sample [0]" + str(sample[0])
    else:
         print "line " + str(i) + " is fucked: " + data[i]
print "..."
print t
print v
plot(t,v)
show()
sys.exit(0)
