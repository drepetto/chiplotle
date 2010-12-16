from chiplotle.shapes.shape import _Shape
from chiplotle.shapes.rectangle import Rectangle
from chiplotle.hpgl.coordinatepair import CoordinatePair
from chiplotle.hpgl.coordinatearray import CoordinateArray
import math

class Frame(_Shape):
   '''
      A frame (rectangle within a rectangle) with a width, height, inset,
      offset, rotation, and pivot.
      
      offset is a CoordinatePair for moving the shape around in 2D space
      rotation is an angle expressed in radians
      pivot is a CoordinatePair indicating the point around which to rotate
      
      inset is the distance to inset the inner ellipse from the outer.
      
      The Frame is drawn with the current pen location as the center.
      offset may be used to shift this around, for example, to draw from
      the lower, left corner.
   '''

   def __init__(self, width, height, inset, offset=(0, 0), rotation=0, pivot=(0, 0)):  
      self.width = width
      self.height = height
      self.inset = inset

      _Shape.__init__(self, offset, rotation, pivot)
      

   @property
   def points(self):
      
      
      r1 = Rectangle(self.width, self.height, self.offset)
      r1_points = r1.points[0]
      r2 = Rectangle(self.width - (self.inset * 2), self.height - (self.inset * 2), self.offset)
      r2_points = r2.points[0]
      
      return [CoordinateArray(r1_points), CoordinateArray(r2_points)]


## RUN DEMO CODE
if __name__ == '__main__':
   from chiplotle.shapes.frame import Frame
   from chiplotle.shapes.group import Group
   from chiplotle.tools import io
   import math
   d1 = Frame(1000, 500, inset = 20)
   print '\Frame(1000, 500, inset = 20)'
   print d1.format

   ## displaced
   d2 = Frame(1000, 500, inset = 20, offset = (100, 100)) 
   print '\Frame(1000, 500, inset = 20, offset = (100, 100)) '
   print d2.format

   ## displaced and rotated around (0, 0)
   d3 = Frame(1000, 500, inset = 20, offset = (100, 100), rotation = math.pi / 3) 
   print '\Frame(1000, 500, inset = 20, offset = (100, 100), rotation = math.pi / 3) '
   print d3.format

   ## displaced and rotated around (100, 100)
   d4 = Frame(1000, 500, inset = 20, offset = (100, 100), rotation = math.pi / 3, pivot = (100, 100)) 
   print '\Frame(1000, 500, inset = 20, offset = (100, 100), rotation = math.pi / 3, pivot = (100, 100))'
   print d4.format

   g1 = Group([d1, d2, d3, d4])
   io.view(g1)
   
   

