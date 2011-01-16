from chiplotle.geometry.coordinatearray import CoordinateArray
from chiplotle.geometry.transforms._transform import _Transform

class Scale(_Transform):

   def __init__(self, *arg):
      if len(arg) == 2:
         self.xscale = arg[0]
         self.yscale = arg[1]
      else:
         try:
            self.xscale = arg[0][0]
            self.yscale = arg[0][1]
         except TypeError:
            self.xscale = arg[0]
            self.yscale = arg[0]


   ## PUBLIC METHODS ##
   
   def transform(self, points):
      '''Transforms the given points.'''
      result = CoordinateArray([ ])
      for coord in points:
         xy = coord * (self.xscale, self.yscale)         
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
   s = Scale(2, 3)
   s(e1)
   Scale(3)(r1)
   g1 = Group([e1, r1])
   g2 = Group([e1, e2])
   Scale(2)(g2)
   io.view(Group([g1, g2]))
