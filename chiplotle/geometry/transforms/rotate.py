from chiplotle.geometry.vectorarray import VectorArray
from chiplotle.geometry.vector import Vector
from chiplotle.geometry.transforms._transform import _Transform
from chiplotle.tools.mathtools.rotate_2d import rotate_2d

class Rotate(_Transform):

   def __init__(self, angle, pivot = (0, 0)):
      self.angle = angle
      self.pivot = Vector(pivot)


   ## PUBLIC METHODS ##
   
   def transform(self, points):
      '''Transforms the given points.'''
      result = VectorArray([ ])
      for coord in points:
         xy = rotate_2d(coord, self.angle, self.pivot)
         result.append(xy)
      return result


## RUN DEMO CODE
if __name__ == '__main__':
   from chiplotle.geometry.factory.ellipse import ellipse
   from chiplotle.geometry.factory.rectangle import rectangle
   from chiplotle.geometry.shapes.group import Group
   from chiplotle.tools import io
      
   e1 = ellipse(1000,500)
   r1 = rectangle(1000, 500)
   rot = Rotate(3.14 / 2)
   rot(e1)
   Rotate(3.14 / 3)(r1)
   g1 = Group([e1, r1])
   Rotate(3.14 / 2)(g1)
   io.view(g1)
