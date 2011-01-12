from chiplotle.geometry.coordinatearray import CoordinateArray
from chiplotle.geometry.coordinate import Coordinate
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
      result = [ ]
      for coordarray in points:
         ca = CoordinateArray( )
         for coord in coordarray:
            xy = coord * (self.xscale, self.yscale)         
            ca.append(xy)
         result.append(ca) 
      return result


## RUN DEMO CODE
if __name__ == '__main__':
   from chiplotle.geometry.transforms.scale import Scale
   from chiplotle.geometry.shapes.ellipse import Ellipse
   from chiplotle.geometry.shapes.rectangle import Rectangle
   from chiplotle.geometry.shapes.group import Group
   from chiplotle.tools import io
      
   e1 = Ellipse(1000,1000)
   r1 = Rectangle(1000, 1000)
   s = Scale(2, 3)
   s(e1)
   Scale(3)(r1)
   g = Group([e1, r1])
   io.view(g)
