from chiplotle.geometry.coordinate import Coordinate

def get_line_intersection(line_a, line_b):
   '''
   Finds the intersection point, if any, between lines a and b.
   Returns a Coordinate or None if there is no intersection.
   '''
    
   p0_x, p0_y = line_a[0]
   p1_x, p1_y = line_a[1]
   p2_x, p2_y = line_b[0]
   p3_x, p3_y = line_b[1]
    
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
   
   #print "s: %f" % s
   #print "t: %f" % t

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
   from chiplotle.geometry.factory.line import line
   from chiplotle.geometry.shapes.group import Group
   from chiplotle.tools import io

   line_a = line([0,0], [1000,700])
   line_b = line([1000,0], [0, 1000])
   
   intersection = get_line_intersection(line_a, line_b)
   
   print "intersection: "
   print intersection
   
   line_c = line([100, 1100], [900, 1100])
   line_d = line([100, 1200], [900, 1200])
   
   intersection = get_line_intersection(line_c, line_d)
   
   print "intersection: "
   print intersection

   line_e = line([1100, 100], [1100, 900])
   line_f = line([1200, 100], [1200, 900])
   
   intersection = get_line_intersection(line_e, line_f)
   
   print "intersection: "
   print intersection
   
   g = Group([line_a, line_b, line_c, line_d, line_e, line_f])
   io.view(g)
   
