from chiplotle.geometry.core.polygon import Polygon
from chiplotle.geometry.core.group import Group
from chiplotle.tools.mathtools.lcm import lcm
import math
from fractions import gcd

def star_crisscross(width, height, num_points = 5, jump_size = None, find_valid_jump_size = True):  
   '''
      Draws a star with criscrossing lines.
      
      jump_size determines how many points to skip between connected points.
      an illegal jump size (one that does not result in a valid crisscross star)
      is ignored and replaced with a dot in the center of the star.
   '''
   corners = []
   pi_div_180 = math.pi / 180.0
   half_width = width * 0.5
   half_height = height * 0.5

   degrees = degrees_offset = 90
      
   degrees_incr = 360.0 / num_points

   while degrees < 360.0 + degrees_offset: 
      alpha = degrees * pi_div_180
      sin_alpha = math.sin(alpha);
      cos_alpha = math.cos(alpha);
         
      point_x = (half_width * cos_alpha);
      point_y = (half_height * sin_alpha);

      corners.append((point_x, point_y))
      
      degrees += degrees_incr

   corners.append(corners[0])
      
   if num_points == 6:
      #special case, ignore jump_size
      #rearrange points to draw two polygons
      multiplier = int(num_points / 2)
      
      corners1 = [corners[0], corners[2], corners[4]]
      corners2 = [corners[1], corners[3], corners[5]]
      
      poly1 = Polygon(corners1)
      poly2 = Polygon(corners2)
      return Group([poly1, poly2])

   else:
      if jump_size is None:
         jump_size = int(num_points/2)

      if gcd(num_points, jump_size) != 1:
         if find_valid_jump_size:
            while gcd(num_points, jump_size) != 1:
               jump_size -= 1
         else:
            invalid_star = [[half_width, half_height], [half_width, half_height]]
            return Polygon(invalid_star)
      
      point_order = []
      for i in range(0, num_points):
         point_num =  (i * jump_size) % num_points
         point_order.append(point_num)
      
      corners = [corners[i] for i in point_order]
      
      return  Polygon(corners)


## RUN DEMO CODE
if __name__ == '__main__':
   from chiplotle.tools import io
   from chiplotle.geometry.shapes.star_crisscross import star_crisscross
   from chiplotle.geometry.core.group import Group
   from chiplotle.geometry.transforms.offset import offset
   
   gr1 = Group()
   
   for points in range(5, 26):
      for i in range(1, points):
         s = star_crisscross(1000, 1000, num_points = points, 
            jump_size = i, find_valid_jump_size = False)
         offset(s, ((i - 1) * 1000, -(points - 5) * 1000))
         gr1.append(s)
   
   io.view(gr1)
   

