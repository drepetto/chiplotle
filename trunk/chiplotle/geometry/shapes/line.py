from chiplotle.geometry.shapes.shape import _Shape
from chiplotle.geometry.coordinate import Coordinate
from chiplotle.geometry.coordinatearray import CoordinateArray

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
   from chiplotle.geometry.shapes.line import Line
   from chiplotle.geometry.shapes.group import Group
   from chiplotle.tools import io
   import math
   
   l1 = Line((0,0), (1000,1000))
   print '\nLine((0,0), (1000,1000))'
   print l1.format

   ## displaced
   l2 = Line((0,0), (1000,1000))
   l2.offset = (200,100)
   print '\nLine((0,0), (1000,1000))\noffset = (200,100)'
   print l2.format

   ## displaced and rotated around (0, 0)
   l3 = Line((0,0), (1000,1000))
   l3.offset = (100, 100)
   l3.rotation = math.pi / 3.0
   print '\nLine((0,0), (1000,1000))\noffset = (100, 100)\nrotation = math.pi / 3'
   print l3.format

   ## displaced and rotated around (100, 100)
   l4 = Line((0,0), (1000,1000))
   l4.offset = (100, 100)
   l4.rotation = math.pi / 3.0
   l4.pivot = (100, 100)
   print '\nLine((0,0), (1000,1000))\noffset = (100, 100)\nrotation = math.pi / 3\npivot = (100, 100)'
   print l4.format

   g1 = Group([l1, l2, l3, l4])
   io.view(g1)
   
   