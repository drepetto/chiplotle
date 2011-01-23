from chiplotle.geometry.shapes.polygon import Polygon
from chiplotle.geometry.coordinate import Coordinate
from chiplotle.hpgl.commands import PU, PD, PA
import math

class Ellipse(Polygon):
   '''
      An ellipse with a width, height, segments, and offset.
      
      segments is how many lines should be used to draw ellipse. More
      segments create a smoother ellipse, but will take longer to draw.
      
      offset is a Coordinate for moving the Ellipse around on the page.
      
      The Ellipse is drawn with the current pen location as the center.
      offset may be used to shift this around, for example, to draw from
      the lower, left corner.
   '''

   def __init__(self, width, height, segments, offset):  
      self.width = width
      self.height = height
      self.segments = segments
   
      pi_div_180 = math.pi / 180.0
      rads_incr = 360.0/float(segments)
      half_width = width * 0.5
      half_height = height * 0.5
      
      rads = 0.0
      
      ellipse_points = []
      
      while rads < 360.0: 
         alpha = rads * pi_div_180
         sin_alpha = math.sin(alpha);
         cos_alpha = math.cos(alpha);

         point_x = (half_width * cos_alpha);
         point_y = (half_height * sin_alpha);
 
         ellipse_points.append(Coordinate(point_x, point_y))
         
         rads += rads_incr
    
      #close the ellipse
      rads = 0.0
      alpha = rads * pi_div_180
      sin_alpha = math.sin(alpha);
      cos_alpha = math.cos(alpha);

      point_x = (half_width * cos_alpha);
      point_y = (half_height * sin_alpha);
 
      ellipse_points.append(Coordinate(point_x, point_y))
      
      Polygon.__init__(self, [ellipse_points], offset)  

      
'''
from shapes.ellipse import Ellipse
e1 = Ellipse(1000,2000, 100, [0,0])
e1.points
e1.format
io.view(e1)


'''