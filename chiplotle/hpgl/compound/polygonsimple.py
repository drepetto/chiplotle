from chiplotle.hpgl.compound.hpglcompoundshape import _HPGLCompoundShape
from chiplotle.hpgl.coordinatepair import CoordinatePair
from chiplotle.hpgl.commands import PU, PD, PA

class PolygonSimple(_HPGLCompoundShape):
   '''A simple polygon, e.g. one that is simply a closed path.
      points is an [] of CoordinatePairs.
      If first_point != last_point then one final point 
      (a duplicate of the first point) will be added to close the polygon.   
   '''

   _scalable = _HPGLCompoundShape._scalable + ['width', 'height']

   def __init__(self, xy, points):
      _HPGLCompoundShape.__init__(self, xy)           
      self.points = points
      
      first_point = self.points[0]
      last_point = self.points[len(points) - 1]
      
      if first_point != last_point:
          new_last_point = CoordinatePair(first_point)
          self.points.append(new_last_point)
      

   @property
   def _subcommands(self):
      first_point = self.points[0]
      result = _HPGLCompoundShape._subcommands.fget(self)
      result.append( PU( ) )
      
      result.append( PA(self.xy + first_point) )
      result.append( PD() )
      for point in self.points:
          result.append( PA(self.xy + point) )
      result.append( PU() )
      return result

