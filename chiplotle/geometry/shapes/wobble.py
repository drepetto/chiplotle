from chiplotle.geometry.shapes.shape import _Shape
from chiplotle.geometry.coordinate import Coordinate
from chiplotle.geometry.coordinatearray import CoordinateArray

class Wobble(_Shape):
   '''
      A rectangle with a width and height.

      offset is a Coordinate for moving the shape around in 2D space
      rotation is an angle expressed in radians
      pivot is a Coordinate indicating the point around which to rotate
      
      The Rectangle is drawn with the current pen location as the center.
      offset may be used to shift this around, for example, to draw from
      the lower, left corner.
   '''

   def __init__(self, shape, dynamic = False):
      self.shape = shape
      self.dyname = dynamic
      
      _Shape.__init__(self)

   @property
   def points(self):
      import random
      virgin_points = self.shape.points[0]
      wiggle_points = []
      for p in virgin_points:
         #print p
         x_wiggle = random.randrange(-5,5)
         x = p.x + x_wiggle
         y_wiggle = random.randrange(-5,5)
         y = p.y + y_wiggle         
         xy_new = Coordinate(x, y)
         wiggle_points.append(xy_new)
      
      print [wiggle_points]
      return [CoordinateArray(wiggle_points)]


## RUN DEMO CODE
if __name__ == '__main__':
   from chiplotle.geometry.shapes.group import Group
   from chiplotle.geometry.shapes.wobble import Wobble
   from chiplotle.geometry.shapes.rectangle import Rectangle
   from chiplotle.geometry.shapes.ellipse import Ellipse
   from chiplotle.tools import io
      
   r1 = Rectangle(1000,1000)
   r2 = Wobble(r1)

   e1 = Ellipse(1000,1000)
   e2 = Wobble(e1)
   

   g1 = Group([r1, r2, e1, e2])
   io.view(g1)
   