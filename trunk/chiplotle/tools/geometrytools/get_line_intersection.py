from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.geometry.core.path import Path
   
def get_line_intersection(line_a, line_b):
   '''
   Finds the intersection point, if any, between lines a and b.
   Returns a Coordinate or None if there is no intersection.
   '''
    
   #make sure we have two lines
   assert isinstance(line_a, Path) and len(line_a) == 2
   assert isinstance(line_b, Path) and len(line_b) == 2   
   
   p0_x, p0_y = line_a.points[0]
   p1_x, p1_y = line_a.points[1]
   p2_x, p2_y = line_b.points[0]
   p3_x, p3_y = line_b.points[1]
    
   s1_x = float(p1_x - p0_x)
   s1_y = float(p1_y - p0_y)
   s2_x = float(p3_x - p2_x)
   s2_y = float(p3_y - p2_y)

   s_divisor = (-s2_x * s1_y + s1_x * s2_y)
   if s_divisor == 0.0:
      s = -1.0
   else:
      s = (-s1_y * (p0_x - p2_x) + s1_x * (p0_y - p2_y)) / s_divisor
      
   t_divisor = (-s2_x * s1_y + s1_x * s2_y)
   
   if t_divisor == 0.0:
      t = -1.0
   else:
      t = ( s2_x * (p0_y - p2_y) - s2_y * (p0_x - p2_x)) / t_divisor

   if s >= 0 and s <= 1 and t >= 0 and t <= 1:
      #Collision detected
      i_x = p0_x + (t * s1_x)
      i_y = p0_y + (t * s1_y)
      return Coordinate(i_x, i_y)
   else:
      #No collision
      return None
   


## DEMO
if __name__ == '__main__':
   from chiplotle.geometry.shapes.line import line
   from chiplotle.geometry.core.group import Group
   from chiplotle.tools import io
   from random import randrange
   
   #draw a bunch of lines that do not intersect
   
   no_intersections = Group()

   line_1 = line([randrange(0, 4000), randrange(0, 4000)], 
      [randrange(0, 4000), randrange(0, 4000)])
   no_intersections.append(line_1)
   
   while len(no_intersections) < 300:
      new_line = line([randrange(0, 4000), randrange(0, 4000)], 
         [randrange(0, 4000), randrange(0, 4000)])
      
      intersection = False
      
      for l in no_intersections:
         if get_line_intersection(new_line, l) != None:
            intersection = True
            break
         
      if intersection == False:
         no_intersections.append(new_line)
         print "found %d lines..." % len(no_intersections)
               
   io.view(no_intersections)
   
