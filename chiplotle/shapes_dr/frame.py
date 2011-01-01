from chiplotle.shapes.polygon import Polygon
from chiplotle.shapes.rectangle import Rectangle
from chiplotle.geometry.coordinate import Coordinate
from chiplotle.hpgl.commands import PU, PD, PA

class Frame(Polygon):
   '''
      A frame (rect within a rect) with a width, height, inset, and offset.
      
      inset is the distance to inset the inner rect from the outer.
      
      offset is a Coordinate for moving the Rectangle around on the page.
      
      The Frame is drawn with the current pen location as the center.
      offset may be used to shift this around, for example, to draw from
      the lower, left corner.
   '''

   def __init__(self, width, height, inset, offset):  
      self.width = width
      self.height = height
      self.inset = inset
      
      
      r1 = Rectangle(width, height, offset)
      r1_points = r1.points[0]
      r2 = Rectangle(width - (inset * 2), height - (inset * 2), offset)
      r2_points = r2.points[0]
      
      Polygon.__init__(self, [r1_points, r2_points], offset) 
      
      
'''
from shapes.frame import Frame
f1 = Frame(1000, 2000, 200, [0,0])
f1.points
f1.format
io.view(f1)


'''