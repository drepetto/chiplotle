
"""
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
"""

import hpgl
import math
from utils import *
#import numpy as np

def edgeRect(x, y, sx, sy, rot):
    tl = (-sx / 2., sy / 2.)
    tr = (sx / 2., sy / 2.)
    bl = (-sx / 2., -sy / 2.)
    br = (sx / 2., -sy / 2.)

    tl = rotate2d(tl,  rot)
    tr = rotate2d(tr,  rot)
    bl = rotate2d(bl,  rot)
    br = rotate2d(br,  rot)

    #print 'tl ', tl
    #print 'tr ', tr
    #print 'bl ', bl
    #print 'br ', br

    out = hpgl.penUp()
    out += hpgl.plotAbsolute((x, y))
    out += hpgl.plotAbsolute((x + tl[0], y + tl[1]))
    out += hpgl.penDown()
    out += hpgl.plotAbsolute((x + tr[0], y + tr[1]))
    out += hpgl.plotAbsolute((x + br[0], y + br[1]))
    out += hpgl.plotAbsolute((x + bl[0], y + bl[1]))
    out += hpgl.plotAbsolute((x + tl[0], y + tl[1]))
    out += hpgl.penUp()

    return out

def edgeCircle(x, y, rad):
    out = hpgl.penUp()
    out += hpgl.plotAbsolute((x, y))
    out += hpgl.circle(rad)
    return out



def randomWalk(steps=100, step_size_var=500):
    penDown()
    for i in range(steps):
        r = random.randint(1, step_size_var)
        A = random.random() * math.pi * 2
        (x,y) = polar2xy(r,A)
        goto(x, y)
        sleepWhileBufferFull()
    penUp()


def plotAsciiArt(text, char_size, compensation = 1):
    h = char_size * 5/4.
    if compensation:
        h *= 5/4.
    return plotText(text, char_size, h, 0, 0, -0.3)      


def plotText(text, b=None, h=None, angle=None, char_s=None, line_s=None, chunk=10):
    """Print text ."""
    out = ''
    # replace all \n by \n\r
    text = text.replace('\n','\n\r')
    if b and h:
        out += absCharSize(b, h)
    if angle:
        out += charSlant(angle)   
    if char_s and line_s:
        out += charPlot(char_s, line_s)
    for i in range(0, len(text), chunk):
        out += label(text[i:i + 10])

    return out


def plotTextFile(filename, pen=None):
    """Open and print the txt file.
    If pen argument is passed, select that pen
    """
    out = ''
    f = open(filename)

    if pen:
        out += selectPen(pen)

    out += plotText(f.read())
    return out


def absCharSize(w = None, h = None):
    return hpgl.absCharSize(w, h)

def absoluteDirection(run = 1, rise = 0):
    return hpgl.absoluteDirection(run, rise)
    
def altCharSet(n = 0):
    return hpgl.altCharSet(n)

def charChordAngle(angle = 5):
    return hpgl.charChordAngle(angle)
    
def bufferLabel(text = None):
    return hpgl.bufferLabel(text)

def charPlot(spaces = None, lines = None):
    return hpgl.charPlot(spaces, lines)

newline = charPlot

def charSelectionMode(switch = 0, fallback = 0):
    return hpgl.charSelectionMode(switch, fallback)
    
def charSet(set = 0):
    return hpgl.charSet(set)       

def charSlant(angle = 0):
    tan = angle * 2 * math.pi / 360.
    return hpgl.charSlant(tan)
    
def defineLabelTerminator(t = chr(3)):
    return hpgl.defineLableTerminator(t)

def directionVertical(dir = 0):
    return hpgl.directionVertical(dir)

def extraSpace(spaces = 0, lines = 0):
    return hpgl.extraSpace(spaces, lines)

def invokeCharSlant(slot = 0, left = None):
    return hpgl.invokeCharSlant(slote, left)

def label(text):
    #print "label got: %s" % text
    return hpgl.label(text)

def labelOrigin(positionNum = 1):
    return hpgl.labelOrigin(positionNum)
    

def outputLabelLength():
    return hpgl.outputLabelLength()
    

def printBufferedLabel():
    return hpgl.printBufferedLabel()
    
def relCharSize( w = None, h = None):
    return hpgl.relCharSize(w, h)

def relativeDirection( run = 1, rise = 0):
    return hpgl.relativeDirection(run, rise)
            
def selectAltCharSet():
    return hpgl.selectAltCharSet()

def symbolMode( char = None):
    return hpgl.symbolMode(char)

def selectStandardCharSet():
    return hpgl.selectStandardCharSet()



"""
    DRAWING PRIMITIVES & SETTINGS
"""
    
def arcAbsolute(x, y, aa, ca = 5):
    return hpgl.arcAbsolute(x, y, aa, ca)

def arcRelative(x, y, aa, ca = 5):
    return hpgl.arcRelative(x, y, aa, ca)
    
def chordTolerance(type = 0):
    return hpgl.chordTolerance(type)

def circle(rad, ca = 5):
    return hpgl.circle(rad, ca)

def curvedLineGenerator(n = None, inputDelay = None):
    return hpgl.curvedLineGenerator(n, inputDelay)

def edgePolygon():
    return hpgl.edgePolygon()

def edgeRectRelative(x, y):
    return hpgl.edgeRectRelative(x,y)

def edgeRectAbsolute(x, y):
    return hpgl.edgeRectAbsolute(x,y)

def edgeWedge(r, sa, swa, ca=5):
    return hpgl.edgeWedge(r, sa, swa, ca)

def fillPolygon():
    return hpgl.fillPolygon()

def fillRectAbsolute(x, y):        
    return shadeRectAbsolute(x, y)  

def fillRectRelative(x, y):        
    return shadeRectRelative(x, y)  
            
def fillType(type=1, space=None,  angle=0):
    return hpgl.fillType(type, space, angle)

def lineAbsolute(x1, y1, x2, y2):
    out = penUp()
    out += plotAbsolute((x1, y1))
    out += penDown()
    out += plotAbsolute((x2, y2))
    out += penUp()
    return out

def lineRelative(x, y):
    out = penDown()
    out += goto(x, y)
    out += penUp()
    return out

def lineType(patNum, patLength = 4):
    return hpgl.lineType(pattype, patlength)

def plotPolygon(n = 0):
    return hpgl.plotPolygon(n)
    
def polyLineAbsolute(array):
    out = penDown()
    out += plotAbsolute(array)
    out += penUp()
    return out

def polyLineRelative(array):
    out = penDown()
    out += plotRelative(array)
    out += penUp()
    return out

def shadeRectAbsolute(x, y):        
    return hpgl.shadeRectAbsolute(x, y)

def shadeRectRelative(x, y):
    return hpgl.shadeRectRelative(x, y)

def shadeWedge(r, sa, swa, ca = 5):
    return hpgl.shadeWedge(r, sa, swa, ca)



"""
    DIRECT PEN CONTROL & INFO
"""

def accelSelect(accel = None, pen = None):
    return hpgl.accelSelect(accel, pen)
    

def forceSelect(force = None, pen = None):
    return hpgl.forceSelect(force, pen)
    
def goto(x, y):
    """Alias for plotAbsolute() with only one point"""
    return plotAbsolute((x, y))

def nudge(x, y):
    """Alias for plotRelative() with only one x,y pair."""
    return plotRelative((x,y))

def outputActualPosition():
    return hpgl.outputActualPosition()

def outputCommandedPosition():
    return hpgl.outputCommandedPosition()
            
def plotAbsolute(coords = None):
    """
        Plot Absolute.
        Takes a tuple of any number of sets of points:
        (0,0,100,100,2500,1000) will go to three different points:
            0,0 100,100 2500,1000
    """
    return hpgl.plotAbsolute(coords)

def plotRelative(coords = None):
    """
        Plot Relative.
        Takes a tuple of any number of sets of points:
        (0,0,100,100,2500,1000) will go to three different points:
            0,0 100,100 2500,1000
    """
    return hpgl.plotRelative(coords)

def penDown(coords = None):
    """Pen Down."""
    return hpgl.penDown(coords)

def pd():
    """Alias for penDown()"""
    return penDown()

def penThickness(thickness = 0.3):
    return hpgl.penThickness(thickness)
    
def penUp(coords = None):
    """Pen Up."""
    return hpgl.penUp(coords)

def pu():
    """Alias for penUp()"""
    return penUp()

def selectPen(penNum = 0):
    return hpgl.selectPen(penNum)
    
#def sp(penNum = 0):
#    self.selectPen(penNum)
sp = selectPen

def tickLength(tp = 0.5, tn = 0.5):
    return hpgl.tickLength(tp, tn)

def xTick():
    return hpgl.xTick()

def yTick():
    return hpgl.yTick()       
                
def velocitySelect(v = None, pen = None):
    """ Set pen's velocity."""
    return hpgl.velocitySelect(v, pen)



        
def inputP1P2(p1x = None, p1y = None, p2x = None, p2y = None):
    return hpgl.inputP1P2(p1x, p1y, p2x, p2y)

def inputWindow(xLL = None, yLL = None, xUR = None, yUR = None):
    return hpgl.inputWindow(xLL, yLL, xUR, yUR)

def outputHardClipLimits():
    return hpgl.outputHardClipLimits()

def outputP1P2():
    return hpgl.outputP1P2()

def outputWindow():
    return hpgl.outputWindow()

def paperSize(size = None):
    return hpgl.paperSize(size)

    
def rotateCoordSystem(angle = 0):
    return hpgl.rotateCoordSystem(angle)
    
rotate = rotateCoordSystem

def scale(xMin, xMax, yMin, yMax):
    return hpgl.scale(xMin, xMax, yMin, yMax)
        

"""
    PAPER CONTROLS
"""

def advanceFrame():
    return hpgl.advanceFrame()
    
def advanceFullPage():
    return hpgl.advanceFullPage()
    
def advanceHalfPage():
    return hpgl.advanceHalfPage()  

def enableCutLine(n):
    return hpgl.enableCutLine(n)

def pageFeed(n = None):
    return hpgl.pageFeed(n)



"""
    DIGITIZER CONTROLS
"""
def clearDigitizer():
    return hpgl.clearDigitizer()
    
def digitizePoint():
    return hpgl.digitizePoint()

def outputDigiPoint():
    return hpgl.outputDigiPoint()




"""
    MISC I/O, PLOTTER QUERIES, ERRORS, SETUP
"""

def abortCommand():
    """Tells the plotter to discard commands in its buffer."""
    return hpgl.abortCommand()

def automaticPen(p = None):
    return hpgl.automaticPen(p)

def bufferPlot():
    return hpgl.bufferPlot()

def defaultInstruction():
    return hpgl.defaultInstruction()

def defineKey(key = None, function = None):
    return hpgl.defineKey()

    
def initialize():
    """Initialize plotter."""
    return hpgl.initialize()

def inputMask(e = 233, s = 0, p = 0):
    return hpgl.inputMask(e, s, p)

def notReady():
    return hpgl.notReady()
    
def outputError():
    return hpgl.outputError()

def outputID():
    return hpgl.outputID()

def outputKey():
    return hpgl.outputKey()

def outputOptions():
    return hpgl.outputOptions()

def outputStatus():
    return hpgl.outputStatus()

def outputCarouselType():
    return hpgl.outputCarouselType()

def replot(n = 1):
    return hpgl.replot(n)
    
def writeToDisplay(text):
    return hpgl.writeToDisplay(text)



"""
    DCI (Device Control Instructions) escape commands ----------------------------
"""

def escapePlotterOn():
    return hpgl.escapePlotterOn() 

def escapeHS2(minbytes=81, xon='17'):
    return hpgl.escapeHS2(minbytes, xon)

def escapeXoff(xoff='19', interchar_speed=0):
    return hpgl.escapeXoff(xoff, interchar_speed)



