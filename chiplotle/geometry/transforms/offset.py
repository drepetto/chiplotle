from chiplotle.geometry.core.group import Group
from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.geometry.transforms.transformvisitor import TransformVisitor

def offset(shape, value):
   '''In place offsetting.

   - `shape` is the shape to be rotated.
   - `value` is the offset value. Can be a scalar or an (x, y) coordinate.
   '''
   if isinstance(value, (list, tuple)):
      value = Coordinate(*value)

   def offset(coords, value):
      return coords + value

   t = TransformVisitor(offset)
   t.visit(shape, value)


## RUN DEMO CODE
if __name__ == "__main__":
   from chiplotle.geometry.shapes.rectangle import rectangle
   from chiplotle.tools import io
   r0 = rectangle(1000, 400)
   r1 = rectangle(1000, 400)
   r2 = rectangle(1000, 400)
   offset(r1, (0, 1500))
   offset(r2, (100, 200))
   io.view(Group([r0, r1, r2]))

