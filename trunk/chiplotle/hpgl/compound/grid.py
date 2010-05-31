from __future__ import division
from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.commands import PU, PD, PA, PR

class Grid(_CompoundHPGL):
   '''Rectangular grid. 

   - `xy` : ``tuple``, (x, y) position.
   - `width` : ``int`` or ``float``, width of the rectangle.
   - `height` : ``int`` or ``float``, height of the rectangle.
   - `width_divisions` : ``int``, number of horizontal equidistant partitions.
   - `horizontal_divisions` : ``int``, number of vertical equidistant 
      partitions.
   - `pen` : ``int``, pen number.
   
   '''

   _scalable = ['width', 'height']

   def __init__(self, xy, width, height, height_divisions, 
      width_divisions, pen=None):
      _CompoundHPGL.__init__(self, xy, pen = pen) 
      self.width = width
      self.height = height
      self.height_divisions = height_divisions
      self.width_divisions = width_divisions
      self.reference_point = (0, 0) ## range: [0 to 1]


   @property
   def _subcommands(self):
      ul_x = self.xabsolute - self.reference_point[0] * self.width
      bl_x = ul_x
      ur_x = ul_x + self.width

      ul_y = self.yabsolute + self.reference_point[1] * self.height
      ur_y = ul_y
      bl_y = ul_y - self.height


      result = _CompoundHPGL._subcommands.fget(self)
      ## add horizontal lines
      for i in range(self.width_divisions + 1):
         step_y = self.height / self.width_divisions * i
         result.append(PU( ))
         result.append(PA((ul_x, ul_y - step_y)))
         result.append(PD( ))
         result.append(PA((ur_x, ur_y - step_y)))
      ## add vertical lines
      for i in range(self.height_divisions + 1):
         step_x = self.width / self.height_divisions * i
         result.append(PU( ))
         result.append(PA((ul_x + step_x, ul_y)))
         result.append(PD( ))
         result.append(PA((bl_x + step_x, bl_y)))

      result.append(PU( ))
      return result

