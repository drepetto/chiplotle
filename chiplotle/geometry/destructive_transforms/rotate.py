from chiplotle.geometry.coordinate import Coordinate
from chiplotle.geometry.shapes.group import Group
from chiplotle.tools.geometrytools.get_centroid import get_centroid
from chiplotle.tools.iterabletools.flatten import flatten
from chiplotle.tools.mathtools.rotate_2d import rotate_2d


#def rotate(shape, angle, pivot = 'centroid'):
#   if pivot == 'centroid':
#      coords = flatten(list(shape.points))
#      pivot = get_centroid(coords)
#
#   return DestructiveTransform(rotate_2d)(shape, angle, pivot))

def rotate(shape, angle, pivot = 'centroid'):
   '''In place rotation.

   - `shape` is the shape to be rotated.
   - `angle` is the angle (in radians) of rotation.
   - `pivot` is the center of rotation. Can be a string description 
      of the pivot point or a Coordinate. Current supported strings
      is just 'centroid'. This is the default.
   '''

   if pivot == 'centroid':
      coords = flatten(list(shape.points))
      pivot = get_centroid(coords)

   if isinstance(shape, Group):
      for s in shape:
         rotate(s, angle, pivot)
   else: ## it's a Path...
      shape.points = rotate_2d(shape.points, angle, pivot)



## RUN DEMO CODE
if __name__ == "__main__":
   from chiplotle.geometry.factory.rectangle import rectangle
   from chiplotle.tools import io
   r1 = rectangle(100, 40)
   r2 = rectangle(100, 40)
   r3 = rectangle(200, 200)
   rotate(r1, 3.14 / 4)
   rotate(r2, 3.14 / 4, (100, 100))
   io.view(Group([r1, r2, r3]))
