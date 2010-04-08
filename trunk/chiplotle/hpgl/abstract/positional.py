from chiplotle.hpgl.abstract.hpglcommand import _HPGLCommand
#from chiplotle.hpgl.scalable import Scalable
from chiplotle.hpgl.coordinatearray import CoordinateArray


class _Positional(_HPGLCommand):
   def __init__(self, xy, transposable=True):
      assert isinstance(transposable, bool)
      self._transposable = transposable
      self.xy = xy

   ### MANAGED ATTRIBUTES ###  

   @apply
   def xy( ):
      def fget(self):
         return self._coords
      def fset(self, arg):
         if arg is None:
            arg = [ ]
         #assert len(arg) % 2 == 0
         #self._xy = Scalable(arg).ravel( )
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

#   def _getCoord(self, n):
#      '''Helper function for x( ) and y( ).'''
#      result = self.xy[n::2]
#      if len(result) == 1:
#         return result[0]
#      else:
#         return result

   ### FORMATTING ###

   @property
   def format(self):
      if self._coords.dtype == int:
         coordinates = ['%i,%i' % tuple(p) for p in self.xy]
      else:
         coordinates = ['%.2f,%.2f' % tuple(p) for p in self.xy]
      return '%s%s%s' % (self._name, ','.join(coordinates), 
         _HPGLCommand._terminator)
