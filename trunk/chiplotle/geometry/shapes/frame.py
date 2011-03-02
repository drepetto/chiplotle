from chiplotle.geometry.shapes.rectangle import rectangle
from chiplotle.geometry.core.group import Group

def frame(width, height, inset):
   '''A frame (rectangle within a rectangle) with a width, height, and inset.

   - `width` is the width of the frame.
   - `height` is the height of the frame.
   - `inset` is the distance to inset the inner rectangle from the outer.
   '''

   r1 = rectangle(width, height)
   r2 = rectangle(width - (inset * 2), height - (inset * 2))
   return Group([r1, r2])



## RUN DEMO CODE
if __name__ == '__main__':
   from chiplotle.tools import io

   f1 = frame(1000, 500, inset = 20)
   io.view(f1)
