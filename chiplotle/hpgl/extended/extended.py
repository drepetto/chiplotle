from chiplotle.hpgl.abstract.positional import _Positional
from chiplotle.hpgl.commands import SP
from chiplotle.hpgl.scalable import Scalable

class _CompoundHPGL(_Positional):
   def __init__(self, xy, pen=None):
      _Positional.__init__(self, xy, True) 
      self.pen = pen
      self._parent = None

   @property
   def xyabsolute(self):
      if self._parent:
         return self._parent.xyabsolute + self.xy
      else:
         return self.xy

   @property
   def xabsolute(self):
      return self._getAbsCoord(0)

   @property
   def yabsolute(self):
      return self._getAbsCoord(1)

   def _getAbsCoord(self, n):
      result = self.xyabsolute[n::2]
      if len(result) == 1:
         return result[0]
      else:
         return result



   ### FORMATTING ### 

   @property
   def _subcommands(self):
      result = [ ]
      if not self.pen is None:
         result.append(SP(self.pen))
      return result

   @property
   def format(self):
      result = ''
      for c in self._subcommands:
         result += c.format
      return result

