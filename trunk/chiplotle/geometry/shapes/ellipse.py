from chiplotle.geometry.shapes.shape import _Shape
from chiplotle.geometry.coordinate import Coordinate
from chiplotle.geometry.coordinatearray import CoordinateArray
import math

class Ellipse(_Shape):
   '''
      An ellipse with a width, height, segments.
      
      segments is how many lines should be used to draw ellipse. More
      segments create a smoother ellipse, but will take longer to draw.
      
      The Ellipse is drawn with the current pen location as the center.
      offset may be used to shift this around, for example, to draw from
      the lower, left corner.
   '''
   def __init__(self, width, height, segments = 100):  
      self.width = width
      self.height = height
      self.segments = segments

      _Shape.__init__(self)
      

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
   from chiplotle.geometry.shapes.ellipse import Ellipse
   from chiplotle.geometry.shapes.group import Group
   from chiplotle.tools import io
   import math
   
   e1 = Ellipse(100, 50)
   print '\nEllipse(100, 50)'
   print e1.format

   ## displaced
   e2 = Ellipse(100, 50)
   e2.offset = (100, 100)
   print '\nEllipse(100, 50)\noffset = (100, 100)'
   print e2.format

   ## displaced and rotated around (0, 0)
   e3 = Ellipse(100, 50)
   e3.offset = (100, 100)
   e3.rotation = math.pi / 3.0
   print '\nEllipse(100, 50)\noffset = (100, 100)\n rotation = math.pi / 3.0'
   print e3.format

   ## displaced and rotated around (100, 100)
   e4 = Ellipse(100, 50)
   e4.offset = (100, 100)
   e4.rotation = math.pi / 3.0
   e4.pivot = (100, 100)
   print '\nEllipse(100, 50)\noffset = (100, 100)\nrotation = math.pi / 3.0\npivot = (100, 100)'
   print e4.format
   
   g1 = Group([e1, e2, e3, e4])
   io.view(g1)
   
   