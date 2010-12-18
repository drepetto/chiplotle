from chiplotle.shapes.shape import _Shape
from chiplotle.hpgl.coordinate import Coordinate
from chiplotle.hpgl.coordinatearray import CoordinateArray
import math

class Ellipse(_Shape):
   '''
      An ellipse with a width, height, segments, and offset.
      
      offset is a Coordinate for moving the shape around in 2D space
      rotation is an angle expressed in radians
      pivot is a Coordinate indicating the point around which to rotate
      
      segments is how many lines should be used to draw ellipse. More
      segments create a smoother ellipse, but will take longer to draw.
      
      The Ellipse is drawn with the current pen location as the center.
      offset may be used to shift this around, for example, to draw from
      the lower, left corner.
   '''
   def __init__(self, width, height, segments = 100, offset=(0, 0), rotation=0, pivot=(0, 0)):  
      self.width = width
      self.height = height
      self.segments = segments

      _Shape.__init__(self, offset, rotation, pivot)
      

   @property
   def points(self):
      pi_div_180 = math.pi / 180.0
      degrees_incr = 360.0/float(self.segments)
      half_width = self.width * 0.5
      half_height = self.height * 0.5
      
      degrees = 0.0
      
      ellipse_points = []
      
      while degrees < 360.0: 
         alpha = degrees * pi_div_180
         sin_alpha = math.sin(alpha);
         cos_alpha = math.cos(alpha);

         point_x = (half_width * cos_alpha);
         point_y = (half_height * sin_alpha);
 
         ellipse_points.append(Coordinate(point_x, point_y))
         
         degrees += degrees_incr
    
      #close the ellipse
      degrees = 0.0
      alpha = degrees * pi_div_180
      sin_alpha = math.sin(alpha);
      cos_alpha = math.cos(alpha);

      point_x = (half_width * cos_alpha);
      point_y = (half_height * sin_alpha);
 
      ellipse_points.append(Coordinate(point_x, point_y))
      
      return [CoordinateArray(ellipse_points)]


## RUN DEMO CODE
if __name__ == '__main__':
   from chiplotle.shapes.ellipse import Ellipse
   from chiplotle.shapes.group import Group
   from chiplotle.tools import io
   import math
   e1 = Ellipse(100, 50)
   print '\nEllipse(100, 50)'
   print e1.format

   ## displaced
   e2 = Ellipse(100, 50, offset = (100, 100)) 
   print '\nEllipse(100, 50, (100, 100))'
   print e2.format

   ## displaced and rotated around (0, 0)
   e3 = Ellipse(100, 50, offset = (100, 100), rotation = math.pi / 3) 
   print '\nEllipse(100, 50, (100, 100), math.pi / 3)'
   print e3.format

   ## displaced and rotated around (100, 100)
   e4 = Ellipse(100, 50, offset = (100, 100), rotation = math.pi / 3, pivot = (100, 100)) 
   print '\nEllipse(100, 50, (100, 100), math.pi / 3, (100, 100))'
   print e4.format
   
   g1 = Group([e1, e2, e3, e4])
   io.view(g1)
   
   