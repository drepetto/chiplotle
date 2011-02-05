from chiplotle.geometry.coordinate import Coordinate
from chiplotle.geometry.coordinatearray import CoordinateArray
#import sys

def get_bounding_coordinate_pairs(shape):
   '''Returns the pair of coordinate pairs outlining the bounding box of
   the given `shape`, or None if `shape` is empty.'''
   
   ## TODO add type checking?

   coords = CoordinateArray(shape.points)

   if len(coords) == 0:
      return None

   max_x = max(coords.x)
   min_x = min(coords.x)
   max_y = max(coords.y)
   min_y = min(coords.y)
   

#   min_x = min_y = sys.maxint
#   max_x = max_y = -sys.maxint
#   
#   coords = shape.points
#
#   if len(coords) == 0:
#      return None
#
#   for c in coords:
#      ## x...
#      if c.x > max_x:
#         max_x = c.x
#      if c.x < min_x:
#         min_x = c.x
#      ## y...
#      if c.y > max_y:
#         max_y = c.y
#      if c.y < min_y:
#         min_y = c.y

   return (Coordinate(min_x, min_y), Coordinate(max_x, max_y))


## DEMO
if __name__ == '__main__':
   from chiplotle.geometry.factory.circle import circle
   from chiplotle.geometry.factory.cross import cross
   from chiplotle.geometry.transforms.noise import noise
   from chiplotle.geometry.transforms.offset import offset
   from chiplotle.geometry.shapes.group import Group
   from chiplotle.tools import io

   #c = noise(circle(100), 20)
   c1 = circle(1000)
   noise(c1, 500)
   c2 = circle(2000)
   offset(c2, 3000)
   g = Group([c1, c2])
   ## bounding coords...
   bb = get_bounding_coordinate_pairs(g)
   cr1 = cross(500, 500)
   offset(cr1, bb[0])
   cr2 = cross(500, 500)
   offset(cr2, bb[1])
   io.view(Group([cr1, cr2, g]))
