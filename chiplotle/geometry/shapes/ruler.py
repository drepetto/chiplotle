from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.geometry.core.group import Group
from chiplotle.geometry.shapes.line import line
from chiplotle.geometry.transforms.rotate import rotate
from chiplotle.geometry.transforms.offset import offset
import math

def ruler(start_coord, end_coord, units, min_tick_height, symmetric=False):
   '''
   A measuring ruler.
   
   - `units` is a list of units on which to put marks, from smaller
      to larger. e.g., (10, 20, 40).
   - `min_tick_height` is the height of the marks for the smallest units.
      The hight of the other units are multiples of this.
   - `symmetric` set to True to draw the tick lines symmetrically around 
      the invisible center-line.
   '''
   start_coord = Coordinate(*start_coord)
   end_coord = Coordinate(*end_coord)

   length = (end_coord - start_coord).magnitude
   angle = (end_coord - start_coord).angle

   result = [ ]
   for i, unit in enumerate(units):
      ticks = int(math.ceil(length / unit))
      for t in range(ticks):
         tick_height = min_tick_height * (i + 1)
         if symmetric:
            x1, y1 = unit * t, tick_height / 2
            x2, y2 = unit * t, -tick_height / 2
         else:
            x1, y1 = unit * t, 0
            x2, y2 = unit * t, -tick_height
         tick = line((x1, y1), (x2, y2))
         result.append(tick)
   g = Group(result)
   rotate(g, angle, (0, 0))
   offset(g, start_coord)
   return g


if __name__ == '__main__':
   from chiplotle import * 
      
   r = ruler((0, 0), (1000, 1000), (100, 200, 400), 10)
   c = circle(30)
   g = Group([r, c])
   io.view(g)
