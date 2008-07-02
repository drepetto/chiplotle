from chiplotle.hpgl.commands import PU, CI, WG
from chiplotle.hpgl.extended.extended import _ExtendedHPGL
from chiplotle.hpgl.scalable import Scalable

class Circle(_ExtendedHPGL):
   '''Circle with absolute position.'''
   def __init__(self, x, y, radius, chord=11.25, filled=False, pen=None):
      _ExtendedHPGL.__init__(self, (x, y), pen)
      self.radius = Scalable(radius)
      self.chord = chord
      self.filled = filled
      
   @property
   def _subcommands(self):
      result = _ExtendedHPGL._subcommands.fget(self)
      result.append(PU(self.xy))
      if self.filled:
         result.append(WG(self.radius, 0, 359))
      else:
         result.append(CI(self.radius, self.chord))
      return result
