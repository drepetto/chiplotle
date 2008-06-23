from chiplotle.hpgl.abstract.hpglcommand import _HPGLCommand
from chiplotle.hpgl.scalable import Scalable


class _Positional(_HPGLCommand):
   def __init__(self, xy, transposable=True):
      if not xy is None:
         assert len(xy) % 2 == 0
         self._xy = Scalable(xy).ravel()
      else:
         self._xy = Scalable([])
      assert isinstance(transposable, bool)
      self._transposable = transposable

   ### MANAGED ATTRIBUTES ###  

   @apply
   def xy( ):
      def fget(self):
         return self._xy
      def fset(self, arg):
         self._xy = Scalable(arg)
      return property(**locals())

   @apply
   def x( ):
      def fget(self):
         x = self.xy[0::2]
         if len(x) == 1:
            return x[0]
         else:
            return x
      def fset(self, arg):
         self.xy[0::2] = arg
      return property(**locals())

   @apply
   def y( ):
      def fget(self):
         y = self.xy[1::2]
         if len(y) == 1:
            return y[0]
         else:
            return y
      def fset(self, arg):
         self.xy[1::2] = arg
      return property(**locals())

   ### OVERRIDES ###

   def __str__(self):
      coordinates = [str(p) for p in self.xy]
      return '%s%s%s' % (self._name, ','.join(coordinates), self.terminator)
