from chiplotle.shapes.shape import _Shape
from chiplotle.hpgl.coordinatepair import CoordinatePair
from chiplotle.hpgl.coordinatearray import CoordinateArray
import math

class Star(_Shape):
   '''
      A star with a width, height, star_type, num_points, and offset.

      offset is a CoordinatePair for moving the shape around in 2D space
      rotation is an angle expressed in radians
      pivot is a CoordinatePair indicating the point around which to rotate
      
      star_type is either "outline" or "crisscross". "outline" draws
      the outline of the star. "crisscross" connects points across the
      star to one another. The effect of crisscross depends on the number
      of points. Odd numbers of points result in one continuous polygon.
      Even numbers of points result in two overlapping polygons.
      
      num_points is the number of points in the star (duh). 
      
      The Star is drawn with the current pen location as the center.
      offset may be used to shift this around, for example, to draw from
      the lower, left corner.
   '''

   def __init__(self, width, height, star_type = "outline", num_points = 5, offset=(0, 0), rotation=0, pivot=(0, 0)):  
      self.width = width
      self.height = height
      self.star_type = star_type
      self.num_points = num_points
      
      _Shape.__init__(self, offset, rotation, pivot)

   
   @property
   def points(self):
      corners = []
      
      if self.star_type is "outline":
         pi_div_180 = math.pi / 180.0
         degrees_incr = 360.0/float(self.num_points * 2)
         half_width = self.width * 0.5
         quarter_width = half_width * 0.5
         half_height = self.height * 0.5
         quarter_height = half_height * 0.5
   
         degrees_offset = 90
         degrees = degrees_offset
         
         even = True
         
         while degrees < 360.0 + degrees_offset: 
            alpha = degrees * pi_div_180
            sin_alpha = math.sin(alpha);
            cos_alpha = math.cos(alpha);
   
            if even:
               w_multi = half_width
               h_multi = half_height
               even = False
            else:
               w_multi = quarter_width
               h_multi = quarter_height
               even = True
               
            point_x = (w_multi * cos_alpha);
            point_y = (h_multi * sin_alpha);
    
            corners.append(CoordinatePair(point_x, point_y))
            
            degrees += degrees_incr
   
         last_point = CoordinatePair(corners[0])
         corners.append(last_point)
      else:
         if self.num_points % 2 == 0:
            #even number of points, we need two polygons
            #NOT IMPLEMENTED!!!
            pi_div_180 = math.pi / 180.0
            degrees_incr = 360.0/float(self.num_points * 2)
            half_width = self.width * 0.5
            quarter_width = half_width * 0.5
            half_height = self.height * 0.5
            quarter_height = half_height * 0.5
      
            degrees_offset = 90
            degrees = degrees_offset
            
            even = True
            
            while degrees < 360.0 + degrees_offset: 
               alpha = degrees * pi_div_180
               sin_alpha = math.sin(alpha);
               cos_alpha = math.cos(alpha);
      
               if even:
                  w_multi = half_width
                  h_multi = half_height
                  even = False
               else:
                  w_multi = quarter_width
                  h_multi = quarter_height
                  even = True
                  
               point_x = (w_multi * cos_alpha);
               point_y = (h_multi * sin_alpha);
       
               corners.append(CoordinatePair(point_x, point_y))
               
               degrees += degrees_incr
      
            last_point = CoordinatePair(corners[0])
            corners.append(last_point)
         else:
            #odd number of points, just connect them!
            pi_div_180 = math.pi / 180.0
            degrees_incr = 360.0/float(self.num_points)
            half_width = self.width * 0.5
            half_height = self.height * 0.5
      
            degrees_offset = 90
            degrees = degrees_offset
            
            while degrees < 360.0 + degrees_offset: 
               alpha = degrees * pi_div_180
               sin_alpha = math.sin(alpha);
               cos_alpha = math.cos(alpha);
                  
               point_x = (half_width * cos_alpha);
               point_y = (half_height * sin_alpha);
       
               corners.append(CoordinatePair(point_x, point_y))
               
               degrees += degrees_incr
      
            last_point = CoordinatePair(corners[0])
            corners.append(last_point)
            
            #rearrange points to draw crisscross
            multiplier = int(self.num_points / 2)
            point_order = []
            for i in range(self.num_points + 1):
               point_order.append((i * multiplier) % self.num_points)
            
            corners = [ corners[i] for i in point_order]
            
      return [CoordinateArray(corners)]

   '''
from chiplotle.shapes.star import Star
s1 = Star(1000,1000, star_type = "crisscross")
io.view(s1)

   '''

## RUN DEMO CODE
if __name__ == '__main__':
   from chiplotle.shapes.star import Star
   from chiplotle.shapes.group import Group
   from chiplotle.tools import io
   import math
   s1 = Star(1000, 1000)
   print '\nStar(1000, 1000)'
   print s1.format

   ## displaced
   s2 = Star(1000, 1000, num_points = 7, offset = (100, 100)) 
   print '\nStar(1000, 1000, num_points = 7, offset = (100, 100))'
   print s2.format

   ## displaced and rotated around (0, 0)
   s3 = Star(1000, 1000, star_type = "crisscross", offset = (100, 100), rotation = math.pi / 3) 
   print '\nStar(1000, 1000, star_type = "crisscross", offset = (100, 100), rotation = math.pi / 3)'
   print s3.format

   ## displaced and rotated around (100, 100)
   s4 = Star(1000, 1000, num_points = 9, star_type = "crisscross", offset = (100, 100), rotation = math.pi / 3, pivot = (100, 100)) 
   print '\nStar(1000, 1000, num_points = 9, star_type = "crisscross", offset = (100, 100), rotation = math.pi / 3, pivot = (100, 100))'
   print s4.format

   g1 = Group([s1, s2, s3, s4])
   io.view(g1)
   