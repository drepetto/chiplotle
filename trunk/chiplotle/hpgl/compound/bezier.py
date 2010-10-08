from chiplotle.hpgl.compound.abstractpath import _AbstractPath
from chiplotle.hpgl.commands import PU, PD, PA, PR, LT
from chiplotle.hpgl.coordinatearray import CoordinateArray
from chiplotle.tools.mathtools import bezier_interpolation


class Bezier(_AbstractPath):
   '''Bezier curve interpolation'''

   _scalable = _AbstractPath._scalable 

   def __init__(self, points, interpolation_count=None, weight=None, 
      control_marks=False, xy=None):

      xy = xy or (0, 0)
      _AbstractPath.__init__(self, points, interpolation_count, xy) 
      
      ## set weights...
      if ((type(weight) is list) and len(weight) > 0):      
            l_w = len(weight)
            l_p = len(self.points)
            self.weight = weight*(l_p//l_w)+weight[:l_p%l_w] 
      else:
         self.weight = 1
         
      self.control_marks = control_marks


   ## METHODS ##

   def _get_control_marks_html(self):
      result = [ ]
      if self.control_marks:
         if (self.control_marks == "lines" or self.control_marks == "line"):
            ## draws the polygon defined by control points with dashed line...
            result.append(PA(self.xy + self.points[0]))
            result.append(PD( ))
            result.append(LT(2))
            for point_tuple in self.points[1:]:
               position = self.xy + point_tuple
               result.append(PA(position))
            result.append(LT( ))
            result.append(PU( ))
         elif (self.control_marks == "crosses" or self.control_marks == "cross"):
            ## draws crosses at control points......
            for point_tuple in self.points:
               result.append(PA(self.xy + point_tuple))
               result.append(PR((-50,0)))
               result.append(PD( ))
               result.append(PR((100,0)))
               result.append(PU( ))
               result.append(PR((-50,50)))
               result.append(PD( ))
               result.append(PR((0,-100)))
               result.append(PU( ))
      return result

   @property
   def _subcommands(self):
      plot_points = bezier_interpolation(
         self.points.as_list_of_pairs( ), 
         self.interpolation_count, self.weight)

      result = _AbstractPath._subcommands.fget(self)
      result.append(PA(self.xy + plot_points[0]))
      result.append(PD( ))

      for point_tuple in plot_points[1:]:
         position = self.xy + point_tuple
         result.append(PA(position))
      result.append(PU( ))
      ## get control marks...
      result += self._get_control_marks_html( )

      return result
