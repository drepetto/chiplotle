from chiplotle.hpgl.compound.abstractpath import _AbstractPath
from chiplotle.hpgl.commands import PU, PD, PA
from chiplotle.tools.mathtools import bezier_interpolation


class Path(_AbstractPath):
   '''draws a path given a list of waypoints'''

   _scalable = _AbstractPath._scalable 

   def __init__(self, points, interpolation_count=None, curvature=1.0, xy=None):
      xy = xy or (0, 0)
      _AbstractPath.__init__(self, points, interpolation_count, xy) 
      self.curvature = curvature


   ## PUBLIC PROPERTIES ##

   @apply
   def curvature( ):
      def fget(self):
         return self._curvature
      def fset(self, arg):
         if 0 <= arg and arg <= 1:
            self._curvature = arg
         else:
            raise ValueError('curvature must be between 0 and 1 inclusive.')
      return property(**locals( ))

   ## PRIVATE METHODS ##

   def _get_straight_line_hpgl(self):
      result = [ ]
      plot_points = self.points
      result.append(PU( ))
      result.append(PA(self.xy + plot_points[0]))
      result.append(PD( ))
      for point_tuple in plot_points[1:]:
         position = self.xy + point_tuple
         result.append(PA(position))
      result.append(PU( ))
      return result

   def _get_bezier_line_hpgl(self):
      curvature = 4 + (1.0-self.curvature) * 40
      dx = {0: 0, len(self.points)-1: 0}
      dy = {0: 0, len(self.points)-1: 0}
      bi = {1: -0.25}
      ax = {1: (self.points[2].x - self.points[0].x - dx[0]) / 4}
      ay = {1: (self.points[2].y - self.points[0].y - dy[0]) / 4}

      for i in range(2, len(self.points)-1):
         bi[i] = -1 / (curvature + bi[i-1])
         ax[i] = -(self.points[i+1].x - self.points[i-1].x - ax[i-1]) * bi[i]
         ay[i] = -(self.points[i+1].y - self.points[i-1].y - ay[i-1]) * bi[i]

      r = range(1, len(self.points)-1)
      r.reverse( )
      for i in r:
         dx[i] = ax[i] + dx[i+1] * bi[i]
         dy[i] = ay[i] + dy[i+1] * bi[i]

      result = [ ]
      result.append(PU( ))
      result.append(PA(self.xy + self.points[0]))
      result.append(PD( ))
      for i in range(len(self.points) - 1):
         control_points = [(self.points[i].x, self.points[i].y),
            (self.points[i].x + dx[i], self.points[i].y + dy[i]),
            (self.points[i+1].x - dx[i+1], self.points[i+1].y - dy[i+1]),
            (self.points[i+1].x, self.points[i+1].y)]
         plot_points = bezier_interpolation(control_points, 
            self.interpolation_count, 1)
         for point_tuple in plot_points:
            position = self.xy + point_tuple
            result.append(PA(position))
      result.append(PU( ))
      return result
      

   @property
   def _subcommands(self):
      result = _AbstractPath._subcommands.fget(self)
      if self.curvature == 0:
         result.extend(self._get_straight_line_hpgl( ))
      else:
         result.extend(self._get_bezier_line_hpgl( ))
      return result
