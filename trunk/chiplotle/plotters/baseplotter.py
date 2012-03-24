'''
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
'''
from __future__ import division
from chiplotle.core.cfg.get_config_value import get_config_value 
from chiplotle.core.interfaces.margins.interface import MarginsInterface
from chiplotle.geometry.core.shape import _Shape
from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.hpgl import commands 
from chiplotle.hpgl.abstract.hpgl import _HPGL
from chiplotle.tools.logtools.get_logger import get_logger
from chiplotle.tools.serialtools import VirtualSerialPort
import math
import re
import serial
import time
import types


class _BasePlotter(object):
   def __init__(self, serial_port):
      self.type = '_BasePlotter'
      self._logger = get_logger(self.__class__.__name__)
      self._serial_port = serial_port
      self._hpgl = commands
      self._margins = MarginsInterface(self)
      self.maximum_response_wait_time = get_config_value('maximum_response_wait_time')

      #this is so that we don't pause while preparing and sending
      #full buffers to the plotter. By sending 1/2 buffers we assure
      #that the plotter will still have some data to plot while
      #receiving the new data
      self.buffer_size = int(self._buffer_space / 2)
      self.initialize_plotter( )

      

   @property
   def margins(self):
      '''Read-only reference to MarginsInterface.'''
      return self._margins


   ### PUBLIC METHODS ###

   def initialize_plotter(self):
      self._serial_port.flushInput( )
      self._serial_port.flushOutput( )
      self.write(self._hpgl.On( ))
      self.write(self._hpgl.IN( ))


   def write(self, data):
      '''Public access for writing to serial port. 
         data can be an iterator, a string or an _HPGL. '''
      ## TODO: remove _HPGL from this list...
      if isinstance(data, (_Shape, _HPGL)):
         data = data.format
      try:
         self._write_string_to_port(data)
      except TypeError: ## must be an iterable...
         result = [ ]
         for c in data:
            ## TODO: remove _HPGL from this list...
            if isinstance(c, (_Shape, _HPGL)):
               c = c.format
            result.append(c)
         try:
            self._write_string_to_port(''.join(result))
         except TypeError:
            raise TypeError('Must be a str, iterator, or a _Shape.')
         
#      if isinstance(data, _HPGL):
#         self._write_string_to_port(data.format)
#      elif isinstance(data, str):
#         self._write_string_to_port(data)
#      elif type(data) in (list, tuple, types.GeneratorType):
#         result = [ ]
#         for c in data:
#            #if hasattr(c, 'format'):
#            if isinstance(c, _HPGL):
#               result.append(c.format)
#            elif isinstance(c, str):
#               result.append(c)
#            else:
#               raise TypeError('Elements must be strings or _HPGL commands.')
#         self._write_string_to_port(''.join(result))
#      else:
#         raise TypeError('Must be a str, iterator or an _HPGL command.')


   def write_file(self, filename):
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
               msg = 'HPGL command `%s` not recognized by %s. Command not sent.'
               msg = msg % (comm, self.type)
               self._logger.warning(msg)
      return ''.join(result)


   def _sleep_while_buffer_full(self):
      '''
         sleeps until the buffer has some room in it.
      '''
      if self._buffer_space < self.buffer_size:
         while self._buffer_space < self.buffer_size:
            time.sleep(0.01)


   def _slice_string_to_buffer_size(self, data):
         result = [ ]
         count = int(math.ceil(len(data) / self.buffer_size))
         for i in range(count):
            result.append(data[i * self.buffer_size: (i+1) * self.buffer_size])
         return result


   def _write_string_to_port(self, data):
      ''' Write data to serial port. data is expected to be a string.'''
      #assert type(data) is str
      if not isinstance(data, basestring):
         raise TypeError('string expected.')
      data = self._filter_unrecognized_commands(data)
      data = self._slice_string_to_buffer_size(data)
      for chunk in data:
         self._sleep_while_buffer_full( )
         self._serial_port.write(chunk)
      

   ### PRIVATE QUERIES ###

   def _read_port(self):
      '''Read data from serial port.'''
      elapsed_time = 0
      total_time = self.maximum_response_wait_time
      sleep = 1.0 / 8
      while elapsed_time < total_time:
         if self._serial_port.inWaiting( ): 
            try:
               return self._serial_port.readline(eol='\r') # <-- old pyserial
            except:
               return self._serial_port.readline()
         else:
            time.sleep(sleep)
            elapsed_time += sleep
      msg = 'Waited for %s secs... No response from plotter.' % total_time
      self._logger.error(msg)
      return 
   

   @property
   def _buffer_space(self):
      self._serial_port.flushInput()
      self._serial_port.write(self._hpgl.B().format)
      bs = self._read_port()
      return int(bs)

   def _send_query(self, query):
      '''Private method to manage plotter queries.'''
      if self._is_HPGL_command_known(query):
         self._serial_port.flushInput( )
         self.write(query)
         return self._read_port( )
      else:
         #print '%s not supported by %s.' % (query, self.id)
         msg = 'Command %s not supported by %s.' % (query, self.id)
         self._logger.warning(msg)


   ### PUBLIC QUERIES (PROPERTIES) ###

   @property
   def id(self):
      '''Get id of plotter. Returns a string.'''
      id = self._send_query(self._hpgl.OI( ))
      return id.strip('\r')

   @property
   def actual_position(self):
      '''Output the actual position of the plotter pen. Returns a tuple 
      (Coordinate(x, y), pen status)'''
      response = self._send_query(self._hpgl.OA( )).split(',')
      return [Coordinate(eval(response[0]), eval(response[1])), 
         eval(response[2].strip('\r'))]

   @property
   def carousel_type(self):
      return self._send_query(self._hpgl.OT( ))

   @property
   def commanded_position(self):
      '''Output the commanded position of the plotter pen. Returns a tuple 
      [Coordinate(x, y), pen status]'''
      response = self._send_query(self._hpgl.OC( )).split(',')      
      return [Coordinate(eval(response[0]), eval(response[1])), 
         eval(response[2].strip('\r'))]
          
   @property
   def digitized_point(self):
      '''Returns last digitized point. Returns a tuple 
      [Coordinate(x, y), pen status]'''
      response = self._send_query(self._hpgl.OD( )).split(',')
      return [Coordinate(eval(response[0]), eval(response[1])), 
         eval(response[2].strip('\r'))]

   @property
   def output_error(self):
      return self._send_query(self._hpgl.OE( ))

   @property
   def output_key(self):
      return self._send_query(self._hpgl.OK( ))

   @property
   def label_length(self):
      return self._send_query(self._hpgl.OL( ))

   @property
   def options(self):
      return self._send_query(self._hpgl.OO( ))

   @property
   def output_p1p2(self):
      '''Returns the current settings for P1, P2. Returns two Coordinates'''
      response = self._send_query(self._hpgl.OP( )).split(',')
      cp1 = Coordinate(eval(response[0]), eval(response[1]))
      cp2 = Coordinate(eval(response[2]), eval(response[3].strip('\r')))
      return (cp1, cp2)

   @property
   def status(self):
      return self._send_query(self._hpgl.OS( ))


   ### DCI (Device Control Instructions) Escape commands ###

   def escape_plotter_on(self):
      self.write( self._hpgl.On() )

   
   ## OVERRIDES ##

   def __str__(self):
      return '%s in port %s' % (self.type, self._serial_port.portstr)

   def __repr__(self):
      return '%s(%s)' % (self.type, self._serial_port.portstr)


   ## WEIRD STUFF FOR VIRTUAL PLOTTERS ##

   @property
   def format(self):
      '''
         This lets us pass the VirtualPlotter directly to io.view()
         Returns None if called on a plotter with a real serial port.
      '''
      if isinstance(self._serial_port, VirtualSerialPort):
         return self._serial_port.format
      else:
         return None
 
 
   def clear(self):
      '''
      Tells the virtual serial port to forget its stored commands.
      Used to "erase" the drawing on the virtual plotter.
      '''
      if isinstance(self._serial_port, VirtualSerialPort):
         self._serial_port.clear()
      else:
         pass
         
         
