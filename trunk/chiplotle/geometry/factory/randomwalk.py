from chiplotle.geometry.shapes.path import Path
from chiplotle.tools.mathtools import polar_to_xy
import math
import random


def random_walk_polar(steps, step_size=500):
   '''Random Walk. Border is a circle'''

   the_points = []
   two_pi = math.pi * 2

   for i in range(steps):
      A = random.random() * two_pi
      r = step_size
      xy = polar_to_xy((r,A))
      the_points.append(xy)
   
   return Path(the_points)


def random_walk_cartesian(steps, step_size=500):
   '''Random Walk. Border is a square.'''

   the_points = []
   half_step = step_size/2
   
   previous = (0,0)
   
   for i in range(steps):
      x = previous[0] + random.randrange(-half_step, half_step)
      y = previous[1] + random.randrange(-half_step, half_step)      
      the_points.append((x, y))
   
   return Path(the_points)



## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.tools import io
   rw = random_walk_polar(1000)
   assert isinstance(rw, Path)
   print rw.format
   io.view(rw)

   rw = random_walk_cartesian(1000)
   assert isinstance(rw, Path)
   print rw.format
   io.view(rw)