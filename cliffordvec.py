'''
CliffordVec.py


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
fig.canvas.set_window_title('CliffordVec')

# Keypress 'q' to quit callback function
def press(event):
    sys.stdout.flush()
    if event.key == 'q':
        plt.close()
fig.canvas.mpl_connect('key_press_event', press)

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
        self.slAx = initaxes.init_slider(self.sliderLocSize, label)
        self.slAx.on_changed(self.update_color)

        self.lightLocSize  = [locSize[0]+locSize[2]/3,
                              locSize[1]+locSize[3]*.75,
                              locSize[2]/4,
                              locSize[3]/2]
        self.lightAx = initaxes.initPlainAx(self.lightLocSize, label)
        
        self.changed = False
        
        
xLight = ScalarLight((.05, .55, .2, .2),"x")
        
yLight = ScalarLight((.05, .1, .2, .2), 'y')

# Vector Plot
class VectorPlot:
    
    def update_vector(self, val):
#        self.scalarSl.set_val(val)
#        self.scalarSl.update_color(val)
        self.changed = True
        
        
    def __init__(self, locSize, label):
        self.locSize = locSize
        self.sliderLocSize = [locSize[0],
                              locSize[1],
                              locSize[2],
                              locSize[3]/4.]
        self.slAx = initaxes.init_slider(self.sliderLocSize, label)
        self.slAx.on_changed(self.update_vector)

        self.plotLocSize  = [locSize[0],
                              locSize[1]+locSize[3]*.5,
                              locSize[2],
                              locSize[3]]
        self.plotAx = initaxes.initPlotAxes(self.plotLocSize, label)
        self.line1 = self.plotAx.plot(tArray, dArrayX,'-')
        
        self.changed = False


        
xVector = VectorPlot((.3, .55, .2, .2), 'x')        
        
yVector = VectorPlot((.3, .1,  .2, .2), 'y')        
        
# Bivector Plot
class BivectorPlot:
    
    def update_vector(self, val):
#        self.scalarSl.set_val(val)
#        self.scalarSl.update_color(val)
        self.changed = True
        
        
    def __init__(self, locSize, label):
        self.locSize = locSize

        self.plotLocSize  = [locSize[0],
                              locSize[1],
                              locSize[2],
                              locSize[3]]
        self.plotAx = initaxes.initPlot2Axes(self.plotLocSize, label)
        self.line1 = self.plotAx.plot(tArray, dArrayX,'-')
          
        self.changed = False


biVector = BivectorPlot((.55, .1, .4, .8), 'Bivector')




        
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
    
    biVector.line1[0].set_data((0, currValX), (0, currValY))
    
    # Couple scalar and vector sliders
    if xVector.changed:
        xLight.slAx.set_val(xVector.slAx.val)
        xVector.changed = False
        xLight.changed  = False
    if xLight.changed:
        xVector.slAx.set_val(xLight.slAx.val)
        xLight.changed  = False
        xVector.changed = False
    if yVector.changed:
        yLight.slAx.set_val(yVector.slAx.val)
        yVector.changed = False
        yLight.changed  = False
    if yLight.changed:
        yVector.slAx.set_val(yLight.slAx.val)
        yLight.changed  = False
        yVector.changed = False
    
#    plt.pause(.1)
    
    
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
