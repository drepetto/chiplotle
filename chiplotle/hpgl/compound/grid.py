from __future__ import division
from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.commands import PU, PD, PA, PR
from chiplotle.hpgl.scalable import Scalable

class Grid(_CompoundHPGL):
   '''Rectangular grid. '''
   def __init__(self, xy, width, height, width_line_count, 
      height_line_count, pen=None):
      _CompoundHPGL.__init__(self, xy, pen = pen) 
      self.width = Scalable(width)
      self.height = Scalable(height)
      self.widthLineCount = width_line_count
      self.heightLineCount = height_line_count
      self.referencePoint = (0, 0) ## range: [0 to 1]


   @property
   def _subcommands(self):
      ul_x = self.xabsolute - self.referencePoint[0] * self.width
      bl_x = ul_x
      ur_x = ul_x + self.width
      br_x = ur_x

      ul_y = self.yabsolute + self.referencePoint[1] * self.height
      ur_y = ul_y
      bl_y = ul_y - self.height
      br_y = bl_y

      ul = (ul_x, ul_y)
      bl = (bl_x, bl_y)
      ur = (ur_x, ur_y)
      br = (br_x, br_y)

      result = _CompoundHPGL._subcommands.fget(self)
      ## add horizontal lines
      for i in range(self.heightLineCount):
         step_y = self.height / self.heightLineCount * i
         result.append( PU(( ))
         result.append( PR((ul_x, ul_y - step_y))
         result.append( PD(( ))
         result.append( PR((ur_x, ur_y - step_y))
      ## add vertical lines
      for i in range(self.widthLineCount):
         step_x = self.width / self.widthLineCount * i
         result.append( PU(( ))
         result.append( PR((ul_x + step_x, ul_y))
         result.append( PD(( ))
         result.append( PR((bl_x + step_x, bl_y))

      result.append(PU( ))
      return result

