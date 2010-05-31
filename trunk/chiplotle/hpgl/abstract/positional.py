from chiplotle.hpgl.abstract.hpglprimitive import _HPGLPrimitive
from chiplotle.hpgl.coordinatearray import CoordinatePair


class _Positional(_HPGLPrimitive):
   '''For those primitive HPGL commands that have an (x, y) position pair.'''   
   _scalable = ['xy']

   def __init__(self, xy):
      self.xy = xy

   ## PUBLIC ATTRIBUTES ##  

   @apply
   def xy( ):
      def fget(self):
         return self._coords
      def fset(self, arg):
         self._coords = CoordinatePair(arg)
      return property(**locals())

   @apply
   def x( ):
      def fget(self):
         return self._coords.x
      def fset(self, arg):
         self.xy = CoordinatePair(arg, self.y)
      return property(**locals())

   @apply
   def y( ):
      def fget(self):
         return self._coords.y
      def fset(self, arg):
         self.xy = CoordinatePair(self.x, arg)
      return property(**locals())



   ### FORMATTING ###

   @property
   def format(self):
      if isinstance(self.x, int) and isinstance(self.y, int):
         coordinates = '%i,%i' % (self.x, self.y)
      else:
         coordinates = '%.2f,%.2f' % (self.x, self.y)
      return '%s%s%s' % (self._name, coordinates, _HPGLPrimitive._terminator)
