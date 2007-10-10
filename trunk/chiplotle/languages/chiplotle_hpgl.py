
"""
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
"""

from hpgl import *
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

    out = penUp()
    out += plotAbsolute((x, y))
    out += plotAbsolute((x + tl[0], y + tl[1]))
    out += penDown()
    out += plotAbsolute((x + tr[0], y + tr[1]))
    out += plotAbsolute((x + br[0], y + br[1]))
    out += plotAbsolute((x + bl[0], y + bl[1]))
    out += plotAbsolute((x + tl[0], y + tl[1]))
    out += penUp()

    return out

def edgeCircle(x, y, rad):
    out = penUp()
    out += plotAbsolute((x, y))
    out += circle(rad)
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


def lineAbsolute(x1, y1, x2, y2):
    out = penUp()
    out += plotAbsolute((x1, y1))
    out += penDown()
    out += plotAbsolute((x2, y2))
    out += penUp()
    return out

def lineRelative(x, y):
    out = penDown()
    out += positionRelative(x, y)
    out += penUp()
    return out

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

def goto(x, y):
    """Alias for plotAbsolute() with only one point"""
    return plotAbsolute((x, y))

def nudge(x, y):
    """Alias for plotRelative() with only one x,y pair."""
    return plotRelative((x,y))

pd = penDown
pu = penUp

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
        
    #print "out: ", out

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

def plotFile(filename):
    """Open file [filename] and return its content.  """
    f = open(filename)
    fs = f.read()
    #fs = fs.replace('\n', '')
    #fs = fs.replace('\r', '')
    f.close()
    return fs

