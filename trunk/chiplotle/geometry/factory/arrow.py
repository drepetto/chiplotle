from chiplotle.geometry.vectorarray import VectorArray
from chiplotle.geometry.factory.isosceles import isosceles
from chiplotle.geometry.shapes.group import Group
from chiplotle.tools.mathtools.xy_to_polar import xy_to_polar
import math

def arrow(path, headwidth, headheight):
   ## make arrow head...
   rot, a = xy_to_polar((path[-1] - path[-2]))
   head = isosceles(headwidth, headheight)
   ## TODO: replace this position/orientation attribute mechanism with
   ## explicit operation via +/- and rotation operators?
   head.rotation = rot + math.pi
   head.offset = path[-1]
   head.pivot = path[-1]

   return Group([head, path])



## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.tools import io
   from chiplotle.geometry.factory.bezier_path import bezier_path
   path = bezier_path([(0, 0), (100, 100), (0, 200), (100, -200)], 1)
   e = arrow(path, 10, 20)
   io.view(e)
