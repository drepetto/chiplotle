from chiplotle.geometry.shapes.group import Group
from chiplotle.geometry.shapes.path import Path
from chiplotle.tools.mathtools.difference import difference
import random

def perpendicular_noise(shape, value):
   '''Distort shape by adding noise perpendiculary to the path.
   This is an in-place destructive transformation; no new shapes are created.

   - `shape` is the shape to be noisified.
   - `value` must be a scalar defining the range of the noise 
      for displacement.
   '''
   if isinstance(shape, Group):
      for i in range(len(shape)):
         shape[i] = perpendicular_noise(shape[i], value)
   else:
      result = [ ]
      points = shape.points
      d_points = difference(points)
      for point, d_point in zip(points[:-1], d_points):
         wiggle = random.randrange(-value, value)
         perp = ~d_point 
         xy = point + perp / perp.magnitude * wiggle         
         result.append(xy)
      shape.points = result

   #return shape
      
      
   
## RUN DEMO CODE
if __name__ == "__main__":
   from chiplotle.geometry.factory.circle import circle
   from chiplotle.tools import io
   c1 = circle(100, 200)
   c2 = circle(80, 200)
   c2 += 200
   perpendicular_noise(c1, 36)
   perpendicular_noise(c2, 6)
   g = Group([c1, c2])
   io.view(g)

