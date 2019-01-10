# -*- coding: utf-8 -*-
"""
initaxes.py

Created on Thu Jan  3 14:55:37 2019

@author: slehar
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
#from matplotlib.patches import Circle, Rectangle

# Init plain axes
def initPlainAx(locSize, axTitle):
    ax = plt.axes(locSize)    #(xorg,yorg,width,height)
    ax.set_xlim((-1,1))
    ax.set_ylim((-1,1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(axTitle)
    ax.set_axis_bgcolor((.75,.75,.75))
    ax.spines['bottom'].set_color((.75,.75,.75))
    ax.spines['top'].set_color((.75,.75,.75)) 
    ax.spines['right'].set_color((.75,.75,.75))
    ax.spines['left'].set_color((.75,.75,.75))
    scalarLight = plt.Circle((0,0), .8, fc='k', ec='k')
    ax.add_patch(scalarLight)
    return ax

# Init plot axes
def initPlotAxes(locSize, axTitle):
    ax = plt.axes(locSize)    #(xorg,yorg,width,height)
    ax.set_yticks([])
    ax.set_xlim((-1,1))
    ax.grid(True)
    ax.set_title(axTitle)
    return ax

# Init plot2 axes
def initPlot2Axes(locSize, axTitle):
    ax = plt.axes(locSize)    #(xorg,yorg,width,height)
    ax.set_xlim((-1, 1))
    ax.set_ylim((-1, 1))
    ax.grid(True)
    ax.set_title(axTitle)
    return ax
    
# Init Slider
def init_slider(locSize, label):
    axSl = plt.axes(locSize)  #(xorg,yorg,width,height)
    slider = Slider(axSl, label, -1., 1., valinit=0.)
    slider.poly.fill = False
    return slider

# Scalar Light Y
class ScalarLight:
    
    def update_color(self, slVal):
        r = - np.clip(slVal, -1, 0)
        g =   np.clip(slVal,  0, 1)
        b = 0.
        self.lightAx.patches[0].set_facecolor((r,g,b,1))
#        self.slAx.set_val(slVal)
        self.changed = True
        

    def __init__(self, locSize, label):
        self.locSize = locSize
        self.sliderLocSize = [locSize[0],
                              locSize[1],
                              locSize[2],
                              locSize[3]/4.]
        self.slAx = init_slider(self.sliderLocSize, label)
        self.slAx.on_changed(self.update_color)

        self.lightLocSize  = [locSize[0]+locSize[2]/3,
                              locSize[1]+locSize[3]*.75,
                              locSize[2]/4,
                              locSize[3]/2]
        self.lightAx = initPlainAx(self.lightLocSize, label)
        
        self.changed = False
        
# Vector Plot
class VectorPlot:
    
    def update_vector(self, val):
#        self.scalarSl.set_val(val)
#        self.scalarSl.update_color(val)
        self.changed = True
        
        
    def __init__(self, locSize, label, tArray, dArray):
        self.locSize = locSize
        self.sliderLocSize = [locSize[0],
                              locSize[1],
                              locSize[2],
                              locSize[3]/4.]
        self.slAx = init_slider(self.sliderLocSize, label)
        self.slAx.on_changed(self.update_vector)

        self.plotLocSize  = [locSize[0],
                              locSize[1]+locSize[3]*.5,
                              locSize[2],
                              locSize[3]]
        self.plotAx = initPlotAxes(self.plotLocSize, label)
        self.line1 = self.plotAx.plot(tArray, dArray,'-')
        
        self.changed = False


# Bivector Plot
class BivectorPlot:
    
    def update_vector(self, val):
#        self.scalarSl.set_val(val)
#        self.scalarSl.update_color(val)
        self.changed = True
        
        
    def __init__(self, locSize, label, tArray, dArrayX, dArrayY):
        self.locSize = locSize

        self.plotLocSize  = [locSize[0],
                              locSize[1],
                              locSize[2],
                              locSize[3]]
        self.plotAx = initPlot2Axes(self.plotLocSize, label)
        self.line1 = self.plotAx.plot(tArray, dArrayX,'-')
          
        self.changed = False

