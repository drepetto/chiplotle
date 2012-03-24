from chiplotle.hpgl import commands 
from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.tools.hpgltools.inflate_hpgl_string import inflate_hpgl_string
from sys import maxint

class VirtualSerialPort():
   def __init__(self, left_bottom, right_top):
      left_bottom = Coordinate(*left_bottom)
      right_top = Coordinate(*right_top)
      #print "I am a virtual serial port!"
      self._received_commands_string = ""
      self._next_query_value = ''
      self.commanded_x = 0
      self.commanded_y = 0
      #pen_status: 0 == up, 1 == down
      self.pen_status = 0
      self.left = left_bottom.x
      self.right = right_top.x
      self.bottom = left_bottom.y
      self.top = right_top.y
      self.buffer_size = maxint
      self.portstr = "VirtualSerialPort"
      
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
         out_string = "%i, %i, %i\r" % (self.commanded_x, self.commanded_y, self.pen_status)
         self._next_query_value = out_string
         return
      elif command.startswith(commands.OC().format):
         #commanded position
         out_string = "%i, %i, %i\r" % (self.commanded_x, self.commanded_y, self.pen_status)
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
      
      split_data = command.split(';')
      
      for point in split_data:
         if point.startswith("PA"):
            point_parts = point.strip("PA").split(',')
            self.commanded_x = eval(point_parts[len(point_parts) - 2])
            self.commanded_y = eval(point_parts[len(point_parts) - 1])
         elif point.startswith("PD"):
            if ',' in point:
               point_parts = point.strip("PD").split(',')
               self.commanded_x = eval(point_parts[len(point_parts) - 2])
               self.commanded_y = eval(point_parts[len(point_parts) - 1])
            self.pen_status = 1
         elif point.startswith("PU"):
            if ',' in point:
               point_parts = point.strip("PU").split(',')
               self.commanded_x = eval(point_parts[len(point_parts) - 2])
               self.commanded_y = eval(point_parts[len(point_parts) - 1])
            self.pen_status = 0
         if point.startswith("PR"):
            point_parts = point.strip("PR").split(',')
            self.commanded_x += eval(point_parts[len(point_parts) - 2])
            self.commanded_y += eval(point_parts[len(point_parts) - 1])   

      #print "commanded_x: %i commanded_y: %i" % (self.commanded_x, self.commanded_y)
         
   def flush(self):
      pass
      
   def flushInput(self):
      #print "vsp: flushed input."
      pass
      
   def flushOutput(self):
      #print "vsp: flushed output."
      pass
   
   def clear(self):
      #this method doesn't exist for real serial ports
      #we use it to erase the stored commands so that you can reset
      #a virtual plotter to a blank state
      
      self._received_commands_string = ""
      
   #what's a reasonable value here?
   def inWaiting(self):
      return 10
      
      
   def readline(self, eol=None):
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
