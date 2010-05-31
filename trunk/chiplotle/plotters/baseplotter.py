'''
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
'''
from __future__ import division
from chiplotle.hpgl import commands 
from chiplotle.hpgl.abstract.hpgl import _HPGL
#from chiplotle.plotters import margin
from chiplotle.interfaces.margins.interface import MarginsInterface
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
      self._margins = MarginsInterface(self)
      self.buffer_size = self._buffer_space
      self.initialize_plotter( )


   ### PUBLIC METHODS ###

   @property
   def margins(self):
      '''Read-only reference to MarginsInterface.'''
      return self._margins


   def initialize_plotter(self):
      self._serialPort.flushInput( )
      self._serialPort.flushOutput( )
      self.write(self._hpgl.On( ))
      self.write(self._hpgl.IN( ))


   def write(self, data):
      '''Public access for writing to serial port. 
         data can be an iterator, a string or an _HPGL. '''
      #if hasattr(data, 'format'):
      if isinstance(data, _HPGL):
         self._write_string_to_port(data.format)
      elif isinstance(data, str):
         self._write_string_to_port(data)
      elif type(data) in (list, tuple, types.GeneratorType):
         result = [ ]
         for c in data:
            #if hasattr(c, 'format'):
            if isinstance(c, _HPGL):
               result.append(c.format)
            elif isinstance(c, str):
               result.append(c)
            else:
               raise TypeError('Elements must be strings or _HPGL commands.')
         self._write_string_to_port(''.join(result))
      else:
         raise TypeError('Must be a str, iterator or an _HPGL command.')


   def writeFile(self, filename):
      '''Sends the HPGL content of the given `filename` to the plotter.'''

      if not isinstance(filename, str):
         raise TypeError('Argument must be a string with the file name.')

      f = open(filename, 'r')
      chars = f.read( )
      f.close( )
      chars = chars.replace('\n',';')
      comms = re.split(';+', chars)
      comms = [c + ';' for c in comms if c != '']
      self.write(comms)


   ### PRIVATE METHODS ###

   def _is_HPGL_command_known(self, hpglCommand):
      if isinstance(hpglCommand, str):
         command_head = hpglCommand[0:2]
      elif hasattr(hpglCommand, '_name'):
         command_head = hpglCommand._name
      else:
         raise TypeError("Don't know type %s" % hpglCommand)
      return command_head.upper( ) in self.allowedHPGLCommands


   def _filter_unrecognized_commands(self, commands):
      assert isinstance(commands, str)
      result = [ ] 
      #commands = re.split('[\n;]+', commands)
      commands = commands.split(';')
      for comm in commands:
         if comm: ## if not an empty string.
            if self._is_HPGL_command_known(comm):
               #result.append(comm)
               result.append(comm + ';')
            else:
               print 'WARNING: HPGL command "%s" not recognized by %s.'\
               % (comm, self.type),
               print 'Command not sent.'
      return ''.join(result)


   def _sleep_while_buffer_full(self):
      '''
         sleeps until the buffer has some room in it.
      '''
      if self._buffer_space < self.buffer_size:
         #print 'Buffer getting full, sleeping...'
         while self._buffer_space < self.buffer_size:
            time.sleep(1)
         #print 'Okay, now buffer has room...'


   def _slice_string_to_buffer_size(self, data):
         result = [ ]
         count = int(math.ceil(len(data) / self.buffer_size))
         for i in range(count):
            result.append(data[i * self.buffer_size: (i+1) * self.buffer_size])
         return result


   def _write_string_to_port(self, data):
      ''' Write data to serial port. data is expected to be a string.'''
      assert type(data) is str
      data = self._filter_unrecognized_commands(data)
      data = self._slice_string_to_buffer_size(data)
      for chunk in data:
         self._sleep_while_buffer_full( )
         self._serialPort.write(chunk)
      

   ### PRIVATE QUERIES ###


   def _read_port(self):
      '''Read data from serial port.'''
      elapsed_time = 0
      total_time = 8
      sleep = 1.0 / 8
      while elapsed_time < total_time:
         if self._serialPort.inWaiting( ): 
            return self._serialPort.readline(eol='\r')
         else:
            time.sleep(sleep)
            elapsed_time += sleep
      print 'Waited for %s secs... No response from plotter.' % total_time
      return 
   

   @property
   def _buffer_space(self):
      #print "getting _buffer_space..."
      self._serialPort.flushInput()
      self._serialPort.write(self._hpgl.B().format)
      bs = self._read_port()
      #print "buffer space: ", bs
      return int(bs)

   def _send_query(self, query):
      '''Private method to manage plotter queries.'''
      if self._is_HPGL_command_known(query):
         self._serialPort.flushInput( )
         self.write(query)
         return self._read_port( )
      else:
         print '%s not supported by %s.' % (query, self.id)


   ### PUBLIC QUERIES (PROPERTIES) ###

   @property
   def id(self):
      '''Get id of plotter.'''
      #self._serialPort.flushInput()
      #self.write(self._hpgl.OI())
      #id = self._read_port()
      id = self._send_query(self._hpgl.OI( ))
      return id.strip('\r')

   @property
   def actual_position(self):
      '''Output the actual position of the plotter pen.'''
      #self.write(self._hpgl.OA())
      #return self._read_port()
      return self._send_query(self._hpgl.OA( ))

   @property
   def carouselType(self):
#      command = self._hpgl.OT( )
#      self.write(command)
#      return self._read_port()
      return self._send_query(self._hpgl.OT( ))

   @property
   def commandedPosition(self):
      #self.write(self._hpgl.OC())
      #return self._read_port()
      return self._send_query(self._hpgl.OC( ))
          
   @property
   def digitizedPoint(self):
      #self.write(self._hpgl.OD())
      #return self._read_port()
      return self._send_query(self._hpgl.OD( ))

   @property
   def outputError(self):
      #self.write(self._hpgl.OE())
      #return self._read_port()
      return self._send_query(self._hpgl.OE( ))

#   @property
#   def hardClipLimits(self):
#      '''Output hard clip limits. Same as marginHard.'''
#      self.write(self._hpgl.OH())
#      return self._read_port()

   @property
   def outputKey(self):
      #command = self._hpgl.OK( )
      #self.write(command)
      #return self._read_port()
      return self._send_query(self._hpgl.OK( ))

   @property
   def labelLength(self):
      #command = self._hpgl.OL( )
      #self.write(command)
      #return self._read_port()
      return self._send_query(self._hpgl.OL( ))

   @property
   def options(self):
      #self.write(self._hpgl.OO())
      #return self._read_port()
      return self._send_query(self._hpgl.OO( ))

   @property
   def outputP1P2(self):
      #self.write(self._hpgl.OP())
      #return self._read_port()
      return self._send_query(self._hpgl.OP( ))

   @property
   def status(self):
      #self.write(self._hpgl.OS())
      #return self._read_port()
      return self._send_query(self._hpgl.OS( ))

#   @property
#   def window(self):
#      '''Output window. Same as margins.soft.'''
#      self.write(self._hpgl.OW())
#      return self._read_port()


   ### DCI (Device Control Instructions) Escape commands ###

   def escapePlotterOn(self):
      self.write( self._hpgl.On() )

   
   ## OVERRIDES ##

   def __str__(self):
      return '%s in port %s' % (self.type, self._serialPort.portstr)

   def __repr__(self):
      return '%s(%s)' % (self.type, self._serialPort.portstr)
