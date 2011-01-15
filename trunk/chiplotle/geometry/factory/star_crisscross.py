from chiplotle.geometry.shapes.path import Path
from chiplotle.geometry.shapes.group import Group
from chiplotle.tools.mathtools.lcm import lcm

def star_crisscross(width, height, num_points = 5):  
   '''Draws a star with criscrossing lines.'''
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
      #rearrange points to draw two polygons
      multiplier = int(num_points / 2)
      
      corners1 = [corners[0], corners[2], corners[4], corners[0]]
      corners2 = [corners[1], corners[3], corners[5], corners[1]]
      
      return Group([Path(corners1), Path(corners2)])

   else:            
      multiplier = int(math.ceil((num_points / 4.0) + 1))
      
      if multiplier < 2:
         multiplier = 2
         
      while num_points % multiplier < 2:
         multiplier += 1
      
      the_lcm = lcm(num_points, multiplier)
      
      times_through = 0
      multi_incr = 1
      
      while the_lcm / multiplier <= num_points / 2:              
         if multiplier <= num_points / 3:
            multiplier += 1
         else:
            multiplier -= 1
         
         if num_points % multiplier == 0:
            if multiplier <= num_points / 3:
               multiplier += multi_incr
            else:
               multiplier -= multi_incr
         the_lcm = lcm(num_points, multiplier)
         
         times_through += 1
         
         if times_through % 5 == 0:
            multi_incr += 1
            
      point_order = []
      for i in range(num_points + 1):
         point_order.append((i * multiplier) % num_points)
      
      corners = [corners[i] for i in point_order]
      
      return Path(corners)
   


## RUN DEMO CODE
if __name__ == '__main__':
   from chiplotle.tools import io
   import math
   
   s1 = star_crisscross(1000, 1000)

   ## displaced
   s2 = star_crisscross(1000, 1000, num_points = 7)
   s2.offset = (1000, 0)

   ## displaced and rotated 
   s3 = star_crisscross(1000, 1000)
   s3.offset = (2000, 0)
   s3.rotation = math.pi / 3.0

   ## displaced and rotated around pivot
   s4 = star_crisscross(1000, 1000, num_points = 9)
   s4.offset = (3000, 0)
   s4.rotation = math.pi / 3.0
   s4.pivot = (100, 100)

   gr = Group([s1, s2, s3, s4])
   io.view(gr)
