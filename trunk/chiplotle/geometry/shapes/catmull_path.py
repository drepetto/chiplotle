from chiplotle.geometry.core.path import Path
from chiplotle.tools.mathtools.catmull_interpolation \
   import catmull_interpolation


def catmull_path(points, interpolation_count=50):
   '''Path with Catmull-Rom spline interpolation.'''

   path_points = catmull_interpolation(points, interpolation_count)
   return Path(path_points)



## DEMO
if __name__ == '__main__':
   from chiplotle.tools import io
   from chiplotle.geometry.shapes.cross import cross
   from chiplotle.geometry.core.group import Group
   from chiplotle.geometry.transforms.offset import offset
   import random

   points = [ ]
   for i in range(10):
      x, y = random.randint(-100, 100), random.randint(-100, 100)
      points.append((x, y))

   crosses = [ ]
   for point in points:
      c = cross(15, 15)
      offset(c, point)
      crosses.append(c)

   path = catmull_path(points)
   
   g = Group([path] + crosses)
   io.view(g)

