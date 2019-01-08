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

# Scalar Light X
#ax0 = initaxes.initPlainAx((.13, .75, .05, .1),"Scalar X")
#sliderS = initaxes.init_slider((.05, .55, .2, .05), "Scalar S")
#
#def update_color(xVal):
#    r = - np.clip(xVal, -1, 0)
#    g = np.clip(xVal, 0, 1)
#    b = 0.
#    ax0.patches[0].set_facecolor((r,g,b,1))
#sliderS.on_changed(update_color)

# Scalar Light Y
class ScalarLight:
    
    def update_color(self, slVal):
        r = - np.clip(slVal, -1, 0)
        g =   np.clip(slVal,  0, 1)
        b = 0.
        self.lightAx.patches[0].set_facecolor((r,g,b,1))
        

    def __init__(self, locSize, label):
        self.locSize = locSize
        self.sliderLocSize = [locSize[0],
                              locSize[1],
                              locSize[2],
                              locSize[3]/4.]
        self.slAx = initaxes.init_slider(self.sliderLocSize, label)
        self.slAx.on_changed(self.update_color)

        self.lightLocSize  = [locSize[0]+locSize[2]/3,
                              locSize[1]+locSize[3]*.75,
                              locSize[2]/4,
                              locSize[3]/2]
        self.lightAx = initaxes.initPlainAx(self.lightLocSize, label)
        
        
xLight = ScalarLight((.05, .55, .2, .2),"x")
        
yLight = ScalarLight((.05, .1, .2, .2), 'y')

# Scalar Light Y
class VectorPlot:
    

    def __init__(self, locSize, label):
        self.locSize = locSize
        self.sliderLocSize = [locSize[0],
                              locSize[1],
                              locSize[2],
                              locSize[3]/4.]
        self.slAx = initaxes.init_slider(self.sliderLocSize, label)
#        self.slAx.on_changed(self.update_vector)

        self.plotLocSize  = [locSize[0],
                              locSize[1]+locSize[3]*.5,
                              locSize[2],
                              locSize[3]]
        self.plotAx = initaxes.initPlotAxes(self.plotLocSize, label)
        self.line1 = self.plotAx.plot(tArray, dArrayX,'-')


        
xVector = VectorPlot((.3, .55, .2, .2), 'x')        
        
yVector = VectorPlot((.3, .1,  .2, .2), 'y')        
        
        
########[ Sawtooth Generator ]########
def SawToothGenerator(arg):
    
    global currTime, tArray, dArrayX, dArrayY

    # array T    
    currTime += delT
    relTime = currTime % (2.)
    currValX = relTime * xVector.slAx.val
    currValY = relTime * yVector.slAx.val
    xVector.line1[0].set_data((0., currValX),(0,0)) 
    yVector.line1[0].set_data((0., currValY),(0,0)) 
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
