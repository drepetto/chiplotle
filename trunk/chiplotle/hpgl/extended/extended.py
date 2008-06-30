from chiplotle.hpgl.abstract.positional import _Positional
from chiplotle.hpgl.scalable import Scalable

class _ExtendedHPGL(_Positional):
   def __init__(self, xy):
      _Positional.__init__(self, xy, True) 

   def __str__(self):
      result = ''
      for c in self._subcommands:
         result += c.format
      return result

