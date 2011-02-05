from chiplotle.geometry.shapes.path import Path
import math

def spiral(width, height, turns = 5, direction = "cw", segments = 500):  
   '''
   Constructs an Archimedean (arithmetic) spiral with the given width, height,
   number of turns, direction ("cw" or "ccw"), and number of segments.
   
   Normal spirals have width == height, but this one allows you to distort
   the spiral by using different width and height values

   r = b * theta
   
   '''

   two_pi = math.pi * 2.0
   total_rads = two_pi * turns
   theta = 0.0
   theta_incr = total_rads / float(segments)
   
   if direction is "ccw":
      theta_incr *= -1.0
      
   half_width = width * 0.51
   half_height = height * 0.51
   half_width_multi = half_width / total_rads
   half_height_multi = half_height / total_rads
   
   spiral_points = []
   
   for i in range(segments):
      r_width = half_width_multi * theta 
      r_height = half_height_multi * theta
      x = math.cos(theta) * r_width;
      y = math.sin(theta) * r_height;
      spiral_points.append((x, y))
      theta += theta_incr

   result = Path(spiral_points)

   return result


## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.tools.geometrytools.get_bounding_rectangle import get_bounding_rectangle
   from chiplotle.geometry.shapes.group import Group
   from chiplotle.geometry.factory.rectangle import rectangle
   from chiplotle.tools import io
   
   s = spiral(200, 150, turns = 10)
   assert isinstance(s, Path)

   s_rect = get_bounding_rectangle(s)
   
   #NOT THE RIGHT SIZE?!?
   
   rect = rectangle(200, 150)
   
   g = Group([s, s_rect, rect])

   io.view(g)
