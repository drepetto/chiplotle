from chiplotle.geometry.shapes.ellipse import ellipse
from chiplotle.geometry.core.group import Group
from chiplotle.geometry.core.path import Path

def donut(width, height, inset, segments = 100):  
   '''
      A donut (ellipse within ellipse) with a width, height, inset, segments.
      
      segments is how many lines should be used to draw ellipse. More
      segments create a smoother ellipse, but will take longer to draw.
      
      inset is the distance to inset the inner ellipse from the outer.
      
      The donut is drawn with the current pen location as the center.
      offset may be used to shift this around, for example, to draw from
      the lower, left corner.
   '''

   e1 = ellipse(width, height, segments)
   e2 = ellipse(width - (inset * 2), height - (inset * 2), segments)
   return Group([e1, e2])


## RUN DEMO CODE
if __name__ == '__main__':
   from chiplotle.tools import io

   d1 = donut(1000, 500, inset = 20)
   io.view(d1)
