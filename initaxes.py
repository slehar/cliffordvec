# -*- coding: utf-8 -*-
"""
initaxes.py

Created on Thu Jan  3 14:55:37 2019

@author: slehar
"""


import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.patches import Circle, Rectangle

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
    ax.set_xlim((-1,1))
    ax.grid(True)
    ax.set_title(axTitle)
    return ax
    
# Init Slider
def init_slider(locSize, label):
    axSl = plt.axes(locSize)  #(xorg,yorg,width,height)
    slider = Slider(axSl, label, -1., 1., valinit=0.)
    slider.poly.fill = False
    return slider

