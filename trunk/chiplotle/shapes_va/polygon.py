from chiplotle.shapes_va.shape import _Shape
from chiplotle.hpgl.coordinatearray import CoordinateArray
from chiplotle.hpgl.coordinatepair import CoordinatePair
from chiplotle.hpgl.commands import PU, PD, PA

class Polygon(_Shape):
   '''
      A polygon, i.e. a series of points that will be connected by
      straight lines. 
      
      offset is a CoordinatePair for moving the shape around in 2D space
      rotation is an angle expressed in radians
      pivot is a CoordinatePair indicating the point around which to rotate
      
      If first_point != last_point then one final point 
      (a duplicate of the first point) will be added to close the polygon.   
   '''

   def __init__(self, points, offset=(0, 0), rotation=0, pivot=(0, 0)):
      ## TODO: find better name instead of coords?
      self.coords = CoordinateArray(points)
      if points[0] != points[-1]:
          self.coords.append(CoordinatePair(points[0]))
      
      _Shape.__init__(self, offset, rotation, pivot)

      
   @property
   def points(self):
      return [self.coords]


## RUN CODE
if __name__ == '__main__':
   from chiplotle.shapes_va.polygon import Polygon
   from chiplotle.tools import io
   import math
   ## Polygon
   p = Polygon([(0, 0), (100, 100), (0, 100)])
   print '\nPolygon([(0, 0), (100, 100), (0, 100)])'
   print p.format

   ## Polygon with offset
   p = Polygon([(0, 0), (100, 100), (0, 100)], (100, 100))
   print '\nPolygon([(0, 0), (100, 100), (0, 100)], (100, 100))'
   print p.format

   ## Polygon with offset and rotation around (0, 0)
   p = Polygon([(0, 0), (100, 100), (0, 100)], (100, 100), math.pi / 3)
   print '\nPolygon([(0, 0), (100, 100), (0, 100)], (100, 100), math.pi / 3)'
   print p.format

   ## Polygon with offset and rotation around (100, 100)
   p = Polygon([(0, 0), (100, 100), (0, 100)], (100, 100), math.pi / 3, (100, 100))
   print '\nPolygon([(0, 0), (100, 100), (0, 100)], (100, 100), math.pi / 3, (100, 100))'
   print p.format
