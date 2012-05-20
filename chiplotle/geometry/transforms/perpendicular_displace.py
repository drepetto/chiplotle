from chiplotle.tools.geometrytools.split_coordinatearray_proportionally \
   import split_coordinatearray_proportionally
from chiplotle.geometry.core.path import Path

def perpendicular_displace(path, displacements):
   '''Displaces a path along its perpendiculars.
   
   - `path` is a Path instance.
   - `displacement` is a list of displacement values (scalars). 
   ''' 
   if not isinstance(path, Path):
      raise TypeError('`path` should be of type Path.')

   ## TODO may want to check here for identical consecutive coords
   ## to avoid 0 differences.
   count    = len(displacements)
   points   = split_coordinatearray_proportionally(path.points, count)
   d_points = points.difference

   result  = []
   for i in range(len(d_points)):
      norm = d_points[i].perpendicular.normalized
      disp = norm * displacements[i]
      result.append(points[i] + disp)

   path.points = Path(result).points
#   result = [ ]
#   d_points = path.points.difference
#   d_points.append(d_points[-1])
#   for i in range(len(path.points)):
#      perp = d_points[i].perpendicular.normalized
#      disp = perp * displacements[i]
#      result.append(path.points[i] + disp)
#   path.points = Path(result).points


## ~~~~~~~~~~~~~~~ demo ~~~~~~~~~~~
if __name__ == '__main__':
   from chiplotle import *
   from chiplotle.hpgl.formatters.pen import Pen
   import copy
   from random import randint
   import math

   struct = shapes.circle(1000, randint(5, 12))
   disp   = copy.deepcopy(struct)
   Pen(2)(struct)
   Pen(1)(disp)

   d = [math.sin(x / math.pi / 4) * 300 for x in range(400)]

   perpendicular_displace(struct, d)
   io.view(group([struct, disp]))
