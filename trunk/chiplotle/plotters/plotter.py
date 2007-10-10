

"""
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
"""

import sys
sys.path += ['../']
import serial
from languages import chiplotle_hpgl
import time


"""
    chiplotle is an open source pen plotter control project. 

"""

class Plotter(object):

    """ 
        STARTUP ROUTINE 
    """
    def __init__(self, ser, **kwargs):

        self.type = 'Generic'
        self.ser = ser
        self.memory = []
        
        self.lang = chiplotle_hpgl
        if kwargs.has_key('lang'):
            self.lang = kwargs['lang']
            kwargs.pop('lang')

        self.xoff = '1'
        if kwargs.has_key('xoff'):
            self.xoff = kwargs['xoff']
            kwargs.pop('xoff')

        self.xon = '0'
        if kwargs.has_key('xon'):
            self.xon = kwargs['xon']
            kwargs.pop('xon')
        
# Only these commands will be sent to the plotter. All other will be eaten. Burp.
        self.allowedHPGLCommands = tuple([
        '\x1b.', 'AA','AR','CA','CI','CP','CS','DC','DF','DI','DP','DR','DT',
        'EA','ER','EW','FT','IM','IN','IP','IW','LB','LT','OA','OC',
        'OD','OE','OF','OH','OI','OO','OP','OS','OW','PA','PD','PR',
        'PS','PT','PU','RA','RO','RR','SA','SC','SI','SL','SM','SP',
        'SR','SS','TL','UC','VS','WG','XT','YT'])

        self.initializePlotter()


    def initializePlotter(self):
        self.ser.flushInput()
        self.ser.flushOutput()
    
        self._writePort(self.lang.escapePlotterOn())
        self._writePort(self.lang.initialize())
        
        #self.ser.write(self.lang.escapeHS2(100, self.xon))
        #self.ser.write(self.lang.escapeXoff(self.xoff))

        self.refreshMarginsHard()
        self.refreshMarginsSoft()

    @property
    def id(self):
        """Get name of plotter being used."""
        self.ser.flushInput()
        self._writePort(self.lang.outputID())
       
        id = self._readPort()
        return id.strip('\r')


    def _writePort(self, data):
        """ Write data to serial port """
        #print "_writePort data in: %s", data
        data = self.filterCommands(data)
        #print "_writePort after filtering: %s" % data

        self.memory.append(data)

        self.semaphoreBuffer(data)
        #or,  write directly...
        #self.ser.write(data)


    write = _writePort

    def semaphoreBuffer(self, data):
        """ If the data is larger than the available buffer space we break it up into chunks!  """
        dataLen = len(data)
        bufferSpace = self.bufferSpace()
        #print "total command length: %d" % dataLen
        # uh oh, not enough space!
        if dataLen > bufferSpace:        
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
        

    def _writePortControl(self, data):
        """
            NOTE:  you need to use this function to send control
            messages. If you use the normal _writePort function 
            you will spiral into an infinite loop and will never
            return. YOU HAVE BEEN WARNED!!!
            
            We assume that the buffer has space for a few bytes
            of control data...
        """
        #print "writing control message..."
        self.ser.write(data)
    

    def sleepWhileBufferFull(self):
        """
            sleeps until the buffer has some room in it.
        """
        space = self.bufferSpace()  
        if space < 1000:
            print 'Buffer getting full, sleeping...'
            while True:
                time.sleep(1)
                space = self.bufferSpace()  
                if space >= 1000:
                    print 'Okay, now buffer has room...'
                    break

    def _readByte(self):
        byte = self.ser.read()
        return byte

    def _readPort(self):
        """Read data from the serial port"""

        #print '_readPort: Reading from port...'
        while self.ser.inWaiting() == 0:
            pass

        m = ''
        input = 'xxx'
        while input != '':
            input = self._readByte()
            m += input

        return m

    
    
    def getError(self):
        self.ser.flushInput();
        self._writePort(self.lang.extendedError())
        
        err = self._readPort()
        return err
    
    def bufferSpace(self):
        #print "getting bufferSpace..."
        self.ser.flushInput()
        self._writePortControl(self.lang.escapeOutputBufferSpace())
        #print "buffer space: ", bs
        bs = self._readPort()
        return int(bs)


    def filterCommands(self, code):
        #print "filterCommands got: %s", code
        out = ''
        code_lines = splitCommandString(code)
        for c in code_lines:
            if c[0:2].upper() in self.allowedHPGLCommands:
                out += c
            else:
                print "*** WARNING: Command [%s] not allowed by %s plotter!!\a" % (c, self.type)

        #print "filterCommands returning: %s", out
        return out
    


    """
        PAGE SIZE, MARGINS, CLIPPING, ROTATION
    """

    def getMarginsHard(self):
        """
            Get hard margins of paper.
            This is set automatically at startup. Call this function
            explicitly if you change the paper size/orientation in some way
        """
        #print "getting hard margins..."
        
        self.ser.flushInput()
        self._writePort(self.lang.outputHardClipLimits())

        m = self._readPort()
        m = m.split(',')
        m = tuple([int(n) for n in m])
    
        return m

    def refreshMarginsHard(self):
        self.marginsHard = self.getMarginsHard()

    def getMarginsSoft(self):
        """
            Get soft margins of paper.
            This is set automatically at startup. Call this function
            explicitly if you change the paper size/orientation in some way
        """
        #print "getting soft margins..."
        
        self.ser.flushInput()
        self._writePort(self.lang.outputP1P2())
        
        m = self._readPort()
        m = m.split(',')
        m = tuple([int(n) for n in m])
        
        return m 

    def refreshMarginsSoft(self):
        self.marginsSoft = self.getMarginsSoft()
        
    def bottom(self, hard=True):
        """Get lowest coordinate."""
        if hard:
            return self.marginsHard[1]
        else:
            return self.marginsSoft[1]

    def top(self, hard=True):
        """Get top coordinate."""
        if hard:
            return self.marginsHard[3]
        else:
            return self.marginsSoft[3]

    def left(self, hard=True):
        """Get left coordinate."""
        if hard:
            return self.marginsHard[0]
        else:
            return self.marginsSoft[0]


    def right(self, hard=True):
        """Get right coordinate."""
        if hard:
            return self.marginsHard[2]
        else:
            return self.marginsSoft[2]



    def centerX(self, hard = True):
        """Get center point X."""
        if hard:
            return (self.right() + self.left()) / 2
        else:
            return (self.right(False) + self.left(False)) / 2
            
    def centerY(self, hard = True):
        """Get center point Y."""
        if hard:
            return (self.top() + self.bottom()) / 2
        else:
            return (self.top(False) + self.bottom(False)) / 2

    def centerPoint(self, hard = True):
        """Get center point X."""
        if hard:
            return tuple([self.centerX(), self.centerY()])
        else:
            return tuple([self.centerX(False), self.centerY(False)])            

    @property
    def actualPosition(self):
        self._writePort(self.lang.outputActualPosition())
        return self._readPort()

    def setAndScalePlotWindow(self):
        """
            sets new P1 and P2 points, then sets scale so that we still have the same virtual dimensions
            that means that you can plot an image with absolute coordinates corresponding to the plotter's
            native paper size without having to change the source file.
        """
        raw_input("Put plotter in lower left corner, then press Enter.")
        ll = self.actualPosition
        ll = ll.split(',')[0:2]
        ll = [int(n) for n in ll]
        raw_input("Put plotter in upper right corner, then press Enter.")
        ur = self.actualPosition
        ur = ur.split(',')[0:2]
        ur = [int(n) for n in ur]

        self._writePort(self.lang.inputP1P2(ll[0], ll[1], ur[0], ur[1]))
        self._writePort(self.lang.scale(self.left(), self.right(), self.bottom(), self.top()))
        
        self.marginsSoft = self.refreshMarginsSoft()
        
        print "New window set."

    def setNewCenterPoint(self):
        raw_input("Put plotter in new center, then press Enter.")
        newCenter = self.actualPosition
        newCenter = newCenter.split(',')[0:2]
        newCenter = [int(n) for n in newCenter]
        
        center = self.centerPoint();
        xMoveDist = newCenter[0] - center[0]
        yMoveDist = newCenter[1] - center[1]
        
        #print "you moved x by: %d and y by: %d" % (xMoveDist, yMoveDist)
        
        # new right is the old distance from right to center added to new center X
        newRight = newCenter[0] + (self.right() - center[0])
        if newRight > self.right():
            newRight = self.right()
            
        newLeft = newCenter[0] - (center[0] - self.left())
        if newLeft < 0:
            newLeft = 0
            
        newTop = newCenter[1] + (self.top() - center[1])
        if newTop > self.top():
            newTop = self.top()

        newBottom = newCenter[1] - (center[1] - self.bottom())
        if newBottom < 0:
            newBottom = 0
        
        #print "newRight: %d newLeft: %d newTop: %d newBottom: %d" % (newRight, newLeft, newTop, newBottom)
        
        self._writePort(self.lang.inputP1P2(newLeft, newBottom, newRight, newTop))
        self._writePort(self.lang.scale(0, newRight - newLeft, 0, newTop - newBottom))
        
        self.refreshMarginsSoft()
        
        print "new soft margins: left: %d right: %d bottom: %d top: %d" % (self.marginsSoft[0], self.marginsSoft[2], self.marginsSoft[1], self.marginsSoft[3])
        
    
    def setCoordinates(self):
        raw_input("Put plotter in lower left corner. Then press Enter.")
        ll = self.actualPosition
        ll = ll.split(',')[0:2]
        ll = [int(n) for n in ll]
        raw_input("Put plotter in upper right corner. Then press Enter.")
        ur = self.actualPosition
        ur = ur.split(',')[0:2]
        ur = [int(n) for n in ur]
        #print ll
        #print ur

        center = self.centerPoint()

        new_length_x = (ur[0] - ll[0]) / 2
        new_length_y = (ur[1] - ll[1]) / 2

        ll_new_x = center[0] - new_length_x
        ll_new_y = center[1] - new_length_y
        ur_new_x = center[0] + new_length_x
        ur_new_y = center[1] + new_length_y

        print 'll_new_x', ll_new_x
        print 'll_new_y', ll_new_y
        print 'ur_new_x', ur_new_x
        print 'ur_new_y', ur_new_y

        self._writePort(self.lang.inputP1P2(ll[0], ll[1], ur[0], ur[1]))
        self._writePort(self.lang.scale(ll_new_x, ur_new_x, ll_new_y, ur_new_y))
        
        self.refreshMarginsSoft()


    def selfTest(self):
        """Prints the ID of the plotter in the center of the page"""
        #print "getting pen 1"
        self.sp(1)
        #print "going to center"
        self.gotoC()
        #print "getting ID"
        #print "plotting id"
        self.plotText(self.id)
        #print "putting back pen"
        self.sp(0)
           

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
        self._writePort(self.lang.newLine())
        
    def outputLabelLength(self):
        self._writePort(self.lang.outputLabelLength())
        
    def plotText(self, text):
        self._writePort(self.lang.plotText(text))
    
    def plotTextFile(self, filename):
        self._writePort(self.lang.plotTextFile(filename))
        
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

    def fillType(self, type=1, space=None,  angle=0):
        self._writePort(self.lang.fillType(type, space, angle))


    def lineType(self, patNum, patLength = 4):
        self._writePort(self.lang.lineType(pattype, patlength))

    def plotPolygon(self, n = 0):
        self._writePort(self.lang.plotPolygon(n))



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
        self.plotRelative((x,y))
        
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

    def plotFile(self, filename):
        self._writePort(self.lang.plotFile(filename))
        
    def replot(self, n = 1):
        self._writePort(self.lang.replot(n))
        
    def writeToDisplay(self, text):
        self._writePort(self.lang.writeToDisplay(text))


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




####  utility functions -----------------------------        

def splitCommandString(string):
    #string = string.replace(' ', '')
    #string = string.replace('\n','')
    string = string.replace(';',';@')
    comms = string.split('@')
    comms = filter(lambda x: x!= '', comms)
    #print "comms after splitting:", comms
    return comms


### TRASH -------------------------------------------

    def semaphoreBuffer2(self, data):
        """ this is trying to do handshaking stuff"""
        data = data.replace(';', ';@')
        data = data.split('@')
        for e in data:
            fromPlotter = self.ser.read(self.ser.inWaiting())
            print 'fromPlotter:',fromPlotter
            time.sleep(.025)
            if fromPlotter == self.xoff:
                print "found xoff"
                while True:
                    time.sleep(2)
                    fromPlotter = self.ser.read(self.ser.inWaiting())
                    if fromPlotter == self.xon:
                        print "found xon"
                        break
            
            self.ser.write(e)            
                    
