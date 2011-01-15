from chiplotle.tools.mathtools.rotate_2d import rotate_2d
from chiplotle.geometry.shapes.group import Group

def rotate(shape, angle, pivot = (0, 0)):
   '''In place rotation.

   - `shape` is the shape to be rotated.
   - `angle` is the angle (in radians) of rotation.
   - `pivot` is an coordinate tuple used as center of rotation; 
      default is (0, 0).
   '''

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
   rotate(r1, 3.14 / 4)
   rotate(r2, 3.14 / 4, (100, 100))
   io.view(Group([r1, r2]))
