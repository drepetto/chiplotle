from chiplotle.geometry.shapes.group import Group
from chiplotle.geometry.shapes.path import Path
from chiplotle.geometry.coordinate import Coordinate
import random

def noise(shape, value):
   '''Distort shape by adding noise.

   - `value` can be a scalar or a tuple (x, y) that sets the range of the 
      noise for the x and y coordinates.
   '''
   if isinstance(shape, Group):
      for i in range(len(shape)):
         shape[i] = noise(shape[i], value)
   else:
      try:
         x, y = value
      except TypeError:
         x = y = value
      result = [ ]
      for point in shape.points:
         x_wiggle = random.randrange(-x, x)
         y_wiggle = random.randrange(-y, y)
         xy = point + Coordinate(x_wiggle, y_wiggle)         
         result.append(xy)
      shape.points = result

   #return shape
      
      
   
## RUN DEMO CODE
if __name__ == "__main__":
   from chiplotle.geometry.factory.circle import circle
   from chiplotle.tools import io
   c1 = circle(100)
   c2 = circle(80)
   cn = noise(c1, 6)
   cn += 100
   g = Group([cn, c2])
   g = noise(g, 6)
   io.view(g)
