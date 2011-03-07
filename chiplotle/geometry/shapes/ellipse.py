from chiplotle.geometry.core.path import Path
import math

def ellipse(width, height, segments = 36):  
   '''
   Constructs an ellipse with the given width, height, and number of segments.
   '''

   two_pi = math.pi * 2.0
   
   rads_incr = two_pi / float(segments)
   half_width = width * 0.5
   half_height = height * 0.5
   
   rads = 0.0
   
   ellipse_points = []
   
   while rads < two_pi: 
      sin = math.sin(rads);
      cos = math.cos(rads);

      point_x = (half_width * cos);
      point_y = (half_height * sin);

      ellipse_points.append((point_x, point_y))
      
      rads += rads_incr
 
   result = Path(ellipse_points)
   result.closed = True
   return result


## RUN DEMO CODE

if __name__ == '__main__':

   from chiplotle import *
   from chiplotle.geometry import *

   import math

   two_pi = math.pi * 2.0

   g = []

   for a in range(0,7):
      e = ellipse(5000, 1000, 500)
      assert isinstance(e, Path)
      rotate(e, (two_pi / 7) * a)
      g.append(e)
   
   io.view(Group(g))
