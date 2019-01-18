# -*- coding: utf-8 -*-
"""
TestMultiPlot.py

Test multiple plots plotted in sequence 
on top of each other at 1 sec intervals.

Created on Fri Jan 11 12:09:13 2019

@author: slehar
"""
import numpy as np
import matplotlib.pyplot as plt
import popup

plt.close('all')
fig = plt.figure(figsize=[6,6])
ax = plt.axes((.1,.1,.8,.8))
plt.show()
popup.Popup()

tDat=np.arange(-np.pi, np.pi, np.pi/360)

#plt.ion()
for f in np.arange(1,11):
    print f
    sDat = np.sin(tDat*f) * .5
    plt.plot(tDat,sDat)
    plt.pause(1)


