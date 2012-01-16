from chiplotle.geometry.shapes.isosceles import isosceles
from chiplotle.geometry.transforms.offset import offset
from chiplotle.geometry.transforms.rotate import rotate
from chiplotle.geometry.core.group import Group
from chiplotle.tools.mathtools.xy_to_polar import xy_to_polar
import math

def arrow(path, headwidth, headheight, filled=False):
   '''Returns an arrow shape.

   - `path` is a Path object.
   - `headwidth` is the width of the arrow head.
   - `headheight` is the height of the arrow head.
   '''

   ## make arow head...
   r, a = xy_to_polar((path.points[-1] - path.points[-2]))
   head = isosceles(headwidth, headheight, filled)
   offset(head, (0, -headheight))
   rotate(head, a - math.pi / 2, (0, 0))
   offset(head, path.points[-1])

   return Group([head, path])



## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle import *

   coords = [(0, 0), (0, 1000), (2000, 1000)]
   p = shapes.bezier_path(coords, 1)
   a = arrow(p, 100, 200)
   io.view(a, 'png')
