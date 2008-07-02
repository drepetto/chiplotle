from chiplotle.hpgl.abstract.positional import _Positional
from chiplotle.hpgl.commands import SP
from chiplotle.hpgl.scalable import Scalable

class _ExtendedHPGL(_Positional):
   def __init__(self, xy, pen=None):
      _Positional.__init__(self, xy, True) 
      self.pen = pen

   @property
   def _subcommands(self):
      result = [ ]
      if not self.pen is None:
         result.append(SP(self.pen))
      return result

   def __str__(self):
      result = ''
      for c in self._subcommands:
         result += c.format
      return result

