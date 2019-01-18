# -*- coding: utf-8 -*-
"""
popup.py
Created on Fri Jan 11 12:26:44 2019

@author: slehar
"""
import matplotlib.pyplot as plt


# Set window in upper-left corner
#==============================================================================
def Popup():
    
    figmgr=plt.get_current_fig_manager()
    figmgr.canvas.manager.window.raise_()
    geom=figmgr.window.geometry()
    xOrg,yOrg,xSize,ySize = geom.getRect()
    figmgr.window.setGeometry(10,10,xSize,ySize)


