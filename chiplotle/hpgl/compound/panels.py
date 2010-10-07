from __future__ import division
from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.commands import PU, PD, PA, PR

class Panels(_CompoundHPGL):
   '''Rectangular grid of panels with space between them. 

   - `xy` : ``tuple``, (x, y) top, left starting position.
   - `width` : ``int`` or ``float``, total width of the rect to contain panels.
   - `height` : ``int`` or ``float``, total height of the rect to contain panels.
   - `horiz_panels` : ``int``, number of panels across.
   - `vert_panels` : ``int``, number of panels vertical.
   - `horiz_buffer` : ``float``, percentage (0.0 - 1.0) of width dedicated to buffer space
   - `vert_buffer` : ``float``, percentage (0.0 - 1.0) of height dedicated to buffer space
   - `big_border` : ``boolean``, draw big border around panel array
   - `pen` : ``int``, pen number.
      
      
   Example::

      from chiplotle import *
      width = 10000
      height = 10000
      panel = Panels([0,height], width, height, 5, 5, .1, .1, True, 3)
      io.view(panel)      
   
   | x x x x x |
   | x x x x x |
   | x x x x x |
   | x x x x x |
   | x x x x x |
   
   '''

   _scalable = ['width', 'height']

   def __init__(self, xy, width, height, horiz_panels, 
      vert_panels, horiz_buffer, vert_buffer, big_border=False, pen=None):
      _CompoundHPGL.__init__(self, xy, pen = pen) 
      self.width = width
      self.height = height
      self.horiz_panels = horiz_panels
      self.vert_panels = vert_panels
      self.horiz_buffer = horiz_buffer
      self.vert_buffer = vert_buffer
      self.big_border = big_border
      self.reference_point = (0, 0) ## range: [0 to 1]


   @property
   def _subcommands(self):
      horiz_buff_total = self.width * self.horiz_buffer
      vert_buff_total = self.height * self.vert_buffer
      horiz_buff_each = horiz_buff_total / (self.horiz_panels + 1)
      vert_buff_each = vert_buff_total / (self.vert_panels + 1)
      width_each = (self.width - horiz_buff_total) / self.horiz_panels
      height_each = (self.height - vert_buff_total) / self.vert_panels
      
      #print "xabsoute: %d yabsolute: %d" % (self.xabsolute, self.yabsolute)
      #print "width_each: %d height_each: %d horiz_buff_each: %d vert_buff_each %d" % \
      #   (width_each, height_each, horiz_buff_each, vert_buff_each)
         
      result = _CompoundHPGL._subcommands.fget(self)
      
      result.append(PU())

      if self.big_border:
         # draw big rect
         result.append(PA((self.x, self.y)))
         result.append(PD())
         result.append(PA((self.x+ self.width, self.y)))
         result.append(PA((self.x+ self.width, self.y- self.height)))
         result.append(PA((self.x, self.y- self.height)))
         result.append(PA((self.x, self.y)))
         result.append(PU())
      
      for i in range(self.horiz_panels):
         for j in range(self.vert_panels):
            x_start = self.x+ (horiz_buff_each * (i + 1)) + (width_each * i)
            y_start = self.y- (vert_buff_each * (j + 1)) - (height_each * j)
            #print "x_start: %d y_start: %d" % (x_start, y_start)
            result.append(PA((x_start, y_start)))
            result.append(PD())
            result.append(PA((x_start + width_each, y_start)))
            result.append(PA((x_start + width_each, y_start - height_each)))
            result.append(PA((x_start, y_start - height_each)))
            result.append(PA((x_start, y_start)))
            result.append(PU())
      
      return result
      
'''
   


      
'''
      
      
      
