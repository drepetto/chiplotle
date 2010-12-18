from chiplotle.shapes.shape import _Shape
from chiplotle.shapes.rectangle import Rectangle
from chiplotle.hpgl.coordinate import Coordinate
from chiplotle.hpgl.coordinatearray import CoordinateArray
import math

class Frame(_Shape):
   '''
      A frame (rectangle within a rectangle) with a width, height, and inset.
      
      inset is the distance to inset the inner ellipse from the outer.
      
      The Frame is drawn with the current pen location as the center.
      offset may be used to shift this around, for example, to draw from
      the lower, left corner.
   '''

   def __init__(self, width, height, inset):  
      self.width = width
      self.height = height
      self.inset = inset

      _Shape.__init__(self)
      

   @property
   def points(self):
      r1 = Rectangle(self.width, self.height)
      r1.offset = self.offset
      r1.rotation = self.rotation
      r1.pivot = self.pivot
      
      r1_points = r1.points[0]
      
      r2 = Rectangle(self.width - (self.inset * 2), self.height - (self.inset * 2))
      r2.offset = self.offset
      r2.rotation = self.rotation
      r2.pivot = self.pivot
      
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
   d2 = Frame(1000, 500, inset = 20)
   d2.offset = (100, 100)
   print '\Frame(1000, 500, inset = 20)\noffset = (100, 100)'
   print d2.format

   ## displaced and rotated around (0, 0)
   d3 = Frame(1000, 500, inset = 20)
   d3.offset = (100, 100)
   d3.rotation = math.pi / 3.0
   print '\Frame(1000, 500, inset = 20)\noffset = (100, 100)\nrotation = math.pi / 3.0'
   print d3.format

   ## displaced and rotated around (100, 100)
   d4 = Frame(1000, 500, inset = 20)
   d4.offset = (100, 100)
   d4.rotation = math.pi / 3.0
   d4.pivot = (100, 100)
   print '\Frame(1000, 500, inset = 20)\noffset = (100, 100)\nrotation = math.pi / 3.0\npivot = (100, 100)'
   print d4.format

   g1 = Group([d1, d2, d3, d4])
   io.view(g1)
   
   

