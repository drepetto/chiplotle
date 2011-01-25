from chiplotle.geometry.shapes.path import Path

def star_outline(width, height, num_points = 5):  
   '''Constructs a star shape in outline.  '''
   corners = []
   pi_div_180 = math.pi / 180.0
   half_width = width * 0.5
   half_height = height * 0.5

   degrees = degrees_offset = 90
   even = True
   
   degrees_incr = 360.0 / float(num_points * 2)
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

      corners.append((point_x, point_y))
      
      degrees += degrees_incr

   corners.append(corners[0])
   
   path = Path(corners)
   path.closed = True
   
   return path



## RUN DEMO CODE
if __name__ == '__main__':
   from chiplotle.geometry.shapes.group import Group
   from chiplotle.tools import io
   import math
   
   gr = Group()
   
   for i in range(5, 10):
      st = star_outline(1000,1000, num_points = i)
      st.rotation = (i - 5) * ((math.pi * 2)/5.0)
      st.pivot = [500,500]
      gr.append(st)
   
   io.view(gr)
