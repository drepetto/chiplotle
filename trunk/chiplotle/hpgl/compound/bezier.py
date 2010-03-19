from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.commands import PU, PD, PA, PR, LT
from chiplotle.hpgl.scalable import Scalable
from chiplotle.utils.geometry import *
from chiplotle.tools.mathtools import bezier_interpolation


class Bezier(_CompoundHPGL):
   '''Bezier curve interpolation'''
   def __init__(self, control_points, xy=None, points_to_compute=None, weight=None, draw_controls=False, pen=None):
      self.control_points = Scalable(control_points)
      self.points_to_compute = points_to_compute or 100
      if ((type(weight) is list) and len(weight) > 0):      
            l_w = len(weight)
            l_p = len(self.control_points)
            self.w = weight*(l_p//l_w)+weight[:l_p%l_w] 
      else:
         self.w = 1
      self.draw_controls = draw_controls
      xy = xy or (0, 0)
      _CompoundHPGL.__init__(self, xy, pen) 


   @property
   def _subcommands(self):
      plot_points = bezier_interpolation(
         self.control_points, 
         self.points_to_compute, self.w)

      result = _CompoundHPGL._subcommands.fget(self)
      result.append(PU( ))
      result.append(PA(self.xyabsolute + plot_points[0]))
      result.append(PD( ))

      for point_tuple in plot_points[1:]:
         position = self.xyabsolute + point_tuple
         result.append(PA(position))
      result.append(PU( ))
      if self.draw_controls:
         if self.draw_controls == 2:
            ## draws the polygon defined by control points with dashed line
            result.append(PA(self.xyabsolute + self.control_points[0]))
            result.append(PD( ))
            result.append(LT(2))
            for point_tuple in self.control_points[1:]:
               position = self.xyabsolute + point_tuple
               result.append(PA(position))
            result.append(LT( ))
            result.append(PU( ))
         elif self.draw_controls == 1:
            ## draws crosses at control points
            for point_tuple in self.control_points:
               result.append(PA(self.xyabsolute + point_tuple))
               result.append(PR((-50,0)))
               result.append(PD( ))
               result.append(PR((100,0)))
               result.append(PU( ))
               result.append(PR((-50,50)))
               result.append(PD( ))
               result.append(PR((0,-100)))
               result.append(PU( ))

      return result
