from chiplotle.hpgl.compound.abstractpath import _AbstractPath
from chiplotle.hpgl.commands import PU, PD, PA
from chiplotle.tools.mathtools import catmull_interpolation


class Catmull(_AbstractPath):
   '''Catmull-Rom spline interpolation'''

   _scalable = _AbstractPath._scalable 

   def __init__(self, points, interpolation_count=None, xy=None):
      xy = xy or (0, 0)
      _AbstractPath.__init__(self, points, interpolation_count, xy) 


   @property
   def _subcommands(self):
      plot_points = catmull_interpolation(self.points, self.interpolation_count)

      result = _AbstractPath._subcommands.fget(self)
      result.append(PA(self.xy + tuple(plot_points[0])))
      result.append(PD( ))

      for point_tuple in tuple(plot_points[1:]):
         position = self.xy + point_tuple
         result.append(PA(position))
      position = self.xy + self.points[-2]
      result.append(PA(position))
      result.append(PU( ))

      return result
