from chiplotle.shapes.shape import _Shape
from chiplotle.geometry.coordinate import Coordinate
from chiplotle.geometry.coordinatearray import CoordinateArray
import math
import fractions

class Star(_Shape):
   '''
      A star with a width, height, star_type, num_points.
      
      star_type is either "outline" or "crisscross". "outline" draws
      the outline of the star. "crisscross" connects points across the
      star to one another. The effect of crisscross depends on the number
      of points. Odd numbers of points result in one continuous polygon.
      Even numbers of points result in two overlapping polygons.
      
      num_points is the number of points in the star (duh). Must be >= 5
      
      The Star is drawn with the current pen location as the center.
      offset may be used to shift this around, for example, to draw from
      the lower, left corner.
   '''

   def __init__(self, width, height, star_type = "outline", num_points = 5):  
      self.width = width
      self.height = height
      self.star_type = star_type
      self.num_points = num_points
      
      if num_points < 5:
         print "num_points must be >= 5!"
         self.num_points = 5
      
      _Shape.__init__(self)

   
   @property
   def points(self):
      corners = []
      pi_div_180 = math.pi / 180.0
      half_width = self.width * 0.5
      half_height = self.height * 0.5

      degrees_offset = 90
      degrees = degrees_offset
         
      if self.star_type is "outline":
         even = True
         
         degrees_incr = 360.0/float(self.num_points * 2)
         quarter_width = half_width * 0.5
         quarter_height = half_height * 0.5
         
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
    
            corners.append(Coordinate(point_x, point_y))
            
            degrees += degrees_incr
   
         last_point = Coordinate(corners[0])
         corners.append(last_point)
         
         return [CoordinateArray(corners)]
         
      else:
         #rearrange points to draw crisscross
         degrees_incr = 360.0/self.num_points

         while degrees < 360.0 + degrees_offset: 
            alpha = degrees * pi_div_180
            sin_alpha = math.sin(alpha);
            cos_alpha = math.cos(alpha);
               
            point_x = (half_width * cos_alpha);
            point_y = (half_height * sin_alpha);
    
            corners.append(Coordinate(point_x, point_y))
            
            degrees += degrees_incr
   
         last_point = Coordinate(corners[0])
         corners.append(last_point)
            
         if self.num_points == 6:            
            #rearrange points to draw two polygons
            multiplier = int(self.num_points / 2)
            
            corners1 = [corners[0], corners[2], corners[4], corners[0]]
            corners2 = [corners[1], corners[3], corners[5], corners[1]]
            
            return [CoordinateArray(corners1), CoordinateArray(corners2)]

         else:            
            multiplier = int(math.ceil((self.num_points / 4.0) + 1))
            
            if multiplier < 2:
               multiplier = 2
               
            while self.num_points % multiplier < 2:
               multiplier += 1
            
            the_lcm = self.lcm(self.num_points, multiplier)
            
            times_through = 0
            multi_incr = 1
            
            while the_lcm / multiplier <= self.num_points / 2:              
               if multiplier <= self.num_points / 3:
                  multiplier += 1
               else:
                  multiplier -= 1
               
               if self.num_points % multiplier == 0:
                  if multiplier <= self.num_points / 3:
                     multiplier += multi_incr
                  else:
                     multiplier -= multi_incr
               the_lcm = self.lcm(self.num_points, multiplier)
               
               times_through += 1
               
               if times_through % 5 == 0:
                  multi_incr += 1
                  
            point_order = []
            for i in range(self.num_points + 1):
               point_order.append((i * multiplier) % self.num_points)
            
            corners = [ corners[i] for i in point_order]
            
            return [CoordinateArray(corners)]
      


   def lcm(self, a, b):      
      if (b > a):
         c=b;
         b=a;
         a=c;

      return (a * b) / fractions.gcd(a,b)


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
   s2 = Star(1000, 1000, num_points = 7)
   s2.offset = (1000, 0)
   print '\nStar(1000, 1000, num_points = 7)\noffset = (1000, 1000)'
   print s2.format

   ## displaced and rotated 
   s3 = Star(1000, 1000, star_type = "crisscross")
   s3.offset = (2000, 0)
   s3.rotation = math.pi / 3.0
   print '\nStar(1000, 1000, star_type = "crisscross")\noffset = (2000, 2000)\nrotation = math.pi / 3.0'
   print s3.format

   ## displaced and rotated around pivot
   s4 = Star(1000, 1000, num_points = 9, star_type = "crisscross")
   s4.offset = (3000, 0)
   s4.rotation = math.pi / 3.0
   s4.pivot = (100, 100)
   print '\nStar(1000, 1000, num_points = 9, star_type = "crisscross")\noffset = (3000, 3000)\nrotation = math.pi / 3.0\npivot = (100, 100)'
   print s4.format

   g1 = Group([s1, s2, s3, s4])
   io.view(g1)
   
   import time
   time.sleep(1)
   
   gr2 = Group()
   
   for i in range(5, 10):
      st = st = Star(1000,1000, num_points = i, star_type = "crisscross")
      st.rotation = (i - 5) * ((math.pi * 2)/5.0)
      st.pivot = [500,500]
      gr2.append(st)
   
   io.view(gr2)
   

