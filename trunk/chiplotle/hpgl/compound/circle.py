from chiplotle.hpgl.commands import PU, CI, WG
from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.scalable import Scalable

class Circle(_CompoundHPGL):
   '''Circle with absolute position.'''
   def __init__(self, xy, radius, chord=None, filled=False, pen=None):
      _CompoundHPGL.__init__(self, xy, pen)
      self.radius = Scalable(radius)
      self.chord = chord
      self.filled = filled
      
   @property
   def _subcommands(self):
      result = _CompoundHPGL._subcommands.fget(self)
      result.append(PU(self.xyabsolute))
      if self.filled:
         result.append(WG(self.radius, 0, 359))
      else:
         result.append(CI(self.radius, self.chord))
      return result