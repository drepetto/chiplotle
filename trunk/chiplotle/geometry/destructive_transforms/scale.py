from chiplotle.geometry.shapes.group import Group

def scale(shape, value):
   '''In place scaling.

   - `shape` is the shape to be rotated.
   - `value` is the scaling value. Can be a scalar or an (x, y) vector.
   '''

   if isinstance(shape, Group):
      for s in shape:
         scale(s, value)
   else:
      shape.points = shape.points[0] * value



## RUN DEMO CODE
if __name__ == "__main__":
   from chiplotle.geometry.factory.rectangle import rectangle
   from chiplotle.tools import io
   r1 = rectangle(100, 40)
   r2 = rectangle(100, 40)
   scale(r1, 10)
   scale(r2, (10, 20))
   io.view(Group([r1, r2]))

