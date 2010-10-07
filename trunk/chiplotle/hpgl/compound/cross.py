from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.commands import PU, PD, PA, PR
from chiplotle.tools.mathtools import rotate_2d

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
      left = rotate_2d(left, self.rotation)
      right = rotate_2d(right, self.rotation)
      top = rotate_2d(top, self.rotation)
      bottom = rotate_2d(bottom, self.rotation)

      result = _CompoundHPGL._subcommands.fget(self)
      result.append(PA(self.xy + left))
      result.append(PD( ))
      result.append(PA(self.xy + right))
      result.append(PU( ))
      result.append(PA(self.xy + top))
      result.append(PD( ))
      result.append(PA(self.xy + bottom))
      result.append(PU( ))
      return result
