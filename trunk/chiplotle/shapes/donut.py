from chiplotle.shapes.shape import _Shape
from chiplotle.shapes.ellipse import Ellipse
from chiplotle.hpgl.coordinatepair import CoordinatePair
from chiplotle.hpgl.coordinatearray import CoordinateArray
#from chiplotle.hpgl.commands import PU, PD, PA
import math

class Donut(_Shape):
   '''
      A donut (ellipse within ellipse) with a width, height, inset, segments,
      offset, rotation, and pivot.
      
      offset is a CoordinatePair for moving the shape around in 2D space
      rotation is an angle expressed in radians
      pivot is a CoordinatePair indicating the point around which to rotate
      
      segments is how many lines should be used to draw ellipse. More
      segments create a smoother ellipse, but will take longer to draw.
      
      inset is the distance to inset the inner ellipse from the outer.
      
      The Donut is drawn with the current pen location as the center.
      offset may be used to shift this around, for example, to draw from
      the lower, left corner.
   '''

   def __init__(self, width, height, inset, segments = 100, offset=(0, 0), rotation=0, pivot=(0, 0)):  
      self.width = width
      self.height = height
      self.segments = segments
      self.inset = inset

      _Shape.__init__(self, offset, rotation, pivot)
      

   @property
   def points(self):
      
      e1 = Ellipse(self.width, self.height, self.segments, self.offset, self.rotation, self.pivot)
      e1_points = e1.points[0]
      e2 = Ellipse(self.width - (self.inset * 2), self.height - (self.inset * 2), self.segments, self.offset, self.rotation, self.pivot)
      e2_points = e2.points[0]
      
      return [CoordinateArray(e1_points), CoordinateArray(e2_points)]

## RUN DEMO CODE
if __name__ == '__main__':
   from chiplotle.shapes.donut import Donut
   from chiplotle.shapes.group import Group
   from chiplotle.tools import io
   import math
   d1 = Donut(1000, 500, inset = 20)
   print '\Donut(1000, 500, inset = 20)'
   print d1.format

   ## displaced
   d2 = Donut(1000, 500, inset = 20, offset = (100, 100)) 
   print '\Donut(1000, 500, inset = 20, offset = (100, 100)) '
   print d2.format

   ## displaced and rotated around (0, 0)
   d3 = Donut(1000, 500, inset = 20, offset = (100, 100), rotation = math.pi / 3) 
   print '\Donut(1000, 500, inset = 20, offset = (100, 100), rotation = math.pi / 3) '
   print d3.format

   ## displaced and rotated around (100, 100)
   d4 = Donut(1000, 500, inset = 20, offset = (100, 100), rotation = math.pi / 3, pivot = (100, 100)) 
   print '\Donut(1000, 500, inset = 20, offset = (100, 100), rotation = math.pi / 3, pivot = (100, 100))'
   print d4.format

   g1 = Group([d1, d2, d3, d4])
   io.view(g1)
   
   