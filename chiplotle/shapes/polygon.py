from chiplotle.shapes.shape import _Shape
from chiplotle.hpgl.coordinatearray import CoordinateArray
from chiplotle.hpgl.coordinate import Coordinate

class Polygon(_Shape):
   '''
      A polygon, i.e. a series of points that will be connected by
      straight lines. 
      
      If first_point != last_point then one final point 
      (a duplicate of the first point) will be added to close the polygon.   
   '''

   def __init__(self, points):
      ## TODO: find better name instead of coords?
      self.coords = CoordinateArray(points)
      if points[0] != points[-1]:
          self.coords.append(Coordinate(points[0]))
      
      _Shape.__init__(self)

      
   @property
   def points(self):
      return [self.coords]


## RUN CODE
if __name__ == '__main__':
   from chiplotle.shapes.polygon import Polygon
   from chiplotle.shapes.group import Group
   from chiplotle.tools import io
   import math
   ## Polygon
   p1 = Polygon([(0, 0), (100, 100), (0, 100)])
   print '\nPolygon([(0, 0), (100, 100), (0, 100)])'
   print p1.format

   ## Polygon with offset
   p2 = Polygon([(0, 0), (100, 100), (0, 100)])
   p2.offset = (100, 100)
   print '\nPolygon([(0, 0), (100, 100), (0, 100)]\noffset = (100, 100)'
   print p2.format

   ## Polygon with offset and rotation around (0, 0)
   p3 = Polygon([(0, 0), (100, 100), (0, 100)])
   p3.offset = (100, 100)
   p3.rotation = math.pi / 3.0
   print '\nPolygon([(0, 0), (100, 100), (0, 100)])\noffset = (100, 100)\nrotation = math.pi / 3.0'
   print p3.format

   ## Polygon with offset and rotation around (100, 100)
   p4 = Polygon([(0, 0), (100, 100), (0, 100)])
   p4.offset = (100, 100)
   p4.rotation = math.pi / 3.0
   p4.pivot = (100, 100)
   print '\nPolygon([(0, 0), (100, 100), (0, 100)])\noffset = (100, 100)\nrotation = math.pi / 3.0\npivot = (100, 100))'
   print p4.format


   g1 = Group([p1,p2,p3,p4])
   io.view(g1)
   