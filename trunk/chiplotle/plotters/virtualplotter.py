


from chiplotle.hpgl import commands 
from chiplotle.hpgl.abstract.hpgl import _HPGL
from chiplotle.tools.hpgltools import inflate_hpgl_string

import types

class VirtualPlotter():
   """
   First try at a virtual plotter.
   Does not yet keep track of commanded position, which is the whole point...
   
   from chiplotle import *
   from chiplotle.plotters.virtualplotter import VirtualPlotter   
   vp = VirtualPlotter()
   vp.write(SP(3))
   vp.write(PA([0,0]))
   vp.write(PD())
   vp.write(PA([0,1000]))
   vp.write(PA([1000,1000]))
   vp.write(PA([1000,0]))
   vp.write(PA([0,0]))
   vp.write(PU())
   vp.get_hpgl()
   io.view(vp.get_hpgl())
"""
   def __init__(self, **kwargs):
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
      self.megaString += data
      
   def get_hpgl(self):
      return inflate_hpgl_string(self.megaString)
   
   
   
   ### PUBLIC QUERIES (PROPERTIES) ###

   @property
   def id(self):
      '''Get id of plotter. Returns a string.'''
      id = self._send_query(self._hpgl.OI( ))
      return "VirtualPlotter"

   @property
   def actual_position(self):
      '''Output the actual position of the plotter pen. Returns a tuple [x,y]'''
      return [0,0]

   @property
   def commanded_position(self):
      '''Output the commanded position of the plotter pen. Returns a tuple [x,y]'''
      return [0,0]
          
   @property
   def digitized_point(self):
      '''Returns last digitized point. Returns a tuple [x, y, penStatus]'''
      return [0,0]

