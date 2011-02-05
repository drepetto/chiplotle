from chiplotle.geometry.factory.isosceles import isosceles
from chiplotle.geometry.transforms.offset import offset
from chiplotle.geometry.transforms.rotate import rotate
from chiplotle.geometry.shapes.group import Group
from chiplotle.tools.mathtools.xy_to_polar import xy_to_polar
import math

def arrow(path, headwidth, headheight):
   '''Returns an arrow shape.

   - `path` is a Path object.
   - `headwidth` is the width of the arrow head.
   - `headheight` is the height of the arrow head.
   '''

   rot, a = xy_to_polar((path[-1] - path[-2]))
   head = isosceles(headwidth, headheight)
   rotate(head, rot + math.pi, (0, 0))
   offset(head, path[-1])

   return Group([head, path])



## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.tools import io
   from chiplotle.geometry.factory.bezier_path import bezier_path
   path = bezier_path([(0, 0), (100, 100), (0, 200), (100, -200)], 1)
   e = arrow(path, 10, 20)
   io.view(e)
