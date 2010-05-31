from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.commands import PU, PD, PA
from chiplotle.hpgl.coordinatearray import CoordinateArray
from chiplotle.utils.geometry import *
from chiplotle.tools.mathtools import catmull_interpolation


class Catmull(_CompoundHPGL):
   '''Catmull-Rom spline interpolation'''

   _scalable = ['control_points']

   def __init__(self, control_points, xy=None, points_to_compute=None, pen=None):
      self.control_points = CoordinateArray(control_points)
      self.points_to_compute = points_to_compute or 100
      xy = xy or (0, 0)
      _CompoundHPGL.__init__(self, xy, pen) 


   @property
   def _subcommands(self):
      plot_points = catmull_interpolation(
         self.control_points, 
         self.points_to_compute)

      result = _CompoundHPGL._subcommands.fget(self)
      result.append(PU( ))
      result.append(PA(self.xyabsolute + tuple(plot_points[0])))
      result.append(PD( ))

      for point_tuple in tuple(plot_points[1:]):
         position = self.xyabsolute + point_tuple
         result.append(PA(position))
      position = self.xyabsolute + self.control_points[-2]
      result.append(PA(position))
      result.append(PU( ))

      return result
