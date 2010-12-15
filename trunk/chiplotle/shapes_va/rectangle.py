from chiplotle.shapes_va.shape import _Shape
from chiplotle.shapes.polygon import Polygon
from chiplotle.hpgl.coordinatepair import CoordinatePair
from chiplotle.hpgl.coordinatearray import CoordinateArray
from chiplotle.hpgl.commands import PU, PD, PA

class Rectangle(_Shape):
   '''
      A rectangle with a width, height, and offset.

      offset is a CoordinatePair for moving the shape around in 2D space
      rotation is an angle expressed in radians
      pivot is a CoordinatePair indicating the point around which to rotate
      
      The Rectangle is drawn with the current pen location as the center.
      offset may be used to shift this around, for example, to draw from
      the lower, left corner.
   '''

   def __init__(self, width, height, offset=(0, 0), rotation=0, pivot=(0, 0)):  
      self.width = width
      self.height = height
      
      _Shape.__init__(self, offset, rotation, pivot)

   
   @property
   def points(self):
      corners = []
      corners.append(CoordinatePair(-self.width/2, -self.height/2))
      corners.append(CoordinatePair(-self.width/2, self.height/2))
      corners.append(CoordinatePair(self.width/2, self.height/2))
      corners.append(CoordinatePair(self.width/2, -self.height/2))
      corners.append(CoordinatePair(-self.width/2, -self.height/2))
      return [CoordinateArray(corners)]




## RUN DEMO CODE
if __name__ == '__main__':
   from chiplotle.shapes_va.rectangle import Rectangle
   from chiplotle.tools import io
   import math
   p1 = Rectangle(100, 50)
   print '\nRectangle(100, 50)'
   print p1.format

   ## displaced
   p2 = Rectangle(100, 50, (100, 100)) 
   print '\nRectangle(100, 50, (100, 100))'
   print p2.format

   ## displaced and rotated around (0, 0)
   p3 = Rectangle(100, 50, (100, 100), math.pi / 3) 
   print '\nRectangle(100, 50, (100, 100), math.pi / 3)'
   print p3.format

   ## displaced and rotated around (100, 100)
   p4 = Rectangle(100, 50, (100, 100), math.pi / 3, (100, 100)) 
   print '\nRectangle(100, 50, (100, 100), math.pi / 3, (100, 100))'
   print p4.format
