from chiplotle.hpgl.abstract.positional import _Positional
from chiplotle.hpgl.commands import SP
from chiplotle.hpgl.compound.pen import Pen
from chiplotle.interfaces.parentage.interface import ParentageInterface
import types

## TODO: check that xy is a pair *always*?
class _CompoundHPGL(_Positional):
   def __init__(self, xy, pen=None):
      _Positional.__init__(self, xy, True) 
      self.pen = pen
      self._parentage = ParentageInterface(self)

   ## PUBLIC ATTRIBUTES ##

   @property
   def format(self):
      result = ''
      for c in self._subcommands:
         result += c.format
      return result

   @property
   def parentage(self):
      return self._parentage

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
      if self.parentage.parent:
         return self.parentage.parent.xyabsolute + self.xy
      else:
         return self.xy

   @property
   def xabsolute(self):
      #return self._getAbsCoord(0)
      if self.parentage.parent:
         return self.parentage.parent.xabsolute + self.x
      else:
         return self.x

   @property
   def yabsolute(self):
      #return self._getAbsCoord(1)
      if self.parentage.parent:
         return self.parentage.parent.yabsolute + self.y
      else:
         return self.y


   ## PRIVATE ATTRIBUTES ##

   ### TODO should _subcommands return a Generator rather than a list?
   @property
   def _subcommands(self):
      result = [ ]
      if self.pen:
         #result.append(SP(self.pen))
         result.append(self.pen)
      return result


