from chiplotle.hpgl.commands import PU, CI, WG
from chiplotle.hpgl.compound.compound import _CompoundHPGL

class Circle(_CompoundHPGL):
   '''Circle with absolute position.'''
   
   _scalable = _CompoundHPGL._scalable + ['radius']

   def __init__(self, xy, radius, chord=None, filled=False, pen=None):
      _CompoundHPGL.__init__(self, xy, pen)
      self.radius = radius
      self.chord = chord
      self.filled = filled
      
   @property
   def _subcommands(self):
      result = _CompoundHPGL._subcommands.fget(self)
      if self.filled:
         result.append(WG(self.radius, 0, 359))
      else:
         result.append(CI(self.radius, self.chord))
      return result


   ## OVERRIDES ##
   
   def __repr__(self):
      return "Circle(%s, %s)" % (self.xy, self.radius)
