from chiplotle.shapes.shape import _Shape
from chiplotle.hpgl.coordinate import Coordinate
from chiplotle.hpgl.coordinatearray import CoordinateArray

class Point(_Shape):
   '''
      A single point.
   '''

   def __init__(self, point):  
      self.point = point
      
      _Shape.__init__(self)

   
   @property
   def points(self):
      point1 = self.point
      
      # not sure if we need this, but without it nothing shows up
      # when you do io.view(point)!
      point2 = self.point + Coordinate(1,1)
      return [CoordinateArray([point1, point2])]




## RUN DEMO CODE
if __name__ == '__main__':
   from chiplotle.shapes.point import Point
   from chiplotle.shapes.group import Group
   from chiplotle.tools import io
   import random
   import math
   
   g1 = Group()
   
   print '\n1000 x Point((0,0)'

   for i in range(0,1000):
      p1 = Point((0,0))
      p1.offset = random.randrange(0,1000)
      p1.rotation = random.random() * (math.pi * 2)
      p1.pivot = random.randrange(0, 1000)
      print "offset: %s rotation: %f pivot: %s" % (p1.offset, p1.rotation, p1.pivot)
      g1.append(p1)

   io.view(g1)
   
   