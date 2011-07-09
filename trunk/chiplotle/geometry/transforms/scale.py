from chiplotle.geometry.core.group import Group
from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.geometry.transforms.transformvisitor import TransformVisitor

def scale(shape, value, pivot = Coordinate(0, 0)):
   '''In place scaling.

   - `shape` is the shape to be rotated.
   - `value` is the scaling value. Can be a scalar or an (x, y) coordinate.
   - `pivot` is the Coordinate around which the shape will be scaled.
   '''
   from chiplotle.tools.geometrytools.scale import scale 
   t = TransformVisitor(scale)
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

