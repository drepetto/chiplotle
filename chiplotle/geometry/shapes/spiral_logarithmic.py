from chiplotle.geometry.core.path import Path
import math

def spiral_logarithmic(num_turns = 5, 
                       expansion_rate = 0.2, 
                       direction = "cw", 
                       segments = 500):  
   '''
   Constructs an logarithmic spiral with the given number of turns using the
   specified number of points.
   
   expansion_rate controls how large the spiral is for a given number of
   turns. Very small numbers will result in tightly-wound spirals. Large numbers
   will give spirals with giant "tails". Typical values range from 0.1 to 0.3
   
   The logarithmic spiral equation is:
   
   r = e^(bt)
   
   where r is the radius, e is e, b is the expansion rate, and t is theta
   
   '''
   
   two_pi = math.pi * 2.0
   total_rads = two_pi * num_turns
   theta = 0.0
   theta_incr = total_rads / float(segments - 1)

   expansion_rate = abs(expansion_rate)
   
   x, y = 0.0, 0.0
   spiral_points = [(x, y)]
   theta += theta_incr
   
   for i in range(segments - 1):
      x = math.cos(theta) * math.pow(math.e, (expansion_rate * theta))
      y = math.sin(theta) * math.pow(math.e, (expansion_rate * theta))

      if direction == "ccw":
         y *= -1.0
      
      spiral_points.append((x, y))
      theta += theta_incr
      
   return Path(spiral_points)


## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.geometry.core.group import Group
   from chiplotle.geometry.shapes.line import line
   from chiplotle.geometry.transforms.offset import offset
   from chiplotle.tools import io
   
   s = spiral_logarithmic()

   #add some lines for scale
   line_right = line((0,0), (500, 0))
   line_left = line((0,0), (-500, 0))
   line_up = line((0,0), (0, 500))
   line_down = line((0,0), (0, -500))
   
   g = Group([s, line_right, line_left, line_up, line_down])

   io.view(g)
