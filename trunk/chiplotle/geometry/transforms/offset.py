from chiplotle.geometry.coordinatearray import CoordinateArray
from chiplotle.geometry.coordinate import Coordinate
from chiplotle.geometry.transforms._transform import _Transform

class Offset(_Transform):

   def __init__(self, *arg):
      if len(arg) > 2:
         raise TypeError('at most two arguments are allowed.')
      if len(arg) == 2:
         self.xoffset = arg[0]
         self.yoffset = arg[1]
      else:
         try:
            self.xoffset = arg[0][0]
            self.yoffset = arg[0][1]
         except TypeError:
            self.xoffset = arg[0]
            self.yoffset = arg[0]


   ## PUBLIC METHODS ##
   
   def transform(self, points):
      '''Transforms the given points.'''
      result = CoordinateArray([ ])
      for coord in points:
         xy = coord + Coordinate(self.xoffset, self.yoffset)
         result.append(xy)
      return result


## RUN DEMO CODE
if __name__ == '__main__':
   from chiplotle.geometry.factory.ellipse import ellipse
   from chiplotle.geometry.factory.rectangle import rectangle
   from chiplotle.geometry.shapes.group import Group
   from chiplotle.tools import io
      
   e1 = ellipse(1000,1000)
   e2 = ellipse(1000,1000)
   r1 = rectangle(1000, 1000)
   os = Offset(200, 300)
   os(e1)
   Offset(800)(r1)
   g1 = Group([e1, r1])
   g2 = Group([e1, e2])
   Offset(1200)(g2)
   io.view(Group([g1, g2]))
