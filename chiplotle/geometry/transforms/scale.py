from chiplotle.geometry.core.group import Group
from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.geometry.transforms.transformvisitor import TransformVisitor

def scale(shape, value, pivot = Coordinate(0, 0)):
   '''In place scaling.

   - `shape` is the shape to be rotated.
   - `value` is the scaling value. Can be a scalar or an (x, y) coordinate.
   - `pivot` is the Coordinate around which the shape will be scaled.
   '''
   pivot = Coordinate(*pivot)
   try: 
      ## if it's a tuple, convert to Coordinate...
      ## NOTE Coordinate is a bad name for this, Vector is a more general 
      ## notion and thus more appropriate here.
      value = Coordinate(*value)
   except TypeError:
      pass

   def scl(coords, value, pivot):
      ## TODO use matrices to make this more efficient? 
      if pivot == Coordinate(0, 0):
         coords *= value
      else:
         offset_points = coords - pivot
         scaled_points = offset_points * value
         coords = scaled_points + pivot
      return coords

   t = TransformVisitor(scl)
   t.visit(shape, value, pivot)



## RUN DEMO CODE
if __name__ == "__main__":
   from chiplotle.geometry.shapes.rectangle import rectangle
   from chiplotle.tools import io
   r0 = rectangle(1000, 500)
   r1 = rectangle(1000, 500)
   r2 = rectangle(1000, 500)
   scale(r1, 5, (500, 250))
   scale(r2, (10, 20))
   g = Group([r0, r1, r2])
   print g.format
   io.view(g)

