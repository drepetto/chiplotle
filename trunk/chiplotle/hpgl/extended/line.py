from chiplotle.hpgl.extended.extended import _ExtendedHPGL
from chiplotle.hpgl.commands import PU, PD, PA

class Line(_ExtendedHPGL):
   '''Line at absolute position.'''
   def __init__(self, x1, y1, x2, y2):
      _ExtendedHPGL.__init__(self, (x1, y1, x2, y2))
      
   @property
   def _subcommands(self):
      result = _ExtendedHPGL._subcommands.fget(self)
      result+=[PU( ), 
               PA(self.xyabsolute[0:2]),
               PD(self.xyabsolute[2:4]),
               PU()]
      return result

