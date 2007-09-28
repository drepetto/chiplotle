

"""
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
"""

import sys
sys.path += ['../']
import serial
from languages import hpgl
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
        
        self.lang = hpgl
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


        self.initialize()


    def initialize(self):
        self.ser.flushInput()
        self.ser.flushOutput()
    
        self._writePort(self.lang.escapePlotterOn())
        self._writePort(self.lang.initialize())
        
        #self.plotterID = self.getPlotterID()
        #print "got ID: " + self.plotterID
        

        #self.marginsHard = self.getHardMargins()
        #self.marginsSoft = self.getSoftMargins()

    @property
    def id(self):
        """Get name of plotter being used."""
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


    def _writePort(self, data):
        """ Write data to serial port """
        data = self.filterCommands(data)
        #print "_writePort got %s" % data

        self.semaphoreBuffer(data)
        #or,  write directly...
        #self.ser.write(data)


    write = _writePort

    def semaphoreBuffer(self, data):
        """ If the data is larger than the available buffer space we break it up into chunks!  """
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
        if space < 250:
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

    def _readPort(self, numBytes = 100):
        """Read numBytes from the serial port"""
        print "waiting for %d bytes..." % numBytes
        return self.ser.read(numBytes)

    
    
    def getError(self):
        self.ser.flushInput();
        self._writePort(self.lang.extendedError())
        err = self._readPort()
        while len(err) == 0:
            self.ser.flushInput()
            err = self._readPort()
        return self._readPort()
    
    def bufferSpace(self):
        #print "getting bufferSpace..."
        bspace = '' 
        while len(bspace) == 0:
            self.ser.flushInput()
            self._writePortControl(self.lang.escapeOutputBufferSpace())
            bspace = self._readPort()
        
        #print "buffer space: ", bspace
        return int(bspace)


    def filterCommands(self, code):            
        out = ''
        code_lines = splitCommandString(code)
        for c in code_lines:
            if c[0:2].upper() in self.allowedHPGLCommands:
                out += c
            else:
                print "*** WARNING: Command [%s] not allowed by %s plotter!!\a" % (c, self.type)

        return out
    


    """
        PAGE SIZE, MARGINS, CLIPPING, ROTATION
    """

    @property
    def marginsHard(self):
        """Get margins of paper."""
        m = [] 
        while len(m) < 9:
            self.ser.flushInput()
            self._writePort(self.lang.outputHardClipLimits())
            m = self._readPort()
        m = m.split(',')
        m = tuple([int(n) for n in m])
        return m

    @property
    def marginsSoft(self):
        """Get margins of paper."""
        m = []
        while len(m) < 9:
            self.ser.flushInput()
            self._writePort(self.lang.outputP1P2())
            m = self._readPort()
        m = m.split(',')
        m = tuple([int(n) for n in m])
        return m

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


    def selfTest(self):
        """Prints the ID of the plotter in the center of the page"""
        #print "getting pen 1"
        self.lang.sp(1)
        #print "going to center"
        self.lang.gotoC()
        #print "getting ID"
        #print "plotting id"
        self.lang.plotText(self.lang.plotterID)
        #print "putting back pen"
        self.lang.sp(0)
           






####  utility functions -----------------------------        

def splitCommandString(string):
    string = string.replace(' ', '')
    string = string.replace('\n','')
    string = string.replace(';',';@')
    comms = string.split('@')
    comms = filter(lambda x: x!= '', comms)
    #print "comms after splitting:", comms
    return comms


    
