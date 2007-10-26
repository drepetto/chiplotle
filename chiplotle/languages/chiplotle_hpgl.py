
"""
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
"""

from hpgl import *
import math
from utils import *
import random
import re

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

def newLine():
    """
        Alias for charPlot()
        Move down one line and back to the left margin
    """
    return charPlot()
        
pd = penDown
pu = penUp


def plotAsciiArt(text, width, height=None, char_spacing=None, line_spacing=-0.3, wiggle=0):
    if not height:
        height = width * 5/4.

    # replace all \n by \n\r
    text = text.replace('\n','\r')

    # parse text for spaces
    charlist = []
    parsed = []
    for t in text:
        charlist.append(t)
    
    while len(charlist) > 0:
        c = charlist.pop(0)
        if c == ' ':
            spaces = ' '
            while len(charlist) > 0 and charlist[0] == ' ':
                spaces += ' '
                charlist.pop(0)
            parsed.append(spaces)
        else:
            parsed.append(c)
    print parsed


    
    out = ''
    out += absCharSize(width, height)

    for c in parsed:
        if c.startswith(' '):
            out += charPlot(len(c), 0)
            if char_spacing:
                out += charPlot(len(c) * char_spacing, 0)

        elif c == '\r':
            out += label(c)
            out += charPlot(0, line_spacing)
        else:
            out += label(c)
            w = random.gauss(0,wiggle)
            if char_spacing:
                out += charPlot(char_spacing + w, 0 + w)

    return out    


def plotText(text, width=None, height=None, angle=None):
    """Print text ."""
    out = ''
    # replace all \n by \n\r
    text = text.replace('\n','\n\r')

    if width and height:
        out += absCharSize(width, height)

    if angle:
        out += charSlant(angle)   

    out += label(text)

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
    #need to eat these, otherwise they look like commands...
    fs = fs.replace('\n', '')
    fs = fs.replace('\r', '')
    f.close()
    return fs

