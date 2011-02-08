from chiplotle.geometry.shapes.path import Path
import math

def archimedean_spiral(num_turns = 5, turn_spacing = 100, direction = "cw", segments = 500):  
   '''
   Constructs an Archimedean (arithmetic) spiral with the given number of
   turns, turn spacing, direction ("cw" or "ccw"), exponent, and number of
   segments.
   
   The default values will create a CW spiral with a right half that is
   500 (num_turns * turn_spacing) units from the center to the edge. 
   
   r = b * theta
   
   '''

   two_pi = math.pi * 2.0
   total_rads = two_pi * num_turns
   theta = 0.0
   theta_incr = total_rads / float(segments - 1)

   if direction is "ccw":
      theta_incr *= -1.0
   
   spiral_points = []
   
   for i in range(segments):
      
      x = math.cos(theta) * ((turn_spacing * theta)/two_pi)
      y = math.sin(theta) * ((turn_spacing * theta)/two_pi)

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
   
   s = archimedean_spiral()
   assert isinstance(s, Path)
   
   line_right = line((0,0), (500, 0))
   line_left = line((0,0), (-500, 0))
   line_up = line((0,0), (0, 500))
   line_down = line((0,0), (0, -500))
   
   g = Group([s, line_right, line_left, line_up, line_down])

   io.view(g)
