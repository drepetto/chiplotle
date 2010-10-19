
from chiplotle.hpgl import commands 
from chiplotle.hpgl.abstract.hpgl import _HPGL
from chiplotle.tools.hpgltools import inflate_hpgl_string

class VirtualSerialPort():
   def __init__(self):
      #print "I am a virtual serial port!"
      self._received_commands_string = ""
      self._next_query_value = ''
      
   def write(self, command):
      '''
      we assume that commands are sent either as single escaped commands,
      like B() or On(), or as single or strings of regular text commands,
      like PA0,0;PD;
      
      if an escape command is somehow inserted into a string of text commands
      we will not catch it! but that shouldn't happen...
      
     '''
     
      if command == commands.B().format:
         self._next_query_value = "4000"
      elif command == commands.On().format + ";":
         #print "vsp: ignoring On() command."
         pass
      else:
         self._received_commands_string += command
         
   def flushInput(self):
      #print "vsp: flushed input."
      pass
      
   def flushOutput(self):
      #print "vsp: flushed output."
      pass
      
   #what's a reasonable value here?
   def inWaiting(self):
      return 10
      
      
   def readline(self, eol):
      #print "returning: " + self._next_query_value
      return self._next_query_value
      
   def get_received_commands(self):
      return inflate_hpgl_string(self._received_commands_string)

   def get_received_commands_string(self):
      return self._received_commands_string
      
   @property
   def format(self):
      '''This is so that a VirtualPlotter can all serial_port.format to retrieve
      stored commands and send them to io.view()
      '''
      return self._received_commands_string