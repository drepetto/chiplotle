from chiplotle.geometry.shapes.shape import _Shape
from chiplotle.geometry.coordinate import Coordinate
from chiplotle.geometry.coordinatearray import CoordinateArray

class Rectangle(_Shape):
   '''
      A rectangle with a width and height.

      offset is a Coordinate for moving the shape around in 2D space
      rotation is an angle expressed in radians
      pivot is a Coordinate indicating the point around which to rotate
      
      The Rectangle is drawn with the current pen location as the center.
      offset may be used to shift this around, for example, to draw from
      the lower, left corner.
   '''

   def __init__(self, width, height):  
      self.width = width
      self.height = height
      
      _Shape.__init__(self)

   
   @property
   def points(self):
      corners = []
      corners.append(Coordinate(-self.width/2, -self.height/2))
      corners.append(Coordinate(-self.width/2, self.height/2))
      corners.append(Coordinate(self.width/2, self.height/2))
      corners.append(Coordinate(self.width/2, -self.height/2))
      corners.append(Coordinate(-self.width/2, -self.height/2))
      return [CoordinateArray(corners)]




## RUN DEMO CODE
if __name__ == '__main__':
   from chiplotle.geometry.shapes.rectangle import Rectangle
   from chiplotle.geometry.shapes.group import Group
   from chiplotle.tools import io
   import math
   p1 = Rectangle(100, 50)
   print '\nRectangle(100, 50)'
   print p1.format

   ## displaced
   p2 = Rectangle(100, 50)
   p2.offset = (100,100)
   print '\nRectangle(100, 50)\noffset = (100,100)'
   print p2.format

   ## displaced and rotated around (0, 0)
   p3 = Rectangle(100, 50)
   p3.offset = (100, 100)
   p3.rotation = math.pi / 3.0
   print '\nRectangle(100, 50)\noffset = (100, 100)\nrotation = math.pi / 3'
   print p3.format

   ## displaced and rotated around (100, 100)
   p4 = Rectangle(100, 50)
   p4.offset = (100, 100)
   p4.rotation = math.pi / 3.0
   p4.pivot = (100, 100)
   print '\nRectangle(100, 50)\noffset = (100, 100)\nrotation = math.pi / 3\npivot = (100, 100)'
   print p4.format

   g1 = Group([p1, p2, p3, p4])
   io.view(g1)
   