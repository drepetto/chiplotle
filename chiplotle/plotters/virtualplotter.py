
from chiplotle.hpgl import commands 
from chiplotle.hpgl.abstract.hpgl import _HPGL
from chiplotle.tools.hpgltools import inflate_hpgl_string
from chiplotle.plotters.margins.plottermarginsvirtual import PlotterMarginsVirtual

import types

class VirtualPlotter():
   """
   Virtual pen plotter. Keeps track of all commands written to plotter,
   keeps track of virtual current position, provides virtual margins.
   
   Instantiate class by passing in virtual margins, then use as any
   other plotter.
   
   Use io.view(myVirtualPlotter) to view accumulated commands.
   
from chiplotle import *
from chiplotle.plotters.virtualplotter import VirtualPlotter   
vp = VirtualPlotter([0, 11000, 0, 13000])
vp.write(SP(3))
vp.write(PA([0,0]))
vp.write(PD())
vp.write(PA([0,1000]))
vp.write(PA([1000,1000]))
vp.write(PA([1000,0]))
vp.write(PA([0,0]))
vp.write(PU())
vp.write(Rectangle([111,222], 333, 444))
vp.get_hpgl()
io.view(vp)
"""

   def __init__(self, leftRightTopBottom):
      ## allowedHPGLCommands must be set prior to base class init.
      self.allowedHPGLCommands = tuple(['\x1b.','AA','AR','CA','CI','CP',
         'CS','DC','DF','DI','DP','DR','DT','EA','ER','EW','FT','IM','IN',
         'IP','IW','LB','LT','OA','OC','OD','OE','OF','OH','OI','OO','OP',
         'OS','OW','PA','PD','PR','PS','PT','PU','RA','RO','RR','SA','SC',
         'SI','SL','SM','SP', 'SR','SS','TL','UC','VS','WG','XT','YT'])

      self.type = "Virtual"

      self.megaString = ""
      
      self.commandedX = 0
      self.commandedY = 0
      
      # args are [left, right, top, bottom]
      self._margins = PlotterMarginsVirtual(self, 
         [leftRightTopBottom[0], leftRightTopBottom[1],
         leftRightTopBottom[2], leftRightTopBottom[3]])
         
      print "Opened VirtualPlotter with margins:"
      print "left: %d right: %d top: %d bottom: %d" % \
         (self.margins.hard.left, self.margins.hard.right, 
         self.margins.hard.top, self.margins.hard.bottom)

   @property
   def margins(self):
      '''Simulated margins'''
      return self._margins
      
      
   def write(self, data):
      '''Public access for writing to serial port. 
         data can be an iterator, a string or an _HPGL. '''
      if isinstance(data, _HPGL):
         self._write_string_to_port(data.format)
      elif isinstance(data, str):
         self._write_string_to_port(data)
      elif type(data) in (list, tuple, types.GeneratorType):
         result = [ ]
         for c in data:
            if isinstance(c, _HPGL):
               result.append(c.format)
            elif isinstance(c, str):
               result.append(c)
            else:
               raise TypeError('Elements must be strings or _HPGL commands.')
         self._write_string_to_port(''.join(result))
      else:
         raise TypeError('Must be a str, iterator or an _HPGL command.')
         

   def _write_string_to_port(self, data):
      ''' Write data to serial port. data is expected to be a string.'''
      assert type(data) is str
      
      splitData = data.split(';')
      
      for point in splitData:
         if point.startswith("PA"):
            #print "got: " + point
            pointParts = point.strip("PA").split(',')
            #print pointParts
            #print len(pointParts)
            self.commandedX = eval(pointParts[len(pointParts) - 2])
            self.commandedY = eval(pointParts[len(pointParts) - 1])
         elif point.startswith("PD"):
            #print "got: " + point
            if ',' in point:
               pointParts = point.strip("PD").split(',')
               #print pointParts
               #print len(pointParts)
               self.commandedX = eval(pointParts[len(pointParts) - 2])
               self.commandedY = eval(pointParts[len(pointParts) - 1])
         if point.startswith("PR"):
            #print "got: " + point
            pointParts = point.strip("PR").split(',')
            #print pointParts
            #print len(pointParts)
            self.commandedX += eval(pointParts[len(pointParts) - 2])
            self.commandedY += eval(pointParts[len(pointParts) - 1])
            
            
      self.megaString += data
      
   def get_hpgl(self):
      return inflate_hpgl_string(self.megaString)
   
   @property
   def format(self):
      '''This lets us pass the VirtualPlotter directly to io.view()'''
      return self.megaString
   
   ### PUBLIC QUERIES (PROPERTIES) ###

   @property
   def id(self):
      '''Get id of plotter. Returns a string.'''
      id = self._send_query(self._hpgl.OI( ))
      return "VirtualPlotter"

   @property
   def actual_position(self):
      '''Output the actual position of the plotter pen. Returns a tuple [x,y]'''
      return [self.commandedX, self.commandedY]

   @property
   def commanded_position(self):
      '''Output the commanded position of the plotter pen. Returns a tuple [x,y]'''
      return [self.commandedX, self.commandedY]
          
   @property
   def digitized_point(self):
      '''Returns last digitized point. Returns a tuple [x, y, penStatus]'''
      return [0,0]

