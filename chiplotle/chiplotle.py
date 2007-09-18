"""
 *  Copyright 2007 Douglas Repetto and Victor Adan
 *
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
 *
 *  chiplotlib is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License version 2 as
 *  published by the Free Software Foundation.
 *
 *  chiplotlib is distributed in the hope that it will be useful, but
 *  WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 *  General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with chiplotle; if not, write to the Free Software
 *  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 *  02110-1301 USA
 *
 *  See the file "COPYING" for the text of the license.
"""

import serial
import chiplotle_hpgl
import sys
import time
import random
import math


"""
    chiplotle is an open source pen plotter control project. 

"""

class Plotter(object):

    """ 
        STARTUP ROUTINE 
    """
    def __init__(self, ser, lang='hpgl', writeToSerial = True, 
        writeToFile = False, defaultFileName = "default.hpgl", 
        xoff='1', xon='0'):
        
        #Victor, how should we handle the version???
        self.versionString = "chiplotle v.9"
        
        
        if lang == 'hpgl':
            self.lang = chiplotle_hpgl.Hpgl()
        else:
            print "Don't know language [%s]. Try another." % lang
            sys.exit(2)
        

        self.writeToSerial = writeToSerial
        self.writeToFile = writeToFile
        self.outputFilename = defaultFileName
        self.outputFile = ""
        
        self.ser = ser
        
        if self.writeToSerial:
            self.ser.flushInput()
            self.ser.flushOutput()
        
            #print "doing escapePlotterOn()"
            self.escapePlotterOn()
            #print "doing initialize()"
            self.initialize()
        
        #print "doing getPlotterID()"
        self.plotterID = self.getPlotterID()
        #print "got ID: " + self.plotterID
        
        self.xoff = xoff
        self.xon = xon

        #print "doing getHardMargins()"
        self.marginsHard = self.getHardMargins()
        #print "doing getSoftMargins()"
        self.marginsSoft = self.getSoftMargins()


    
    """
        TEXT OUTPUT & SETTINGS
    """
        
    def absCharSize(self, w = None, h = None):
        self._writePort(self.lang.absCharSize(w, h))

    def absoluteDirection(self, run = 1, rise = 0):
        self._writePort(self.lang.absoluteDirection(run, rise))
        
    def altCharSet(self, n = 0):
        self._writePort(self.lang.altCharSet(n))

    def charChordAngle(self, angle = 5):
        self._writePort(self.lang.charChordAngle(angle))
        
    def bufferLabel(self, text = None):
        self._writePort(self.lang.bufferLabel(text))
    
    def charPlot(self, spaces = None, lines = None):
        self._writePort(self.lang.charPlot(spaces, lines))

    def charSelectionMode(self, switch = 0, fallback = 0):
        self._writePort(self.lang.charSelectionMode(switch, fallback))
        
    def charSet(self, set = 0):
        self._writePort(self.lang.charSet(set))        

    def charSlant(self, angle = 0):
        tan = angle * 2 * math.pi / 360.
        self._writePort(self.lang.charSlant(tan))
        
    def defineLabelTerminator(self, t = chr(3)):
        self._writePort(self.lang.defineLableTerminator(t))
    
    def directionVertical(self, dir = 0):
        self._writePort(self.lang.directionVertical(dir))

    def extraSpace(self, spaces = 0, lines = 0):
        self._writePort(self.lang.extraSpace(spaces, lines))

    def invokeCharSlant(self, slot = 0, left = None):
        self._writePort(self.lang.invokeCharSlant(slote, left))
    
    def label(self, text):
        #print "label got: %s" % text
        self._writePort(self.lang.label(text))

    def labelOrigin(self, positionNum = 1):
        self._writePort(self.lang.labelOrigin(positionNum))
        
    def newLine(self):
        """
            Alias for charPlot()
            Move down one line and back to the left margin
        """
        self.charPlot()

    def outputLabelLength(self):
        self._writePort(self.lang.outputLabelLength())
        
    def plotText(self, text, b=-1, h=-1, angle=0, char_s=0, line_s=0, chunk=10):
        """Print text ."""
        #print "plotText got: " + text
        # replace all \n by \n\r
        text = text.replace('\n','\n\r')
        if b >= 0:
            if h >= 0:
                self.absCharSize(b, h)
        self.charSlant(angle)   
        self.charPlot(char_s, line_s)
        for i in range(0, len(text), chunk):
            self.label(text[i:i+chunk])

    def plotTextFile(self, filename, pen=-1):
        """Open and print the txt file.
        If pen argument is passed, select that pen
        """
        f = open(filename)

        if pen >= 0:
            self.selectPen(pen)

        for line in f:
            self.plotText(line)

    def printBufferedLabel(self):
        self._writePort(self.lang.printBufferedLabel())
        
    def relCharSize(self, w = None, h = None):
        self._writePort(self.lang.relCharSize(w, h))

    def relativeDirection(self, run = 1, rise = 0):
        self._writePort(self.lang.relativeDirection(run, rise))
                
    def selectAltCharSet(self):
        self._writePort(self.lang.selectAltCharSet())

    def symbolMode(self, char = None):
        self._writePort(self.lang.symbolMode(char))

    def selectStandardCharSet(self):
        self._writePort(self.lang.selectStandardCharSet())
    
    
    
    """
        DRAWING PRIMITIVES & SETTINGS
    """
        
    def arcAbsolute(self, x, y, aa, ca = 5):
        self._writePort(self.lang.arcAbsolute(x, y, aa, ca))
    
    def arcRelative(self, x, y, aa, ca = 5):
        self._writePort(self.lang.arcRelative(x, y, aa, ca))
        
    def chordTolerance(self, type = 0):
        self._writePort(self.lang.chordTolerance(type))

    def circle(self, rad, ca = 5):
        self._writePort(self.lang.circle(rad, ca))

    def curvedLineGenerator(self, n = None, inputDelay = None):
        self._writePort(self.lang.curvedLineGenerator(n, inputDelay))

    def edgePolygon(self):
        self._writePort(self.lang.edgePolygon())
    
    def edgeRectRelative(self, x, y):
        self._writePort(self.lang.edgeRectRelative(x,y))
 
    def edgeRectAbsolute(self, x, y):
        self._writePort(self.lang.edgeRectAbsolute(x,y))

    def edgeWedge(self, r, sa, swa, ca=5):
        self._writePort(self.lang.edgeWedge(r, sa, swa, ca))

    def fillPolygon(self):
        self._writePort(self.lang.fillPolygon())

    def fillRectAbsolute(self, x, y):        
        self.shadeRectAbsolute(x, y)  

    def fillRectRelative(self, x, y):        
        self.shadeRectRelative(x, y)  
                
    def fillType(self, type=1, space=None,  angle=0):
        self._writePort(self.lang.fillType(type, space, angle))

    def lineAbsolute(self, x1, y1, x2, y2):
        self.penUp()
        self.plotAbsolute(x1, y1)
        self.penDown()
        self.plotAbsolute(x2, y2)
        self.penUp()

    def lineRelative(self, x, y):
        self.penDown()
        self.goto(x, y)
        self.penUp()

    def lineType(self, patNum, patLength = 4):
        self._writePort(self.lang.lineType(pattype, patlength))

    def plotPolygon(self, n = 0):
        self._writePort(self.lang.plotPolygon(n))
        
    def polyLine(self, array, rel=True):
        """Draws multisegment line. 
        array:  2d-array. May be a list of length 2 lists, or an n*2 numeric array.
        rel:    if True, numbers in array are interpreted as relative positions, otherwise as absolute."""

        self.penDown()
        for p in array:
            if rel:
                self.goto(p[0], p[1])
            else:
                self.plotAbsolute(p[0], p[1])
        self.penUp()

    def shadeRectAbsolute(self, x, y):        
        self._writePort(self.lang.shadeRectAbsolute(x, y))
    
    def shadeRectRelative(self, x, y):
        self._writePort(self.lang.shadeRectRelative(x, y))

    def shadeWedge(self, r, sa, swa, ca = 5):
        self._writePort(self.lang.shadeWedge(r, sa, swa, ca))



    """
        DIRECT PEN CONTROL & INFO
    """
    
    def accelSelect(self, accel = None, pen = None):
        self._writePort(self.lang.accelSelect(accel, pen))
        
    def currLoc(self, hard = True):
        self.ser.flushInput()
        self._writePort(self.lang.outputActualPosition())
        loc = self._readPort()
        while len(loc) == 0:
            self.ser.flushInput()
            self._writePort(self.lang.outputActualPosition())
            loc = self._readPort()
        return loc

    def forceSelect(self, force = None, pen = None):
        self._writePort(self.lang.forceSelect(force, pen))
        
    def goto(self, x, y):
        """Alias for plotAbsolute() with only one point"""
        self.plotAbsolute((x, y))
    
    def gotoC(self, hard = True):
        self.goto(self.centerX(hard), self.centerY(hard))
        
    def gotoBL(self, hard = True):
        self.goto(self.left(hard), self.bottom(hard))        
        
    def gotoBR(self, hard = True):
        self.goto(self.right(hard), self.bottom(hard)) 

    def gotoTL(self, hard = True):
        self.goto(self.left(hard), self.top(hard))        
        
    def gotoTR(self, hard = True):
        self.goto(self.right(hard), self.top(hard))        

    def nudge(self, x, y):
        """Alias for plotRelative() with only one x,y pair."""
        self.plotRelative((x,y))

    def outputActualPosition(self):
        self._writePort(self.lang.outputActualPosition())

    def outputCommandedPosition(self):
        self._writePort(self.lang.outputCommandedPosition())
                
    def plotAbsolute(self, coords = None):
        """
            Plot Absolute.
            Takes a tuple of any number of sets of points:
            (0,0,100,100,2500,1000) will go to three different points:
                0,0 100,100 2500,1000
        """
        self._writePort(self.lang.plotAbsolute(coords))

    def plotRelative(self, coords = None):
        """
            Plot Relative.
            Takes a tuple of any number of sets of points:
            (0,0,100,100,2500,1000) will go to three different points:
                0,0 100,100 2500,1000
        """
        self._writePort(self.lang.plotRelative(coords))

    def penDown(self, coords = None):
        """Pen Down."""
        self._writePort(self.lang.penDown(coords))

    def pd(self):
        """Alias for penDown()"""
        self.penDown()

    def penThickness(self, thickness = 0.3):
        self._writePort(self.lang.penThickness(thickness))
        
    def penUp(self, coords = None):
        """Pen Up."""
        self._writePort(self.lang.penUp(coords))

    def pu(self):
        """Alias for penUp()"""
        self.penUp()
    
    def selectPen(self, penNum = 0):
        self._writePort(self.lang.selectPen(penNum))
        
    def sp(self, penNum = 0):
        self.selectPen(penNum)

    def tickLength(self, tp = 0.5, tn = 0.5):
        self._writePort(self.lang.tickLength(tp, tn))

    def xTick(self):
        self._writePort(self.lang.xTick())

    def yTick(self):
        self._writePort(self.lang.yTick())        
                    
    def velocitySelect(self, v = None, pen = None):
        """ Set pen's velocity."""
        self._writePort(self.lang.velocitySelect(v, p))
    



    """
        PAGE SIZE, MARGINS, CLIPPING, ROTATION
    """

    def bottom(self, hard = True):
        """Get lowest coordinate."""
        if hard:
            return self.marginsHard[1]
        else:
            return self.marginsSoft[1]

    def centerX(self, hard = True):
        """Get center point X."""
        if hard:
            return (self.right() - self.left()) / 2
        else:
            return (self.right(false) - self.left(false)) / 2
            
    def centerY(self, hard = True):
        """Get center point Y."""
        if hard:
            return (self.top() - self.bottom()) / 2
        else:
            return (self.top(false) - self.bottom(false)) / 2

    def centerPoint(self, hard = True):
        """Get center point X."""
        if hard:
            return tuple([self.centerX(), self.centerY()])
        else:
            return tuple([self.centerX(false), self.centerY(false)])            
            
    def getHardMargins(self):
        """Get margins of paper."""
        if self.writeToSerial:
            self.ser.flushInput()
            self._writePort(self.lang.outputHardClipLimits())
            m = self._readPort()
            while len(m) < 9:
                self.ser.flushInput()
                self._writePort(self.lang.outputHardClipLimits())
                m = self._readPort()
            m = m.split(',')
            m = tuple([int(n) for n in m])
            return m
        else:
            return (tuple([0, 0, 10870, 7600]))

    def getSoftMargins(self):
        """Get margins of paper."""
        if self.writeToSerial:
            self.ser.flushInput()
            self._writePort(self.lang.outputP1P2())
            m = self._readPort()
            while len(m) < 9:
                self.ser.flushInput()
                self._writePort(self.lang.outputP1P2())
                m = self._readPort()
            m = m.split(',')
            m = tuple([int(n) for n in m])
            return m
        else:
            return (tuple([0, 0, 10870, 7600]))
            
    def inputP1P2(self, p1x = None, p1y = None, p2x = None, p2y = None):
        self._writePort(self.lang.inputP1P2(p1x, p1y, p2x, p2y))
        #print "doing getHardMargins()"
        self.marginsHard = self.getHardMargins()
        #print "doing getSoftMargins()"
        self.marginsSoft = self.getSoftMargins()

    def inputWindow(self, xLL = None, yLL = None, xUR = None, yUR = None):
        self._writePort(self.lang.inputWindow(xLL, yLL, xUR, yUR))
        #print "doing getHardMargins()"
        self.marginsHard = self.getHardMargins()
        #print "doing getSoftMargins()"
        self.marginsSoft = self.getSoftMargins()

    def left(self, hard = True):
        """Get leftmost coordinate."""
        if hard:
            return self.marginsHard[0]
        else:
            return self.marginsSoft[0]

    def outputHardClipLimits(self):
        self._writePort(self.lang.outputHardClipLimits())

    def outputP1P2(self):
        self._writePort(self.lang.outputP1P2())

    def outputWindow(self):
        self._writePort(self.lang.outputWindow())

    def paperSize(self, size = None):
        self._writePort(self.lang.paperSize(size))
        #print "doing getHardMargins()"
        self.marginsHard = self.getHardMargins()
        #print "doing getSoftMargins()"
        self.marginsSoft = self.getSoftMargins()

    def right(self, hard = True):
        """Get rightmost coordinate."""
        if hard:
            return self.marginsHard[2]
        else:
            return self.marginsSoft[2]

    def rotate(self, angle = 0):
        self.rotateCoordSystem(angle)
        #print "doing getHardMargins()"
        self.marginsHard = self.getHardMargins()
        #print "doing getSoftMargins()"
        self.marginsSoft = self.getSoftMargins()
        
    def rotateCoordSystem(self, angle = 0):
        self._writePort(self.lang.rotateCoordSystem(angle))
        
    def scale(self, xMin, xMax, yMin, yMax):
        self._writePort(self.lang.scale(xMin, xMax, yMin, yMax))
        #print "doing getHardMargins()"
        self.marginsHard = self.getHardMargins()
        #print "doing getSoftMargins()"
        self.marginsSoft = self.getSoftMargins()
            
    def top(self, hard = True):
        """Get top coordinate."""
        if hard:
            return self.marginsHard[3]
        else:
            return self.marginsSoft[3]


    """
        PAPER CONTROLS
    """

    def advanceFrame(self):
        self._writePort(self.lang.advanceFrame())
        
    def advanceFullPage(self):
        self._writePort(self.lang.advanceFullPage())
        
    def advanceHalfPage(self):
        self._writePort(self.lang.advanceHalfPage())   

    def enableCutLine(self, n):
        self._writePort(self.lang.enableCutLine(n))

    def pageFeed(self, n = None):
        self._writePort(self.lang.pageFeed(n))



    """
        DIGITIZER CONTROLS
    """
    def clearDigitizer(self):
        self._writePort(self.lang.clearDigitizer())
        
    def digitizePoint(self):
        self._writePort(self.lang.digitizePoint())

    def outputDigiPoint(self):
        self._writePort(self.lang.outputDigiPoint())




    """
        MISC I/O, PLOTTER QUERIES, ERRORS, SETUP
    """
    
    def abortCommand(self):
        """Tells the plotter to discard commands in its buffer."""
        self._writePort(self.lang.abortCommand())
	
    def automaticPen(self, p = None):
        self._writePort(self.lang.automaticPen(p))

    def bufferPlot(self):
		self._writePort(self.lang.bufferPlot())

    def defaultInstruction(self):
        self._writePort(self.lang.defaultInstruction())

    def defineKey(self, key = None, function = None):
        self._writePort(self.lang.defineKey())

    def getError(self):
        self.ser.flushInput();
        self._writePort(self.lang.extendedError())
        err = self._readPort()
        while len(err) == 0:
            self.ser.flushInput()
            err = self._readPort()
        return self._readPort()
        
    def getPlotterID(self):
        """Get name of plotter being used."""
        if self.writeToSerial:
            #print "getPlotterID()"
            self.ser.flushInput()
            self._writePort(self.lang.outputID())
            id = self._readPort(100)
        
            while len(id) == 0:
                #print "len == 0, trying again..."
                self.ser.flushInput()
                self._writePort(self.lang.outputID())
                id = self._readPort(100)
            
            #print "got %d bytes" % len(id)
            return id.strip('\r')
        else:
            return "offline plotter"
        
    def initialize(self):
        """Initialize plotter."""
        self._writePort(self.lang.initialize())

    def inputMask(self, e = 233, s = 0, p = 0):
        self._writePort(self.lang.inputMask(e, s, p))

    def notReady(self):
        self._writePort(self.lang.notReady())
        
    def outputError(self):
        self._writePort(self.lang.outputError())

    def outputID(self):
        self._writePort(self.lang.outputID())

    def outputKey(self):
        self._writePort(self.lang.outputKey())

    def outputOptions(self):
        self._writePort(self.lang.outputOptions())

    def outputStatus(self):
        self._writePort(self.lang.outputStatus())

    def outputCarouselType(self):
        self._writePort(self.lang.outputCarouselType())

    def replot(self, n = 1):
        self._writePort(self.lang.replot(n))
        
    def writeToDisplay(self, text):
        self._writePort(self.lang.writeToDisplay(text))




    """
        PLOTTING UTILITIES & TESTS
    """
    
    def asciiArt(self, text, char_size, compensation = 1):
        h = char_size * 5/4.
        if compensation:
            h *= 5/4.
        self.plotText(text, char_size, h, 0, 0, -0.3)      

    def decrudPlotterLine(self, input):
        """
            Removes strange commands that cause us sadlies.
            input is a string of commands.
        """
        
        #print "input: " + input        
        parts = input.split(';')
        
        output = ""
        
        #Now go through each command to see if we keep it.
        for command in parts:

            good = False
        
            if command.startswith(self.lang.allowedCommands):
                good = True
            
            if good == True:
                output += command + ";"
                
        #print "output: " + output
        return output
        
    def eatPlotterCommand(self, input, commandToEat):
        """
            Removes a particular command from a command string.
            input is a string of commands.
            commandToEat is a string containing one unwanted command, like "PW" in HPGL
        """
        
        #print "input: " + input

        parts = input.split(';')
        
        output = ""
        
        for command in parts:
            good = True
            if command.startswith(commandToEat):
                good = False
                print "removing command: " + command
                
            if good == True:
                output += command
                output += ";"
        
        #print "output: " + output
        return output    
    
    def eatPlotterLine(self, input, commandToEat):
        """
            If line starts with commandToEat, the line is eaten. 
            Otherwise it is returned unharmed. 
            input is a string of commands.
            commandToEat is a string containing one unwanted command, 
            like the mysterious "PW" put out by some translators that's 
            not a real HPGL command.
        """
        
        if input.startswith(commandToEat):
            print "eating line: " + input
            return ""
        else:
            return input
    
    def plotFile(self, filename, decrud = True):
        """Open and plot the file one line at a time."""
        f = open(filename)

        for line in f:
            if decrud:
                self.sendCode(self.decrudPlotterLine(line))
            else:
                self.sendCode(line);  

    def plotFileLineByLine(self, filename, decrud = True):
        """Open and plot the file one line at a time, 
            waiting until the buffer is empty after sending
            each line. This is useful for debugging plotter
            files
        """
        f = open(filename)

        for line in f:
                
            if len(line) > 1000:
                print "line too long! %d" % len(line)
                return
                
            space = self.bufferSpace()
            print "space: %d" % space
            
            while space < 1024:
                space = self.bufferSpace()
                print "waiting for buffer to clear: %d" % space
                
            if decrud:
                print "sending: %s" % self.decrudPlotterLine(line)
                self.sendCode(self.decrudPlotterLine(line))
                
            else:
                print "sending: %s" % line
                self.sendCode(line);  
    
    def randomWalk(self, steps=100, step_size_var=500):
        self.goto(self.centerXHard, self.centerYHard)
        self.penDown()
        for i in range(steps):
            r = random.randint(1, step_size_var)
            A = random.random() * math.pi * 2
            (x,y) = polar2xy(r,A)
            self.goto(x, y)
            self.sleepWhileBufferFull()
        self.penUp()

    def selfTest(self):
        """Prints the ID of the plotter in the center of the page"""
        #print "getting pen 1"
        self.sp(1)
        #print "going to center"
        self.gotoC()
        #print "getting ID"
        #id = self.plotterID
        #print "plotting id"
        self.plotText(self.plotterID)
        #print "putting back pen"
        self.sp(0)
           
 


    """
        SERIAL AND FILE I/O
    """

    def bufferSpace(self):
        self.ser.flushInput()
        self._writePortControl(self.lang.escapeOutputBufferSpace())
        #Can we always assume 4 bytes? I think so. -dr
        bspace = self._readPort(4)
        while len(bspace) == 0:
            self.ser.flushInput()
            self._writePortControl(self.lang.escapeOutputBufferSpace())
            bspace = self._readPort(4)
        
        #print "buffer space: ", bspace
        
        # if len > 5 we probably have some garbage on the end...
        if len(bspace) > 5:
            return 0
        else:
            return int(bspace)

    def cleanup(self):
        """ closes serial port & file """
        if self.writeToSerial:
            self.ser.close()
        if self.writeToFile:
            self.stopFileOutput()

    def _readByte(self):
        byte = self.ser.read()
        return byte

    def _readPort(self, numBytes = 100):
        """Read numBytes from the serial port"""
        #print "waiting for %d bytes..." % numBytes
        return self.ser.read(numBytes)

    def sendCode(self, code):            
        code = code.replace('\n',';@')
        code_lines = code.split('@')
        #print code_lines
        for c in code_lines:
            self._writePort(c)
            self.sleepWhileBufferFull()
    
    def startFileOutput(self):
        #self.outputFilename = filename
        #self.writeToFile = True
        self.outputFile = open(self.outputFilename, 'w')
        
    def stopFileOutput(self):    
        self.writeToFile = False
        self.outputFile.close()
                
    def sleepWhileBufferFull(self):
        """
            sleeps until the buffer has some room in it.
        """
        space = self.bufferSpace()  
        if space < 250:
            print 'Buffer getting full, sleeping...'
            while True:
                time.sleep(1)
                space = self.bufferSpace()  
                if space >= 1000:
                    print 'Okay, now buffer has room...'
                    break
    
    def _writePort(self, data):
        """
            Write data to serial port
            Optionally write same data to a file
            
            NEW: if the data is larger than the available buffer space
            we break it up into chunks!
        """
        if self.writeToSerial:
            #print "writing normal message..."
            #print "_writePort got %s" % data
            dataLen = len(data)
            dataSpace = self.bufferSpace()
            
            #print "total command length: %d" % dataLen
            #print "free buffer space: %d" % dataSpace
            
            # uh oh, not enough space!
            if dataLen > dataSpace:        
                print "uh oh, too much data!"
                numChunks = (dataLen / 1000) + 1

                for i in range(numChunks):
                    self.sleepWhileBufferFull()
                    
                    start = i * 1000
                    end = start + 1000
                    
                    self.ser.write(data[start:end])            
            
            # buffer space is fine, just send it as is!
            else:
                self.ser.write(data)
                        
            #print "done writing to port..."
        
        if self.writeToFile:
            #print "writing to file: " + data
            self.outputFile.write(data)
    
    def _writePortControl(self, data):
        """
            NOTE:  you need to use this function to send control
            messages. If you use the normal _writePort function 
            you will spiral into an infinite loop and will never
            return. YOU HAVE BEEN WARNED!!!
            
            We assume that the buffer has space for a few bytes
            of control data...
        """
        if self.writeToSerial:
            #print "writing control message..."
            self.ser.write(data)
    
        

    
    """
        DCI (Device Control Instructions) escape commands ----------------------------
    """

    def escapePlotterOn(self):
        self._writePortControl( self.lang.escapePlotterOn() )

    def escapeHS2(self, minbytes=81, xon='17'):
        self._writePortControl(self.lang.escapeHS2(minbytes, xon))
        self.xon = str(xon) 
    
    def escapeXoff(self, xoff='19', interchar_speed=0):
        self._writePortControl(self.lang.escapeXoff(xoff, interchar_speed))
        self.xoff = str(xoff)



#####################################################################
# utility functions

def polar2xy(r, A):
    x = r * math.cos(A)
    y = r * math.sin(A)
    return (x, y)

    
    
