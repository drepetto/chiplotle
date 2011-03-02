from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.geometry.core.coordinatearray import CoordinateArray

def get_minmax_coordinates(coords):
   '''Returns the pair of minimum and maximum coordinates of
   the given `coords` list.'''
   
   coords = CoordinateArray(coords)
   if len(coords) == 0:
      return None

   max_x = max(coords.x)
   min_x = min(coords.x)
   max_y = max(coords.y)
   min_y = min(coords.y)
   
   return (Coordinate(min_x, min_y), Coordinate(max_x, max_y))


## DEMO
if __name__ == '__main__':
   from chiplotle.geometry.shapes.circle import circle
   from chiplotle.geometry.shapes.cross import cross
   from chiplotle.geometry.transforms.noise import noise
   from chiplotle.geometry.transforms.offset import offset
   from chiplotle.geometry.core.group import Group
   from chiplotle.tools import io

   c1 = circle(1000)
   noise(c1, 500)
   c2 = circle(2000)
   offset(c2, 3000)
   g = Group([c1, c2])
   ## bounding coords...
   bb = get_minmax_coordinates(g.points)
   cr1 = cross(500, 500)
   offset(cr1, bb[0])
   cr2 = cross(500, 500)
   offset(cr2, bb[1])
   io.view(Group([cr1, cr2, g]))
