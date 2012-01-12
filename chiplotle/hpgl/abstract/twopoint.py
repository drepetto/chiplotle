from chiplotle.hpgl.abstract.hpglprimitive import _HPGLPrimitive
from chiplotle.geometry.core.coordinatearray import CoordinateArray

class _TwoPoint(_HPGLPrimitive):
   '''Abstract class for commands with 2 coordinate pairs: x1, y1, x2, y2.'''
   def __init__(self, coords=None):
      self.coords = coords
      if self.coords and len(self.coords) != 2:
            raise ValueError('Only two coordinate pairs allowed.')


   @apply
   def coords( ):
      def fget(self):
         return self._coords
      def fset(self, arg):
         self._coords = CoordinateArray(arg)
      return property(**locals())


   @property
   def format(self):
      if self.coords:
         coords = self.coords[0].xy + self.coords[1].xy
         coords = map(str, coords)
         coords = ','.join(coords)
         return '%s%s%s' % (self._name, coords, _HPGLPrimitive._terminator)
      else:
         return '%s%s' % (self._name, _HPGLPrimitive._terminator)

