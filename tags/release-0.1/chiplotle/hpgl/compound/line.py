from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.commands import PU, PD, PA

class Line(_CompoundHPGL):
   '''Line at absolute position.'''
   ## TODO: make interface consistent with the rest. 
   ## positional argument should be 1.
   def __init__(self, x1, y1, x2, y2):
      _CompoundHPGL.__init__(self, (x1, y1, x2, y2))
      
   @property
   def _subcommands(self):
      result = _CompoundHPGL._subcommands.fget(self)
      result+=[PU( ), 
               PA(self.xyabsolute[0:2]),
               PD(self.xyabsolute[2:4]),
               PU()]
      return result

