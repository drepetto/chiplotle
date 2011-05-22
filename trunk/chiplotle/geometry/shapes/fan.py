from chiplotle.geometry.core.polygon import Polygon
from chiplotle.geometry.shapes.arc_circle import arc_circle
import math

def fan(radius, start_angle, end_angle, height, segments=100, filled=False):
   '''A Fan is a slice of a donut seen from above 
   (when you can see the hole in the middle).
   
   All angles are assumed to be in radians.'''
   if start_angle > end_angle:
      end_angle += math.pi * 2

   arc1 = arc_circle(radius - height / 2, start_angle, end_angle, segments)
   arc2 = arc_circle(radius + height / 2, start_angle, end_angle, segments)
   points = list(arc1.points) + list(reversed(arc2.points))
   return Polygon(points)

   
## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.tools import io
   import math

   f = fan(1000, math.pi / 4, math.pi / 4 * 3, 500, 30)
   io.view(f)
