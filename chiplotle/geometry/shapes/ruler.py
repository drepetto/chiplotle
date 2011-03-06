from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.geometry.core.group import Group
from chiplotle.geometry.shapes.line import line
import math

def ruler(length, units, min_tick_height):
   '''
   A measuring ruler.
   
   - `units` is a list of units on which to put marks, from smaller
      to larger. e.g., (10, 20, 40).
   - `min_tick_height` is the height of the marks for the smallest units.
      The hight of the other units are multiples of this.
   '''
   result = [ ]
   for i, unit in enumerate(units):
      ticks = int(math.ceil(length / unit))
      for t in range(ticks):
         x1, y1 = unit * t, 0
         x2, y2 = unit * t, -min_tick_height * (i + 1)
         tick = line((x1, y1), (x2, y2))
         result.append(tick)
   return Group(result)


if __name__ == '__main__':
   from chiplotle import * 
      
   r = ruler(2000, (100, 200, 400), 10)
   rotate(r, 3.145 / 8, (0, 0))
   c = circle(30)
   g = Group([r, c])
   io.view(g)
