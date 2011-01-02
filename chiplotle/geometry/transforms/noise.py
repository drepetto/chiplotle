from chiplotle.geometry.coordinatearray import CoordinateArray
from chiplotle.geometry.coordinate import Coordinate
from chiplotle.geometry.transforms._transform import _Transform
import random

class Noise(_Transform):

   def __init__(self, xnoise, ynoise):
      self.xnoise = xnoise
      self.ynoise = ynoise


   ## PUBLIC METHODS ##
   
   def transform(self, points):
      '''Transforms the given points.'''
      ## This must be implemented in all geometric transformations.
      result = [ ]
      for coordarray in points:
         ca = CoordinateArray( )
         for coord in coordarray:
            x_wiggle = random.randrange(-self.xnoise, self.xnoise)
            y_wiggle = random.randrange(-self.ynoise, self.ynoise)
            xy = coord + (x_wiggle, y_wiggle)         
            xy_new = Coordinate(xy)
            ca.append(xy_new)
         result.append(ca) 
      return result


   ## OVERRIDES ##

   def __call__(self, shape):
      shape.transforms.append(self)


## RUN DEMO CODE
if __name__ == '__main__':
   from chiplotle.geometry.transforms.noise import Noise
   from chiplotle.geometry.shapes.ellipse import Ellipse
   from chiplotle.geometry.shapes.rectangle import Rectangle
   from chiplotle.geometry.shapes.group import Group
   from chiplotle.tools import io
      
   e1 = Ellipse(1000,1000)
   r1 = Rectangle(1400, 1400)
   n = Noise(10, 30)
   n(e1)
   n(r1)
   g = Group([e1, r1])
   io.view(g)
