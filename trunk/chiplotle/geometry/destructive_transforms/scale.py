from chiplotle.geometry.shapes.group import Group
from chiplotle.geometry.coordinate import Coordinate

def scale(shape, value, pivot = Coordinate(0, 0)):
   '''In place scaling.

   - `shape` is the shape to be rotated.
   - `value` is the scaling value. Can be a scalar or an (x, y) coordinate.
   - `pivot` is the Coordinate around which the shape will be scaled.
   '''

   try: ## if it's a tuple, convert to Coordinate...
      ## NOTE Coordinate is a poor name for this, Vector is a more general 
      ## notion and thus more appropriate here.
      value = Coordinate(*value)
   except TypeError:
      pass

   pivot = Coordinate(*pivot)

   if isinstance(shape, Group):
      for s in shape:
         scale(s, value, pivot)
   else: ## it's a Path...
      ## TODO use matrices to make this more efficient? 
      if pivot == Coordinate(0, 0):
         shape.points = shape.points * value
      else:
         offset_points = shape.points - pivot
         scaled_points = offset_points * value
         shape.points = scaled_points + pivot



## RUN DEMO CODE
if __name__ == "__main__":
   from chiplotle.geometry.factory.rectangle import rectangle
   from chiplotle.tools import io
   r1 = rectangle(100, 40)
   r2 = rectangle(100, 40)
   scale(r1, 10, (50, 50))
   scale(r2, (10, 20))
   io.view(Group([r1, r2]))

