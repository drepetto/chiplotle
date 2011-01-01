from chiplotle.geometry.shapes.shape import _Shape
from chiplotle.geometry.shapes.ellipse import Ellipse
from chiplotle.geometry.coordinate import Coordinate
from chiplotle.geometry.coordinatearray import CoordinateArray
import math

class Donut(_Shape):
   '''
      A donut (ellipse within ellipse) with a width, height, inset, segments.
      
      segments is how many lines should be used to draw ellipse. More
      segments create a smoother ellipse, but will take longer to draw.
      
      inset is the distance to inset the inner ellipse from the outer.
      
      The Donut is drawn with the current pen location as the center.
      offset may be used to shift this around, for example, to draw from
      the lower, left corner.
   '''

   def __init__(self, width, height, inset, segments = 100):  
      self.width = width
      self.height = height
      self.segments = segments
      self.inset = inset

      _Shape.__init__(self)
      

   @property
   def points(self):
      
      e1 = Ellipse(self.width, self.height, self.segments)
      e1.offset = self.offset
      e1.rotation = self.rotation
      e1.pivot = self.pivot
      
      e1_points = e1.points[0]
      
      e2 = Ellipse(self.width - (self.inset * 2), self.height - (self.inset * 2), self.segments)
      e2.offset = self.offset
      e2.rotation = self.rotation
      e2.pivot = self.pivot
      
      e2_points = e2.points[0]
      
      return [CoordinateArray(e1_points), CoordinateArray(e2_points)]

## RUN DEMO CODE
if __name__ == '__main__':
   from chiplotle.geometry.shapes.donut import Donut
   from chiplotle.geometry.shapes.group import Group
   from chiplotle.tools import io
   import math
   d1 = Donut(1000, 500, inset = 20)
   print '\Donut(1000, 500, inset = 20)'
   print d1.format

   ## displaced
   d2 = Donut(1000, 500, inset = 20)
   d2.offset = (100, 100)
   print '\Donut(1000, 500, inset = 20)\noffset = (100, 100)'
   print d2.format

   ## displaced and rotated around (0, 0)
   d3 = Donut(1000, 500, inset = 20)
   d3.offset = (100, 100)
   d3.rotation = math.pi / 3.0
   print '\Donut(1000, 500, inset = 20)\noffset = (100, 100)\nrotation = math.pi / 3.0'
   print d3.format

   ## displaced and rotated around (100, 100)
   d4 = Donut(1000, 500, inset = 20)
   d4.offset = (100, 100)
   d4.rotation = math.pi / 3.0
   d4.pivot = (100, 100)
   print '\Donut(1000, 500, inset = 20)\noffset = (100, 100)\nrotation = math.pi / 3.0\npivot = (100, 100)'
   print d4.format

   g1 = Group([d1, d2, d3, d4])
   io.view(g1)
   
   