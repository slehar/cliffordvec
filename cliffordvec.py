'''
CliffordVec.py


'''

import numpy as np
import matplotlib.pyplot as plt
#matplotlib.use('TkAgg') # <-- THIS MAKES IT FAST!
#import matplotlib.pyplot as plt
import matplotlib.animation as animation
import initaxes
import popup

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
tRes = 5.             # pixels/sec
delT = period/tRes  
plotWidth = 5.        # sec
nPts = plotWidth * tRes
slope = 1./period     # Basic X/t Y/t slope

# Open figure 
plt.close('all')
fig = plt.figure(figsize=(winXSizeInches, winYSizeInches))
fig.canvas.set_window_title('CliffordVec')
fig.text(.05, .9, "'Q' to quit", fontsize=18)
plt.show()
popup.Popup()


# Keypress 'q' to quit callback function
def press(event):
#    sys.stdout.flush()
    if event.key == 'q':
        plt.close()
fig.canvas.mpl_connect('key_press_event', press)

        
xLight   = initaxes.ScalarLight((.05, .55, .2, .2),"x")
        
yLight   = initaxes.ScalarLight((.05, .1, .2, .2), 'y')
        
xVector  = initaxes.VectorPlot((.3, .55, .2, .2), 'x', 
                               tArray, dArrayX)        
        
yVector  = initaxes.VectorPlot((.3, .1,  .2, .2), 'y', 
                               tArray, dArrayY)        
        
biVector = initaxes.BivectorPlot((.55, .1, .4, .8), 'Bivector', 
                                 tArray, dArrayX, dArrayY)
#biVector.plotAx.hold(True)


        
########[ Sawtooth Generator ]########
def SawToothGenerator(arg):
    
    global currTime, tArray, dArrayX, dArrayY
    

    # array T    
#    currTime += delT
#    relTime = currTime % (2.)
#    if relTime <= delT:
#        biVector.plotAx.hold(False)
        
    
    xVec = []
    yVec = []
    tVec = []
#    for currTime in np.arange(-2,2,.1):
        
    # ValX and ValY
    xVal = xVector.slAx.val
    yVal = yVector.slAx.val

    xVector.line1[0].set_data((0, xVal),(0, 0)) 
    yVector.line1[0].set_data((0, yVal),(0, 0)) 

#    tVec.append(currTime)        
    xVec.append(currValX)
    yVec.append(currValY)
        
    
    biVector.line1[0].set_data((0, xVal), (0, yVal))
#    biVector.line2[0].set_data(tVec, yVec)


    plt.show()
#    ax1.plot(xVec, tVec)



#       ax1.clear()
#        ax1.plot(xs, ys)
#        plt.grid()

    
#    biVector.line1[0].set_data((0, currValX), (0, currValY))
    
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
    
    
def plotOnce(arg):

#    print 'In plotOnce()'
    
#    biVector.plotAx.hold(True)
#    plt.ion()


    for t in np.arange(0, 1, .1):
#        print t

        # ValX and ValY
        currValX = t * xVector.slAx.val
        currValY = t * yVector.slAx.val
        xVector.line1[0].set_data((0., currValX),(0,0)) 
        yVector.line1[0].set_data((0., currValY),(0,0))
        
        # Bivector lines
        biVector.line1[0].set_data((0, currValX), (0, 0))
#        biVector.line1[0].draw(plt.get_backend())
        biVector.line2[0].set_data((currValX, currValX), (0, currValY))
#        biVector.line2[0].draw(plt.get_backend())1
        try: input('hit return')
        except: pass
        plt.draw()
#        fig.canvas.draw_idle()

        
ani = animation.FuncAnimation(fig, SawToothGenerator, interval=0)

# Show figure

#plotOnce(1)
#    plt.draw()

