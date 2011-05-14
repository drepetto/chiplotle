from chiplotle.geometry.core.polygon import Polygon
from chiplotle.geometry.core.group import Group
from chiplotle.tools.mathtools.lcm import lcm
import math
from fractions import gcd
      
def star_outline(width, height, num_points = 5):  
   '''Constructs a star shape in outline.  '''
   corners = []
   pi_div_180 = math.pi / 180.0
   half_width = width * 0.5
   half_height = height * 0.5

   degrees = degrees_offset = 90
   even = True
   
   degrees_incr = 360.0 / float(num_points * 2)
   quarter_width = half_width * 0.5
   quarter_height = half_height * 0.5
   
   while degrees < 360.0 + degrees_offset: 
      alpha = degrees * pi_div_180
      sin_alpha = math.sin(alpha);
      cos_alpha = math.cos(alpha);

      if even:
         w_multi = half_width
         h_multi = half_height
         even = False
      else:
         w_multi = quarter_width
         h_multi = quarter_height
         even = True
         
      point_x = (w_multi * cos_alpha);
      point_y = (h_multi * sin_alpha);

      corners.append((point_x, point_y))
      
      degrees += degrees_incr

   corners.append(corners[0])
   return Polygon(corners)
   


## RUN DEMO CODE
if __name__ == '__main__':
   from chiplotle.tools import io
   from chiplotle.geometry.shapes.star_outline import star_outline
   from chiplotle.geometry.core.group import Group
   
   gr1 = Group()
   
   for i in range(5, 10):
      st = star_outline(100 * (i * i * i), 100 * (i * i * i), num_points = i)
      gr1.append(st)
   
   io.view(gr1)
