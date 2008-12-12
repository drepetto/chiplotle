'''
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
'''

from chiplotle.hpgl import commands 
from margin import _PlotterMargin
import serial
import time
import types


class Plotter(object):
   def __init__(self, serialPort):
      self.type = 'Generic'
      self.memory = []
      self._serialPort = serialPort
      self._hpgl = commands

      ### Only these commands will be sent to the plotter. 
      ### All other will be eaten. Burp.
      self.allowedHPGLCommands = tuple([
      '(', ')', 'AA','AR','CA','CI','CP','CS','DC','DF','DI','DP',
      'DR','DT','EA','ER','EW','FT','IM','IN','IP','IW','LB','LT',
      'OA','OC','OD','OE','OF','OH','OI','OO','OP','OS','OW','PA',
      'PD','PR','PS','PT','PU','RA','RO','RR','SA','SC','SI','SL',
      'SM','SP', 'SR','SS','TL','UC','VS','WG','XT','YT'])

      self.marginHard = _PlotterMargin(self, self._hpgl.OH())
      self.marginSoft = _PlotterMargin(self, self._hpgl.OW()) 

      self.initializePlotter()


   ### PUBLIC METHODS ###

   def initializePlotter(self):
      self._serialPort.flushInput()
      self._serialPort.flushOutput()
      self.write(self._hpgl.On())
      self.write(self._hpgl.IN())

   def write(self, data):
      ''' Public access for writing to serial port. 
         It allows the <data> input to be a list or tuple. 
         All elements inside the list must have a <format> attribute'''
      commands =  [ ]
      if type(data) in (list, tuple, types.GeneratorType):
         for c in data:
            assert hasattr(c, 'format')
            ### TODO how can we check HPGL adecuacy while at the same time 
            ### allowing the user to define his own HPGL objects?
#            if self._isCommandKnown(c):
#               commands.append(c.format) 
#            self._isCommandKnown(c)
            commands.append(c.format) 
         self._writeStringToPort(''.join(commands))
      else:
#         if self._isCommandKnown(data):
#            self._writeStringToPort(data.format)
#         self._isCommandKnown(data)
         self._writeStringToPort(data.format)


   ### PRIVATE METHODS ###

   def _writeStringToPort(self, data):
      ''' Write data to serial port.
      -data- is expected to be of type string.'''
      assert type(data) is str
      self._semaphoreBuffer(data)

   def _semaphoreBuffer(self, data):
      ''' If the data is larger than the available buffer 
         space we break it up into chunks!  '''
      dataLen = len(data)
      bufferSpace = self._bufferSpace()
      #print "total command length: %d" % dataLen
      if dataLen > bufferSpace:      
         print "Uh oh, too much data!"
         numChunks = (dataLen / 1000) + 1
         for i in range(numChunks):
            self._sleepWhileBufferFull()
            start = i * 1000
            end = start + 1000
            self._serialPort.write(data[start:end])         
      # buffer space is fine, just send it as is!
      else:
         self._serialPort.write(data)
      #print "done writing to port..."
      

   def _sleepWhileBufferFull(self):
      '''
         sleeps until the buffer has some room in it.
      '''
      space = self._bufferSpace()  
      if space < 1000:
         print 'Buffer getting full, sleeping...'
         while True:
            time.sleep(1)
            space = self._bufferSpace()  
            if space >= 1000:
               print 'Okay, now buffer has room...'
               break


   ### PRIVATE QUERIES ###

   def _readByte(self):
      byte = self._serialPort.read()
      return byte

   def _readPort(self):
      '''Read data from the serial port'''
      maxattempts = 16 * 5 # 5 secs.
      countAttempts = 0
      while self._serialPort.inWaiting() == 0 and countAttempts < maxattempts:
         countAttempts += 1
         time.sleep(1. / 16)
      if countAttempts == maxattempts:
         print 'No response from plotter. :('
         return None

      m = ''
      input = 'xxx'
      while input != '':
         input = self._readByte()
         m += input
      return m

   
   def _bufferSpace(self):
      #print "getting _bufferSpace..."
      self._serialPort.flushInput()
      self._serialPort.write(self._hpgl.B().format)
      #print "buffer space: ", bs
      bs = self._readPort()
      return int(bs)


   def _isCommandKnown(self, hpglCommand):
      '''Filter out unknown command and tell us about it.'''
      if hpglCommand._name in self.allowedHPGLCommands:
         return True
      else:
         print "*** WARNING: Command [%s] not understood by %s plotter." \
         % (hpglCommand._name, self.type)
         return False


   ### PUBLIC QUERIES (PROPERTIES) ###

   @property
   def id(self):
      '''Get id of plotter.'''
      self._serialPort.flushInput()
      self.write(self._hpgl.OI())
      
      id = self._readPort()
      return id.strip('\r')

   @property
   def actualPosition(self):
      '''Output the actual position of the plotter pen.'''
      self.write(self._hpgl.OA())
      return self._readPort()

   @property
   def carouselType(self):
      command = self._hpgl.OT( )
      if self._isCommandKnown(command):
         self.write(command)
         return self._readPort()

   @property
   def commandedPosition(self):
      self.write(self._hpgl.OC())
      return self._readPort()
          
   @property
   def digitizedPoint(self):
      self.write(self._hpgl.OD())
      return self._readPort()

   @property
   def outputError(self):
      self.write(self._hpgl.OE())
      return self._readPort()

   @property
   def hardClipLimits(self):
      '''Output hard clip limits. Same as marginHard.'''
      self.write(self._hpgl.OH())
      return self._readPort()

   @property
   def outputKey(self):
      command = self._hpgl.OK( )
      if self._isCommandKnown(command):
         self.write(command)
         return self._readPort()

   @property
   def labelLength(self):
      command = self._hpgl.OL( )
      if self._isCommandKnown(command):
         self.write(command)
         return self._readPort()

   @property
   def options(self):
      self.write(self._hpgl.OO())
      return self._readPort()

   @property
   def outputP1P2(self):
      self.write(self._hpgl.OP())
      return self._readPort()

   @property
   def status(self):
      self.write(self._hpgl.OS())
      return self._readPort()

   @property
   def window(self):
      '''Output window. Same as marginSoft.'''
      self.write(self._hpgl.OW())
      return self._readPort()


   ### DCI (Device Control Instructions) Escape commands ###

   def escapePlotterOn(self):
      self.write( self._hpgl.On() )

