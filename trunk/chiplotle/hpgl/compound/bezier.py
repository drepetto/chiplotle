from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.commands import PU, PD, PA
from chiplotle.hpgl.scalable import Scalable
from chiplotle.utils.geometry import *
from chiplotle.tools.mathtools import bezier_interpolation


class Bezier(_CompoundHPGL):
   '''Bezier curve aproximation'''
   def __init__(self, control_points, xy=None, points_to_compute=None):
      self.control_points = Scalable(control_points)
      self.points_to_compute = points_to_compute or 100
      xy = xy or (0, 0)
      _CompoundHPGL.__init__(self, xy) 


   @property
   def _subcommands(self):
      plot_points = bezier_interpolation(
         self.control_points, 
         self.points_to_compute)

      result = _CompoundHPGL._subcommands.fget(self)
      result.append(PU( ))
      result.append(PA(self.xyabsolute + plot_points[0]))
      result.append(PD( ))

      for point_tuple in plot_points[1:]:
         position = self.xyabsolute + point_tuple
         result.append(PA(position))
      result.append(PU( ))

      return result
