from chiplotle.hpgl.abstract.positional import _Positional
from chiplotle.hpgl.commands import SP
from chiplotle.hpgl.compound.pen import Pen
from chiplotle.hpgl.scalable import Scalable
import types

class _CompoundHPGL(_Positional):
   def __init__(self, xy, pen=None):
      _Positional.__init__(self, xy, True) 
      self._parent = None
      self.pen = pen


   @apply
   def pen( ):
      def fget(self):
         return self._pen

      def fset(self, pen):
         if isinstance(pen, int):
            self._pen = Pen(pen)
         elif isinstance(pen, (Pen, types.NoneType)):
            self._pen = pen
         else:
            raise TypeError('pen must be a Pen( ) instance, int or None.')

      return property(**locals( ))
         

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

   ### TODO should _subcommands return a Generator rather than a list?
   @property
   def _subcommands(self):
      result = [ ]
      if self.pen:
         #result.append(SP(self.pen))
         result.append(self.pen)
      return result


   @property
   def format(self):
      result = ''
      for c in self._subcommands:
         result += c.format
      return result

