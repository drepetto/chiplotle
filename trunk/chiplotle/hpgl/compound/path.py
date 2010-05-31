from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.commands import PU, PD, PA
from chiplotle.hpgl.coordinatearray import CoordinateArray
from chiplotle.utils.geometry import *
from chiplotle.tools.mathtools import bezier_interpolation


class Path(_CompoundHPGL):
   '''draws a path given a list of waypoints'''

   _scalable = ['points']

   def __init__(self, points, xy=None, curvature=1.0, points_to_compute=None, pen=None):
      self.points = points
      self.curvature = curvature
      ## points_to_compute determines the number of points calculated for 
      ## each step of the curve
      self.points_to_compute = points_to_compute or 50
      xy = xy or (0, 0)
      _CompoundHPGL.__init__(self, xy, pen) 


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

   @apply
   def points( ):
      def fget(self):
         return self._points
      def fset(self, arg):
         ## TODO: check that there are at least three points.
         self._points = CoordinateArray(arg)
      return property(**locals( ))

   ## PRIVATE METHODS ##

   def _get_straight_line_hpgl(self):
      result = [ ]
      plot_points = self.points
      result.append(PU( ))
      result.append(PA(self.xyabsolute + plot_points[0]))
      result.append(PD( ))
      for point_tuple in plot_points[1:]:
         position = self.xyabsolute + point_tuple
         result.append(PA(position))
      result.append(PU( ))
      return result

   def _get_bezier_line_hpgl(self):
      curvature = 4 + (1.0-self.curvature) * 40
      dx = {0: 0, len(self.points)-1: 0}
      dy = {0: 0, len(self.points)-1: 0}
      bi = {1: -0.25}
      ax = {1: (self.points[2][0]-self.points[0][0]-dx[0]) / 4}
      ay = {1: (self.points[2][1]-self.points[0][1]-dy[0]) / 4}

      for i in range(2, len(self.points)-1):
         bi[i] = -1 / (curvature + bi[i-1])
         ax[i] = -(self.points[i+1][0] - self.points[i-1][0] - ax[i-1]) * bi[i]
         ay[i] = -(self.points[i+1][1] - self.points[i-1][1] - ay[i-1]) * bi[i]

      r = range(1, len(self.points)-1)
      r.reverse( )
      for i in r:
         dx[i] = ax[i] + dx[i+1] * bi[i]
         dy[i] = ay[i] + dy[i+1] * bi[i]

      result = [ ]
      result.append(PU( ))
      result.append(PA(self.xyabsolute + self.points[0]))
      result.append(PD( ))
      for i in range(len(self.points) - 1):
         control_points = [(self.points[i][0], self.points[i][1]),
            (self.points[i][0] + dx[i], self.points[i][1] + dy[i]),
            (self.points[i+1][0] - dx[i+1], self.points[i+1][1] - dy[i+1]),
            (self.points[i+1][0], self.points[i+1][1])]
#         plot_points = bezier_interpolation(control_points, 
#            self.points_to_compute)
         plot_points = bezier_interpolation(control_points, 
            self.points_to_compute, 1)
         for point_tuple in plot_points:
            position = self.xyabsolute + point_tuple
            result.append(PA(position))
      result.append(PU( ))
      return result
      

   @property
   def _subcommands(self):
      result = _CompoundHPGL._subcommands.fget(self)
      if self.curvature == 0:
         result.extend(self._get_straight_line_hpgl( ))
      else:
         result.extend(self._get_bezier_line_hpgl( ))
      return result
