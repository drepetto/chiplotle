from chiplotle.geometry.core.group import Group
from chiplotle.geometry.shapes.circle import circle

def target(outer_radius, inner_radius, circles_count, segments=36):
   '''
   Creates `circles_count` concentric circles.
   Can be used to create radially filled circles.
   '''
   
   if not outer_radius > inner_radius:
      raise ValueError('outer_radius must be > inner_radius.')
   if not circles_count > 1:
      raise ValueError('circles_count must be >= 2.')

   result = [ ]
   radius_delta = (outer_radius - inner_radius) / float(circles_count)
   for i in range(circles_count):
      result.append(circle(inner_radius + radius_delta * i, segments))
     
   return Group(result)
   


if __name__ == '__main__':
   from chiplotle import *

   t = target(1000, 50, 5)
   io.view(t)
