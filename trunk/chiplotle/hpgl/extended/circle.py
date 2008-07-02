from chiplotle.hpgl.commands import PU, CI
from chiplotle.hpgl.extended.extended import _ExtendedHPGL
from chiplotle.hpgl.scalable import Scalable

class Circle(_ExtendedHPGL):
   '''Circle with absolute position.'''
   def __init__(self, x, y, radius, chord=11.25, pen=None):
      _ExtendedHPGL.__init__(self, (x, y), pen)
      self.radius = Scalable(radius)
      self.chord = chord
      
   @property
   def _subcommands(self):
      result = _ExtendedHPGL._subcommands.fget(self)
      result += [PU(self.xy), CI(self.radius, self.chord)]
      return result
