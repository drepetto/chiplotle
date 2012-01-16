from chiplotle.tools.mathtools.difference import difference
from chiplotle.geometry.core.path import Path
import math

def perpendicular_displace(path, displacements):
   '''Displaces a path along its perpendiculars.
   
   - `path` is a Path instance.
   - `displacement` is a list of displacement values (scalars). 

   Precondition: len(path) == len(displacement)
   ''' 
   if not isinstance(path, Path):
      raise TypeError('`path` should be of type Path.')
   if len(path.points) != len(displacements):
      raise ValueError('len(path) != len(displacements).')

   ## TODO may want to check here for identical consecutive coords
   ## to avoid 0 differences.
   result = [ ]
   d_points = difference(path.points)
   d_points.append(d_points[-1])
   for i in range(len(path.points)):
      perp = d_points[i].perpendicular.normalized
      disp = perp * displacements[i]
#      perp = d_points[i].perpendicular
#      mag = perp.magnitude
#      if mag == 0: ## two points are overlapping.
#         disp = 0
#      else:
#         disp = perp / mag * displacements[i]

      result.append(path.points[i] + disp)
   path.points = Path(result).points


## ~~~~~~~~~~~~~~~ demo ~~~~~~~~~~~
if __name__ == '__main__':
   from chiplotle import *
   from chiplotle.hpgl.formatters.pen import Pen
   import copy
   from random import randint
   import math

   rndpath = [(randint(0, 2000), randint(0, 2000)) for i in range(2 * 4)]
   p = bezier_path(rndpath, .1, 80)
   print '*** ', p
   pc = copy.deepcopy(p)
   Pen(2)(pc)

   d = [math.sin(x / math.pi) * 30 for x in range(len(p.points))]

   perpendicular_displace(p, d)
   io.view(group([p, pc]))
