from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.compound.circle import Circle
from chiplotle.tools.mathtools.polar_to_xy import polar_to_xy
import math

class BooleanCycle(_CompoundHPGL):

   _scalable = _CompoundHPGL._scalable + ['radius', 'booleans_radius']

   def __init__(self, xy, radius, booleans, booleans_radius, draw_main_circle=True):
      _CompoundHPGL.__init__(self, xy)
      self.radius = radius
      self.booleans = booleans
      self.booleans_radius = booleans_radius
      self.draw_main_circle = draw_main_circle


   @apply
   def booleans( ):
      def fget(self):
         return self._booleans
      def fset(self, arg):
         if not isinstance(arg, (list, tuple)):
            raise TypeError('`arg` must be a list or tuple of booleans')
         self._booleans = arg
      return property(**locals( ))


   def _get_inter_true_interval_numbers(self):
      if self.draw_inter_true_intervals:
         ## get intervals...
         pass

      
   def _get_main_circle(self):
      if self.draw_main_circle:
         return [Circle(self.xy, self.radius, filled=False)]
      else:
         return [ ]

   def _get_boolean_beads(self):
      '''Returns the little boolean "bead" circles along the main radius.'''
      angle_delta = math.pi * 2 / len(self.booleans)
      angle = 0
      result = [ ]
      for b in self.booleans:
         ## get xy...
         xy = polar_to_xy(self.radius, angle)
         xy += self.xy
         if b: ## filled circle
            result.append(Circle(xy, self.booleans_radius, filled=True))
         else: ## empty
            result.append(Circle(xy, self.booleans_radius, filled=False))
         angle += angle_delta
      return result

   @property
   def _subcommands(self):
      result = _CompoundHPGL._subcommands.fget(self)
      result += self._get_main_circle( )
      result += self._get_boolean_beads( )
      return result

