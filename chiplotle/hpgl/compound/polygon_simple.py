from chiplotle.hpgl.compound.hpglcompoundshape import _HPGLCompoundShape
from chiplotle.hpgl.commands import PU, PD, PA

class PolygonSimple(_HPGLCompoundShape):
   '''A simple polygon, e.g. one that is simply a closed path.
      points is an [] of CoordinatePairs.
      One final point (a duplicate of the first point) will be added to close the polygon.   
   '''

   _scalable = _HPGLCompoundShape._scalable + ['width', 'height']

   def __init__(self, xy, points):
      _HPGLCompoundShape.__init__(self, xy)           
      self.points = points

   @property
   def _subcommands(self):
      first_point = self.points[0]
      result = _HPGLCompoundShape._subcommands.fget(self)
      result.append( PU( ) )
      
      result.append( PA((self.x + first_point.x, self.y + first_point.y)) )
      result.append( PD() )
      for point in self.points:
          result.append( PA((self.x + point.x, self.y + point.y)) )
      #add final point to close the polygon
      result.append( PA((self.x + first_point.x, self.y + first_point.y)) )
      result.append( PU() )
      return result

