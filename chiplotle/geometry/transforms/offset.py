from chiplotle.geometry.core.group import Group
from chiplotle.geometry.coordinate import Coordinate

def offset(shape, value):
   '''In place offsetting.

   - `shape` is the shape to be rotated.
   - `value` is the offset value. Can be a scalar or an (x, y) coordinate.
   '''

   if isinstance(shape, Group):
      for s in shape:
         offset(s, value)
   else: ## it's a Path...
      if isinstance(value, (list, tuple)):
         value = Coordinate(*value)
      shape.points = shape.points + value



## RUN DEMO CODE
if __name__ == "__main__":
   from chiplotle.geometry.factory.rectangle import rectangle
   from chiplotle.tools import io
   r0 = rectangle(100, 40)
   r1 = rectangle(100, 40)
   r2 = rectangle(100, 40)
   offset(r1, 50)
   offset(r2, (10, 20))
   io.view(Group([r0, r1, r2]))

