from chiplotle.shapes.shape import _Shape
from chiplotle.shapes.point import Point
from chiplotle.hpgl.coordinate import Coordinate
from chiplotle.hpgl.coordinatearray import CoordinateArray


class PointCloud(_Shape):
   '''
      A cloud of points.
   '''

   def __init__(self, cloud_points):  
      self.cloud_points = cloud_points
      
      _Shape.__init__(self)

   
   @property
   def points(self):
      
      coord_array_array = []

      for point in self.cloud_points:
         p = Point(point)
         coord_array_array.append(p.points[0])

      return coord_array_array


## RUN DEMO CODE
if __name__ == '__main__':
   from chiplotle.shapes.point import Point
   from chiplotle.shapes.group import Group
   from chiplotle.tools import io
   import random
   import math
   
   g1 = Group()
   
   print '\n1000 x Point((0,0))'

   cloud_points = []
   for i in range(0,1000):
      p = [random.randrange(0,100), random.randrange(0, 100)]
      cloud_points.append(p)
      #print "point: %s" % p

   point_cloud = PointCloud(cloud_points)

   io.view(point_cloud)
   
   