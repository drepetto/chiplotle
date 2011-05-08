from chiplotle.geometry.core.group import Group
from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.geometry.core.coordinatearray import CoordinateArray
import copy

class Formation(Group):
   '''A formation is a form of grouping. While a Group is transparent,
   allowing transformations to pass through to affect its underlying
   shapes, a formation shields its underlying shapes so that they are
   not transformed. Instead, only the Formation is transformed.
   Thus, unlike a Group, a Formation has a position attribute.'''

   def __init__(self, shapes=None):
      Group.__init__(self, shapes = shapes)
      self.position = Coordinate(0, 0)

   @property
   def points(self):
      '''Returns a flat list of all the Coordinates that form this shape.
      This property is useful in computing some property of the shape based
      on all it's points. e.g., centroid, bounding box, etc. 
      '''
      coords = [ ]
      for shape in self:
         coords += list(shape.points)
      return CoordinateArray(coords) + self.position


   ## private properties ##

   @property
   def _infix_commands(self):
      result = [ ]
      for shape in self:
         points = copy.copy(shape.points)
         shape.points += self.position
         result += shape._subcommands
         shape.points = points
      return result




## demo
if __name__ == '__main__':
   from chiplotle import *
   import copy

   r1 = rectangle(1000, 1000)
   r2 = rectangle(1000, 1000)
   offset(r2, (2000, 0))
   f1 = Formation([r1, r2])
   offset(f1, (1000, 0))

   r1 = copy.deepcopy(r1)
   r2 = copy.deepcopy(r1)
   offset(r2, (-2000, 0))
   f2 = Formation([r1, r2])
   offset(f2, (-1000, 0))

   c = circle(100)
   g = Group([f1, f2, c])
   rotate(g, 3.1415 / 4, Coordinate(0, 0))

   io.view(g)
