from chiplotle.geometry.factory.ellipse import ellipse
from chiplotle.geometry.shapes.group import Group
from chiplotle.geometry.shapes.path import Path

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
   import math
   d1 = donut(1000, 500, inset = 20)
   print 'donut(1000, 500, inset = 20)'
   #print d1.format

   ## displaced
   d2 = donut(1000, 500, inset = 20)
   d2.offset = (100, 100)
   print 'donut(1000, 500, inset = 20)\noffset = (100, 100)'
   #print d2.format

   ## displaced and rotated around (0, 0)
   d3 = donut(1000, 500, inset = 20)
   d3.offset = (100, 100)
   d3.rotation = math.pi / 3.0
   print 'donut(1000, 500, inset = 20)\noffset = (100, 100)\nrotation = math.pi / 3.0'
   #print d3.format

   ## displaced and rotated around (100, 100)
   d4 = donut(1000, 500, inset = 20)
   d4.offset = (100, 100)
   d4.rotation = math.pi / 3.0
   d4.pivot = (100, 100)
   print 'donut(1000, 500, inset = 20)\noffset = (100, 100)\nrotation = math.pi / 3.0\npivot = (100, 100)'
   #print d4.format

   g1 = Group([d1, d2, d3, d4])
   io.view(g1)
