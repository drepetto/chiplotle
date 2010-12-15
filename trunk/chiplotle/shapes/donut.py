from chiplotle.shapes.polygon import Polygon
from chiplotle.shapes.ellipse import Ellipse
from chiplotle.hpgl.coordinatepair import CoordinatePair
from chiplotle.hpgl.commands import PU, PD, PA
import math

class Donut(Polygon):
   '''
      A donut (ellipse within ellipse) with a width, height, inset, segments,
      and offset.
      
      inset is the distance to inset the inner ellipse from the outer.
      
      segments is how many lines should be used to draw ellipse. More
      segments create a smoother ellipse, but will take longer to draw.
      
      offset is a CoordinatePair for moving the Donut around on the page.
      
      The Donut is drawn with the current pen location as the center.
      offset may be used to shift this around, for example, to draw from
      the lower, left corner.
   '''

   def __init__(self, width, height, inset, segments, offset):  
      self.width = width
      self.height = height
      self.inset = inset
      self.segments = segments
      
      e1 = Ellipse(width, height, segments, offset)
      e1_points = e1.points[0]
      e2 = Ellipse(width - (inset * 2), height - (inset * 2), segments, offset)
      e2_points = e2.points[0]
      
      Polygon.__init__(self, [e1_points, e2_points], offset)  

      
'''
from shapes.donut import Donut
d1 = Donut(1000,2000, 200, 100, [0,0])
d1.points
d1.format
io.view(d1)


'''