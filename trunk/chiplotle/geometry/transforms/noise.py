from chiplotle.geometry.core.group import Group
from chiplotle.geometry.core.path import Path
from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.geometry.core.coordinatearray import CoordinateArray
from chiplotle.geometry.transforms.transformvisitor import TransformVisitor
import random

def noise(shape, value):
   '''Distort shape by adding noise.

   - `value` can be a scalar or a tuple (x, y) that sets the range of the 
      noise for the x and y coordinates.
   '''
   def noisify(coords, value):
      try:
         x, y = value
      except TypeError:
         x = y = value
      result = [ ]
      for point in coords:
         x_wiggle = random.randrange(-x, x)
         y_wiggle = random.randrange(-y, y)
         xy = point + Coordinate(x_wiggle, y_wiggle)         
         result.append(xy)
      return CoordinateArray(result)

   t = TransformVisitor(noisify)
   t.visit(shape, value)
      
      
   
## RUN DEMO CODE
if __name__ == "__main__":
   from chiplotle.geometry.shapes.circle import circle
   from chiplotle.tools import io
   c1 = circle(1000, 100)
   c2 = circle(800, 100)
   noise(c1, 90)
   c1 += Coordinate(1000, 1000)
   g = Group([c1, c2])
   noise(g, 60)
   io.view(g)
