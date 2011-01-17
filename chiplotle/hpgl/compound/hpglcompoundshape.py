from chiplotle.hpgl.compound.hpglcompound import _HPGLCompound
from chiplotle.geometry.vector import Vector
from chiplotle.hpgl.commands import PU, PA


class _HPGLCompoundShape(_HPGLCompound):
   '''
   Interface (must implement):
      - `_subcommands`
      - `points`
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
         self._coords = Vector(*arg)
      return property(**locals())

   @apply
   def x( ):
      def fget(self):
         return self._coords.x
      def fset(self, arg):
         self.xy = Vector(arg, self.y)
      return property(**locals())

   @apply
   def y( ):
      def fget(self):
         return self._coords.y
      def fset(self, arg):
         self.xy = Vector(self.x, arg)
      return property(**locals())


   ## PRIVATE PROPERTIES ##

   @property
   def _subcommands(self):
      #return [PU( ), PA(self.xy)]
      return [PU( ), PA([self.xy])]

   def points(self):
      pass
      
