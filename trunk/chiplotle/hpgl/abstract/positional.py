from chiplotle.hpgl.abstract.hpglcommand import _HPGLCommand
from chiplotle.hpgl.scalable import Scalable


class _Positional(_HPGLCommand):
   def __init__(self, xy, transposable=True):
      assert isinstance(transposable, bool)
      self._transposable = transposable
      self.xy = xy

   ### MANAGED ATTRIBUTES ###  

   @apply
   def xy( ):
      def fget(self):
         return self._xy
      def fset(self, arg):
         if arg is None:
            arg = [ ]
         assert len(arg) % 2 == 0
         self._xy = Scalable(arg).ravel( )
      return property(**locals())

   @apply
   def x( ):
      def fget(self):
         return self._getCoord(0)
      def fset(self, arg):
         self.xy[0::2] = arg
      return property(**locals())

   @apply
   def y( ):
      def fget(self):
         return self._getCoord(1)
      def fset(self, arg):
         self.xy[1::2] = arg
      return property(**locals())

   def _getCoord(self, n):
      '''Helper function for x( ) and y( ).'''
      result = self.xy[n::2]
      if len(result) == 1:
         return result[0]
      else:
         return result

   ### FORMATTING ###

   @property
   def format(self):
      coordinates = ['%s' % p for p in self.xy]
      return '%s%s%s' % (self._name, ','.join(coordinates), _HPGLCommand._terminator)
