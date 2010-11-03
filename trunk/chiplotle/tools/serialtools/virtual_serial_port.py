#from chiplotle import *
#from chiplotle.hpgl.abstract.hpgl import _HPGL
from chiplotle.hpgl import commands 
from chiplotle.tools.hpgltools.inflate_hpgl_string import inflate_hpgl_string
from sys import maxint

class VirtualSerialPort():
   def __init__(self, left=0, bottom=0, right=15000, top=10000):
      #print "I am a virtual serial port!"
      self._received_commands_string = ""
      self._next_query_value = ''
      self.commandedX = 0
      self.commandedY = 0
      #penStatus: 0 == up, 1 == down
      self.penStatus = 0
      self.left = left
      self.right = right
      self.bottom = bottom
      self.top = top
      self.buffer_size = maxint
      
   def write(self, command):
      '''
      we assume that commands are sent either as single escaped commands,
      like B() or On(), or as single or strings of regular text commands,
      like PA0,0;PD;
      
      if an escape command is somehow inserted into a string of text commands
      we will not catch it! but that shouldn't happen...
      
      '''
      #print "vsp got command: " + command
     
      '''this seems dumb, but don't know how else to do it.
         gotta iterate through all possible weirdo commands.
      '''
      
      #make sure we received a string, not a tuple or something
      assert type(command) is str
            
      if command.startswith(commands.B().format):
         #let's say we have 4MB of memory to avoid buffered writes
         self._next_query_value = self.buffer_size
         return
      elif command.startswith(commands.On().format):
         #print "vsp: ignoring On() command."
         return
      elif command.startswith(commands.OH().format):
         #hard margins
         out_string = "%d, %d, %d, %d\r" % (self.left, self.bottom, self.right, self.top)
         self._next_query_value = out_string
         return
      elif command.startswith(commands.OW().format):
         #soft margins
         out_string = "%d, %d, %d, %d\r" % (self.left, self.bottom, self.right, self.top)
         self._next_query_value = out_string
         return
      elif command.startswith(commands.OI().format):
         self._next_query_value = "VirtualPlotter\r"
         return
      elif command.startswith(commands.OA().format):
         #actual position
         out_string = "%i, %i, %i\r" % (self.commandedX, self.commandedY, self.penStatus)
         self._next_query_value = out_string
         return
      elif command.startswith(commands.OC().format):
         #commanded position
         out_string = "%i, %i, %i\r" % (self.commandedX, self.commandedY, self.penStatus)
         self._next_query_value = out_string
         return
      elif command.startswith(commands.OP().format):
         #output P1P2
         out_string = "%d, %d, %d, %d\r" % (self.left, self.bottom, self.right, self.top)
         self._next_query_value = out_string
         return

      #if we made it here then we're normal HPGL
      
      self._received_commands_string += command
         
      #store commanded position data
      #this breaks for buffered writes since we don't always
      #receive a full PA1000,1000 type command
      
      splitData = command.split(';')
      
      for point in splitData:
         if point.startswith("PA"):
            pointParts = point.strip("PA").split(',')
            self.commandedX = eval(pointParts[len(pointParts) - 2])
            self.commandedY = eval(pointParts[len(pointParts) - 1])
         elif point.startswith("PD"):
            if ',' in point:
               pointParts = point.strip("PD").split(',')
               self.commandedX = eval(pointParts[len(pointParts) - 2])
               self.commandedY = eval(pointParts[len(pointParts) - 1])
            self.penStatus = 1
         elif point.startswith("PU"):
            if ',' in point:
               pointParts = point.strip("PU").split(',')
               self.commandedX = eval(pointParts[len(pointParts) - 2])
               self.commandedY = eval(pointParts[len(pointParts) - 1])
            self.penStatus = 0
         if point.startswith("PR"):
            pointParts = point.strip("PR").split(',')
            self.commandedX += eval(pointParts[len(pointParts) - 2])
            self.commandedY += eval(pointParts[len(pointParts) - 1])   

      #print "commandedX: %i commandedY: %i" % (self.commandedX, self.commandedY)
         
   def flush(self):
      pass
      
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
      return_value = self._next_query_value
      self._next_query_value = None
      return return_value
      
      
   def get_received_commands(self):
      return inflate_hpgl_string(self._received_commands_string)

   def get_received_commands_string(self):
      return self._received_commands_string
      
   @property
   def format(self):
      '''This is so that a VirtualPlotter can call serial_port.format to retrieve
      stored commands and send them to io.view()
      '''
      return self._received_commands_string
