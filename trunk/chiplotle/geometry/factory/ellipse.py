from chiplotle.geometry.shapes.path import Path
import math

def ellipse(width, height, segments = 100):  
   '''Constructs an ellipse with the given `radius` and number of segments.'''

   pi_div_180 = math.pi / 180.0
   degrees_incr = 360.0 / float(segments)
   half_width = width * 0.5
   half_height = height * 0.5
   
   degrees = 0.0
   
   ellipse_points = []
   
   while degrees < 360.0: 
      alpha = degrees * pi_div_180
      sin_alpha = math.sin(alpha);
      cos_alpha = math.cos(alpha);

      point_x = (half_width * cos_alpha);
      point_y = (half_height * sin_alpha);

      ellipse_points.append((point_x, point_y))
      
      degrees += degrees_incr
 
   #close the ellipse
   degrees = 0.0
   alpha = degrees * pi_div_180
   sin_alpha = math.sin(alpha);
   cos_alpha = math.cos(alpha);

   point_x = (half_width * cos_alpha);
   point_y = (half_height * sin_alpha);

   ellipse_points.append((point_x, point_y))
   
   return Path(ellipse_points)


## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.tools import io
   e = ellipse(10, 20)
   assert isinstance(e, Path)
   print e.format
   io.view(e)
