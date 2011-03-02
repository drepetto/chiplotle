from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.geometry.core.path import Path
from chiplotle.tools.mathtools import superformula
import math

def supershape(width, height, m, n1, n2, n3, 
   point_count=100, percentage=1.0, a=1.0, b=1.0, travel=None):
   '''Supershape, generated using the superformula first proposed 
   by Johan Gielis.

   - `points_count` is the total number of points to compute.
   - `travel` is the length of the outline drawn in radians. 
      3.1416 * 2 is a complete cycle.
   '''
   travel = travel or (math.pi * 2)

   ## compute points...
   phis = [i * travel / point_count 
      for i in range(int(point_count * percentage))]
   points = [superformula(a, b, m, n1, n2, n3, x) for x in phis]

   ## scale and transpose...
   path = [ ]
   for x, y in points:
      x *= width
      y *= height
      path.append(Coordinate(x, y))

   return Path(path)


## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.tools import io
   from chiplotle.geometry.core.path import Path
   e = supershape(100, 120, 5, 3.3, 2, 3, b=0.75, travel = 4*math.pi)
   io.view(e)
