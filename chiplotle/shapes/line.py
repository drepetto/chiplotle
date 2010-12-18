from chiplotle.shapes.shape import _Shape
from chiplotle.hpgl.coordinate import Coordinate
from chiplotle.hpgl.coordinatearray import CoordinateArray

class Line(_Shape):
   '''
      A line with start_point and end_point.
   '''

   def __init__(self, start_point, end_point):  
      self.start_point = start_point
      self.end_point = end_point
      
      _Shape.__init__(self)

   
   @property
   def points(self):
      the_points = [self.start_point, self.end_point]

      return [CoordinateArray(the_points)]




## RUN DEMO CODE
if __name__ == '__main__':
   from chiplotle.shapes.line import Line
   from chiplotle.shapes.group import Group
   from chiplotle.tools import io
   import math
   
   p1 = Line((0,0), (1000,1000))
   print '\nLine((0,0), (1000,1000))'
   print p1.format

   ## displaced
   p2 = Line((0,0), (1000,1000))
   p2.offset = (200,100)
   print '\nLine((0,0), (1000,1000))\noffset = (200,100)'
   print p2.format

   ## displaced and rotated around (0, 0)
   p3 = Line((0,0), (1000,1000))
   p3.offset = (100, 100)
   p3.rotation = math.pi / 3.0
   print '\nLine((0,0), (1000,1000))\noffset = (100, 100)\nrotation = math.pi / 3'
   print p3.format

   ## displaced and rotated around (100, 100)
   p4 = Line((0,0), (1000,1000))
   p4.offset = (100, 100)
   p4.rotation = math.pi / 3.0
   p4.pivot = (100, 100)
   print '\nLine((0,0), (1000,1000))\noffset = (100, 100)\nrotation = math.pi / 3\npivot = (100, 100)'
   print p4.format

   g1 = Group([p1, p2, p3, p4])
   io.view(g1)
   
   