from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.commands import PU, PD, PA, PR
from chiplotle.utils.geometry import *

class Cross(_CompoundHPGL):
   '''Cross. Can be rotated.'''

   _scalable = ['width', 'height']

   def __init__(self, xy, width, height, rotation=0, pen=None):
      _CompoundHPGL.__init__(self, xy, pen) 
      self.width = width
      self.height = height
      self.rotation = rotation

   @property
   def _subcommands(self):
      left = (-self.width / 2., 0)
      right = (self.width / 2., 0)
      top = (0, self.height / 2.) 
      bottom = (0, -self.height / 2.) 
      ## rotate ...
      left = rotate2d(left, self.rotation)
      right = rotate2d(right, self.rotation)
      top = rotate2d(top, self.rotation)
      bottom = rotate2d(bottom, self.rotation)

      result = _CompoundHPGL._subcommands.fget(self)
      result.append(PA( ))
      result.append(PU(self.xyabsolute + left))
      result.append(PD(self.xyabsolute + right))
      result.append(PU(self.xyabsolute + top))
      result.append(PD(self.xyabsolute + bottom))
      result.append(PU( ))
      return result
