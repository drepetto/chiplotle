from chiplotle.hpgl.compound.hpglcompound import _HPGLCompound
from chiplotle.hpgl.coordinatepair import CoordinatePair
from chiplotle.hpgl.commands import PU, PA


class _HPGLCompoundShape(_HPGLCompound):
   '''
   Interface (must implement):
      - `_subcommands`
   '''
   
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


   ## PRIVATE PROPERTIES ##

   @property
   def _subcommands(self):
      return [PU( ), PA(self.xy)]
