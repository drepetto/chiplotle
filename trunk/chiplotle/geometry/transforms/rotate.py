from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.geometry.core.group import Group
from chiplotle.tools.mathtools.rotate_2d import rotate_2d
from chiplotle.geometry.transforms.transformvisitor import TransformVisitor

def rotate(shape, angle, pivot = (0, 0)):
   '''In place rotation.

   - `shape` is the shape to be rotated.
   - `angle` is the angle (in radians) of rotation.
   - `pivot` is the center of rotation. Must be a Coordinate or (x, y) pair.
   '''
   def rotate(coords, angle, pivot = pivot):
      return rotate_2d(coords, angle, pivot)

   t = TransformVisitor(rotate)
   t.visit(shape, angle, pivot)



## RUN DEMO CODE
if __name__ == "__main__":
   from chiplotle.geometry.shapes.rectangle import rectangle
   from chiplotle.tools import io
   r1 = rectangle(1000, 400)
   r2 = rectangle(1000, 400)
   r3 = rectangle(2000, 900)
   rotate(r1, 3.14 / 4)
   rotate(r2, 3.14 / 4, (500, 500))
   io.view(Group([r1, r2, r3]))
