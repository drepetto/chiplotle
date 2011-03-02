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
      raise ValueError('len(path) == len(displacements) must be true.')

   result = [ ]
   d_points = difference(path.points)
   for i in range(len(path.points) - 1):
      perp = ~d_points[i]
      mag = perp.magnitude
      if mag == 0: ## two points are overlapping.
         disp = 0
      else:
         disp = perp / mag * displacements[i]

      result.append(path.points[i] + disp)
   path.points = Path(result).points


## demo
if __name__ == '__main__':
   from chiplotle import *
   import copy
   import random

   rndpath = [random.randint(0, 2000) for i in range(10)]
   p = bezier_path(rndpath, .1, 80)
   pc = copy.deepcopy(p)
   PenDecorator(Pen(2))(pc)

   d = [math.sin(x / 3.14159) * 30 for x in range(len(p.points))]

   perpendicular_displace(p, d)
   io.view(group([p, pc]))
