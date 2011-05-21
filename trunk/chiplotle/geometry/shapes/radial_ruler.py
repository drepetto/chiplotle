from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.tools.mathtools.polar_to_xy import polar_to_xy as p2c
from chiplotle.geometry.shapes.line import line
from chiplotle.geometry.core.group import Group
import math

def radial_ruler(radius, 
                 start_angle, 
                 end_angle, 
                 units, 
                 min_tick_height, 
                 symmetric=True):

   length = end_angle - start_angle

   result = []
   for i, unit in enumerate(units):
      ticks = int(math.ceil(length / unit))
      for t in range(ticks):
         tick_height = min_tick_height * (i + 1)
         if symmetric:
            r1, a1 =  tick_height / 2, unit * t + start_angle
            r2, a2 = -tick_height / 2, unit * t + start_angle
         else:
            r1, a1 = 0, unit * t + start_angle
            r2, a2 = -tick_height, unit * t + start_angle
         xy1 = p2c(Coordinate(r1, a1) + Coordinate(radius, 0)) 
         xy2 = p2c(Coordinate(r2, a2) + Coordinate(radius, 0)) 
         tick = line(xy1, xy2)
         result.append(tick)
   return Group(result)


if __name__ == '__main__':
   from chiplotle import * 
   import math
      
   r1 = radial_ruler(1000, 0.1, math.pi, (math.pi/20, math.pi/10), 20, True)
   r2 = radial_ruler(500, math.pi/3, math.pi, (math.pi/40, math.pi/10), 20, False)
   c = circle(30)
   g = Group([r1, r2, c])
   io.view(g)
