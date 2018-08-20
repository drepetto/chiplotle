from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from builtins import range
from future import standard_library
standard_library.install_aliases()
from chiplotle.geometry.core.polygon import Polygon
from chiplotle.geometry.transforms.scale import scale
import math

def circle(radius, segments = 36):
   '''Returns a circle.'''
   coords = [(math.cos(math.pi * 2 / segments * r) * radius,
              math.sin(math.pi * 2 / segments * r) * radius)
              for r in range(segments)]
   return Polygon(coords)


## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.tools import io
   e = circle(1000)
   io.view(e)
