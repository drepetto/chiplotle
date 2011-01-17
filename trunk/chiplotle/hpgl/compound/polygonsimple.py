from chiplotle.hpgl.compound.hpglcompoundshape import _HPGLCompoundShape
from chiplotle.geometry.vector import Vector
from chiplotle.hpgl.commands import PU, PD, PA

class PolygonSimple(_HPGLCompoundShape):
   '''A simple polygon, e.g. one that is simply a closed path.
      points is an [] of Vectors.
      If first_point != last_point then one final point 
      (a duplicate of the first point) will be added to close the polygon.   
   '''

   _scalable = _HPGLCompoundShape._scalable + ['poly_points']

   def __init__(self, xy, poly_points):
      _HPGLCompoundShape.__init__(self, xy)           
      self.poly_points = poly_points
      
      first_point = self.poly_points[0]
      last_point = self.poly_points[len(self.poly_points) - 1]
      
      if first_point != last_point:
          new_last_point = Vector(first_point)
          self.poly_points.append(new_last_point)
      
   @property
   def points(self):
      return [self.poly_points]

   @property
   def _subcommands(self):
      the_points = self.points[0]
      first_point = the_points[0]
      result = _HPGLCompoundShape._subcommands.fget(self)
      result.append( PU( ) )
      
      result.append( PA(self.xy + first_point) )
      result.append( PD() )
      for point in the_points:
          result.append( PA(self.xy + point) )
      result.append( PU() )
      return result

