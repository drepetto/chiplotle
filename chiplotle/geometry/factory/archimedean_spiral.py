from chiplotle.geometry.shapes.path import Path
import math

def archimedean_spiral(num_turns = 5, turn_spacing = 100, direction = "cw", exponent = 1.0, segments = 500):  
   '''
   Constructs an Archimedean (arithmetic) spiral with the given number of
   turns, turn spacing, direction ("cw" or "ccw"), exponent, and number of
   segments.
   
   The default values will create a CW spiral with a right half that is
   500 (num_turns * turn_spacing) units from the center to the edge. 
   
   r = b * theta^1/x
   
   '''

   two_pi = math.pi * 2.0
   total_rads = two_pi * num_turns
   theta = 0.0
   theta_incr = total_rads / float(segments - 1)
   
   radius_multi = turn_spacing/two_pi

   if direction is "ccw":
      theta_incr *= -1.0
   
   spiral_points = []
   
   for i in range(segments):
      r_width = radius_multi * (pow(theta, exponent)) 
      r_height = radius_multi * (pow(theta, exponent))
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
   from chiplotle.geometry.factory.line import line
   from chiplotle.tools import io
   
   s = archimedean_spiral(exponent = .2)
   assert isinstance(s, Path)
 
   line_right = line((0,0), (500, 0))
   line_left = line((0,0), (-500, 0))
   line_up = line((0,0), (0, 500))
   line_down = line((0,0), (0, -500))
   
   g = Group([s, line_right, line_left, line_up, line_down])

   io.view(g)
