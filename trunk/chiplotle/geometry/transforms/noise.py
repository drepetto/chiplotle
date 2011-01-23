from chiplotle.geometry.coordinate import Coordinate
from chiplotle.geometry.coordinatearray import CoordinateArray
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
      result = CoordinateArray([ ])
      for coord in points:
         x_wiggle = random.randrange(-self.xnoise, self.xnoise)
         y_wiggle = random.randrange(-self.ynoise, self.ynoise)
         xy = coord + Coordinate(x_wiggle, y_wiggle)         
         result.append(xy)
      return result



## RUN DEMO CODE
if __name__ == '__main__':
   from chiplotle.geometry.factory.ellipse import ellipse
   from chiplotle.geometry.factory.rectangle import rectangle
   from chiplotle.geometry.shapes.group import Group
   from chiplotle.tools import io
      
   e1 = ellipse(1000,1000)
   r1 = rectangle(1400, 1400)
   n = Noise(20, 40)
   n(e1)
   n(r1)
   g = Group([e1, r1])
   io.view(g)
