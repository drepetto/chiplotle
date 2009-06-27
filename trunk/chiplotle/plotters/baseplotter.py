'''
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
'''
from __future__ import division
from chiplotle.hpgl import commands 
from chiplotle.plotters import margin
#from chiplotle.hpgl.tools.import_hpgl_file import import_hpgl_file
import math
import re
import serial
import time
import types


class _BasePlotter(object):
   def __init__(self, serialPort):
      self.type = '_BasePlotter'
      self.memory = []
      self._serialPort = serialPort
      self._hpgl = commands
      self.bufferSize = self._bufferSpace

      ## Only these commands will be sent to the plotter. 
      #self.allowedHPGLCommands = tuple( )

      self.marginHard = margin._MarginsHard(self)
      self.marginSoft = margin._MarginsSoft(self)

      self.initializePlotter()


   ### PUBLIC METHODS ###

   def initializePlotter(self):
      self._serialPort.flushInput()
      self._serialPort.flushOutput()
      self.write(self._hpgl.On())
      self.write(self._hpgl.IN())


   def write(self, data):
      '''Public access for writing to serial port. 
         data can be an iterator, a string or an _HPGLCommand. '''
      if hasattr(data, 'format'):
         self._writeStringToPort(data.format)
      elif isinstance(data, str):
         self._writeStringToPort(data)
      elif type(data) in (list, tuple, types.GeneratorType):
         result = [ ]
         for c in data:
            if hasattr(c, 'format'):
               result.append(c.format)
            elif isinstance(c, str):
               result.append(c)
            else:
               raise ValueError('Invalid value. Must be str or _HPLGCommand.')
         self._writeStringToPort(''.join(result))
      else:
         raise ValueError('Invalid value. \
         Must be str, iterator or _HPLGCommand.')


   def writeFile(self, filename):
      '''Sends the HPGL content of the given `filename` to the plotter.'''

      if not isinstance(filename, str):
         raise TypeError('Argument must be a string with the file name.')

      f = open(filename, 'r')
      chars = f.read( )
      f.close( )
      chars = chars.replace('\n',';')
      comms = re.split(';+', chars)
      self.write(comms)


   ### PRIVATE METHODS ###

   def _isHPGLCommandKnown(self, hpglCommand):
      if isinstance(hpglCommand, str):
         command_head = hpglCommand[0:2]
      elif hasattr(hpglCommand, '_name'):
         command_head = hpglCommand._name
      else:
         raise TypeError("Don't know type %s" % hpglCommand)
      return command_head.upper( ) in self.allowedHPGLCommands


   def _filterUnrecognizedCommands(self, commands):
      assert isinstance(commands, str)
      result = [ ] 
      #commands = re.split('[\n;]+', commands)
      commands = commands.split(';')
      for comm in commands:
         if comm: ## if not an empty string.
            if self._isHPGLCommandKnown(comm):
               #result.append(comm)
               result.append(comm + ';')
            else:
               print 'WARNING: HPGL command "%s" not recognized by %s.'\
               % (comm, self.type),
               print 'Command not sent.'
      return ''.join(result)


   def _sleepWhileBufferFull(self):
      '''
         sleeps until the buffer has some room in it.
      '''
      if self._bufferSpace < self.bufferSize:
         #print 'Buffer getting full, sleeping...'
         while self._bufferSpace < self.bufferSize:
            time.sleep(1)
         #print 'Okay, now buffer has room...'


   def _sliceStringToBufferSize(self, data):
         result = [ ]
         count = int(math.ceil(len(data) / self.bufferSize))
         for i in range(count):
            result.append(data[i * self.bufferSize: (i+1) * self.bufferSize])
         return result


   def _writeStringToPort(self, data):
      ''' Write data to serial port. data is expected to be a string.'''
      assert type(data) is str
      data = self._filterUnrecognizedCommands(data)
      data = self._sliceStringToBufferSize(data)
      for chunk in data:
         self._sleepWhileBufferFull( )
         self._serialPort.write(chunk)
      

   ### PRIVATE QUERIES ###


   def _readPort(self):
      '''Read data from serial port.'''
      while self._serialPort.inWaiting( ) == 0:
         time.sleep(1.0 / 64)
      result = self._serialPort.readline(eol='\r')
      #print repr(result)
      return result
   

   @property
   def _bufferSpace(self):
      #print "getting _bufferSpace..."
      self._serialPort.flushInput()
      self._serialPort.write(self._hpgl.B().format)
      bs = self._readPort()
      #print "buffer space: ", bs
      return int(bs)


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
      self.write(command)
      return self._readPort()

   @property
   def labelLength(self):
      command = self._hpgl.OL( )
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

