from chiplotle.geometry.core.path import Path
import math

def spiral_archimedean(radius, num_turns = 5, wrapping_constant = 1, direction = "cw", segments = 500):  
   '''
   Constructs an Archimedean (arithmetic) spiral with the given number of
   turns using the specified number of points.
   
   wrapping_constant controls how tightly the spiral is wound. Several classic
   spirals can be created using different wrapping_constants:
   
   lituus:              -2
   hyperbolic spiral:   -1
   Archimedes' spiral:   1
   Fermat's spiral:      2
   
   scaler controls how large the spiral is.
   
   The general Archimedean spiral equation is:
   
   r = a * theta^(1/n) 
   
   where r is the radius, a is the scaler, and n is the wrapping_constant.
   
   
   More info:
   http://mathworld.wolfram.com/ArchimedeanSpiral.html
   
   '''
   
   two_pi = math.pi * 2.0
   total_rads = two_pi * num_turns
   theta = 0.0
   theta_incr = total_rads / float(segments - 1)
   exponent = 1.0/wrapping_constant
   
   scaler = float(radius) / math.pow(total_rads, exponent)
   
   #Spirals with a negative wrapping_constant technically begin at infinity,
   #which obviously isn't practical. So we nudge theta by a bit to get a
   #reasonable starting point
   if wrapping_constant < 0.0:
      theta += theta_incr
      pow = math.pow(theta_incr, abs(exponent))
      scaler = float(radius) / (1.0/pow)

   spiral_points = []
   r = 0.0
   
   for i in range(segments):
      if exponent > 0:
         r = scaler * math.pow(theta, exponent)
      else:
         pow = math.pow(theta, abs(exponent))
         r = scaler * 1.0/pow
         
      x = math.cos(theta) * r
      y = math.sin(theta) * r
      
      if direction == "ccw":
         y *= -1.0
      #print "r: %f theta: %f" % (r, theta)
      spiral_points.append((x, y))
      
      theta += theta_incr   
   
   result = Path(spiral_points)

   return result


## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.geometry.core.group import Group
   from chiplotle.geometry.transforms.offset import offset
   from chiplotle.geometry.transforms.rotate import rotate
   from chiplotle.tools import io
   
   #one of each main spiral type
   s1 = spiral_archimedean(500, wrapping_constant = 1)
   
   s2 = spiral_archimedean(500, wrapping_constant = 2, direction = "ccw")
   offset(s2, (0, -1000))
   
   #these two are long, so we'll rotate them and move them to the side
   #of the others
   s3 = spiral_archimedean(1800, wrapping_constant = -1, direction = "ccw")
   rotate(s3, math.pi * 1.5)
   offset(s3, (650, 400))
   s4 = spiral_archimedean(1500, wrapping_constant = -2, direction = "ccw")
   rotate(s4, math.pi * .6)
   offset(s4, (1000, -1100))
   
   g = Group([s1, s2, s3, s4])

   io.view(g)
