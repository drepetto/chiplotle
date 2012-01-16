from chiplotle.geometry.core.group import Group
from chiplotle.geometry.core.path import Path
from chiplotle.geometry.core.coordinatearray import CoordinateArray
from chiplotle.tools.mathtools.difference import difference
from chiplotle.geometry.transforms.transformvisitor import TransformVisitor
import random

def perpendicular_noise(shape, value):
   '''Distort shape by adding noise perpendiculary to the path.
   This is an in-place destructive transformation; no new shapes are created.

   - `shape` is the shape to be noisified.
   - `value` must be a scalar defining the range of the noise 
      for displacement.
   '''
   def perpnoise(coords, value):
      result = [ ]
      d_coords = difference(coords)
      for coord, d_coord in zip(coords[:-1], d_coords):
         wiggle = random.randrange(-value, value)
         perp = ~d_coord 
         xy = coord + perp / perp.magnitude * wiggle         
         result.append(xy)
      return CoordinateArray(result)

   t = TransformVisitor(perpnoise)
   t.visit(shape, value)

      
      
   
## RUN DEMO CODE
if __name__ == "__main__":
   from chiplotle.geometry.shapes.circle import circle
   from chiplotle.geometry.core.coordinate import Coordinate
   from chiplotle.tools import io
   c1 = circle(1000, 200)
   c2 = circle(800, 200)
   c2 += Coordinate(2000, 2000)
   perpendicular_noise(c1, 360)
   perpendicular_noise(c2, 60)
   g = Group([c1, c2])
   io.view(g)

