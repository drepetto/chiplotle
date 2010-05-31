from chiplotle.hpgl.abstract.hpglprimitive import _HPGLPrimitive
from chiplotle.hpgl.coordinatearray import CoordinateArray


class _PenPlot(_HPGLPrimitive):
   '''For those primitive HPGL commands that can take multiple 
   x,y,x,y,... coordinates. 
   g.e., PA( ).'''

   _scalable = ['xy']

   def __init__(self, xy):
      self.xy = xy

   ### MANAGED ATTRIBUTES ###  

   @apply
   def xy( ):
      def fget(self):
         return self._coords
      def fset(self, arg):
         #if arg is None:
         #   arg = [ ]
         self._coords = CoordinateArray(arg)
      return property(**locals())

   @apply
   def x( ):
      def fget(self):
         return self._coords.x
      def fset(self, arg):
         self.xy.x = arg
      return property(**locals())

   @apply
   def y( ):
      def fget(self):
         return self._coords.y
      def fset(self, arg):
         self.xy.y = arg
      return property(**locals())


   ### FORMATTING ###

   @property
   def format(self):
      if self._coords.dtype == int:
         coordinates = ['%i,%i' % tuple(p) for p in self.xy]
      else:
         coordinates = ['%.2f,%.2f' % tuple(p) for p in self.xy]
      return '%s%s%s' % (self._name, ','.join(coordinates), 
         _HPGLPrimitive._terminator)
