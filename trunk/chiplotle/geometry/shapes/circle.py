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
