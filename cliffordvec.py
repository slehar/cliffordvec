'''
CliffordVec3.py


'''

import numpy as np
import matplotlib.pyplot as plt
#matplotlib.use('TkAgg') # <-- THIS MAKES IT FAST!
#import matplotlib.pyplot as plt
import matplotlib.animation as animation
import initaxes

# Parameters
winXSizeInches = 16
winYSizeInches = 8

# Global variables
tArray  = []
dArrayX = []
dArrayY = []
currTime = 0.
currValX = 0.
currValY = 0.
period = 1.           # sec
tRes = 2.             # pixels/sec
delT = period/tRes  
plotWidth = 5.        # sec
nPts = plotWidth * tRes
slope = 1./period     # Basic X/t Y/t slope

# Open figure 
plt.close('all')
fig = plt.figure(figsize=(winXSizeInches, winYSizeInches))
fig.canvas.set_window_title('CliffordVec3')

# Scalar Light
scalarLight = plt.Circle((0,0), .8, fc='k', ec='k')
ax0 = initaxes.initPlainAx((.1, .65, .05, .1),"Scalar X")
ax0.set_axis_bgcolor((.75,.75,.75))
ax0.spines['bottom'].set_color((.75,.75,.75))
ax0.spines['top'].set_color((.75,.75,.75)) 
ax0.spines['right'].set_color((.75,.75,.75))
ax0.spines['left'].set_color((.75,.75,.75))

ax0.add_patch(scalarLight)
sliderS = initaxes.init_slider((.05, .45, .2, .05), "Scalar S")

def update_color(xVal):
    r = - np.clip(xVal, -1, 0)
    g = np.clip(xVal, 0, 1)
    b = 0.
    scalarLight.set_facecolor((r,g,b,1))
sliderS.on_changed(update_color)
    
# Plot x vector axes
ax1 = initaxes.initPlotAxes((.3, .55, .2, .4),"Vector X")    
line1=ax1.plot(tArray, dArrayX,'-')    

axSl1 = initaxes.init_slider((.3, .45, .2, .05), "X")
#axSl1.initaxes.sliderX.on_changed(update_vector)


########[ Sawtooth Generator ]########
def SawToothGenerator(arg):
    
    global currTime, tArray, dArrayX, dArrayY

    # array T    
    currTime += delT
    relTime = currTime % (2.)
    currValX = relTime * sliderS.val
    line1[0].set_data((0., currValX),(0,0)) 
    plt.pause(.1)
    
    
ani = animation.FuncAnimation(fig, SawToothGenerator, interval=0.)


# Show figure
fig.show()

# Set window in upper-left corner
#==============================================================================
figmgr=plt.get_current_fig_manager()
figmgr.canvas.manager.window.raise_()
geom=figmgr.window.geometry()
xOrg,yOrg,xSize,ySize = geom.getRect()
figmgr.window.setGeometry(10,10,xSize,ySize)

#==============================================================================