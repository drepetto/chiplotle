from chiplotle.geometry.factory.rectangle import rectangle

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
   from chiplotle.geometry.shapes.group import *
   import math

   f1 = frame(1000, 500, inset = 20)

   ## displaced
   f2 = frame(1000, 500, inset = 20)
   f2.offset = (100, 100)

   ## displaced and rotated around (0, 0)
   f3 = frame(1000, 500, inset = 20)
   f3.offset = (100, 100)
   f3.rotation = math.pi / 3.0

   ## displaced and rotated around (100, 100)
   f4 = frame(1000, 500, inset = 20)
   f4.offset = (100, 100)
   f4.rotation = math.pi / 3.0
   f4.pivot = (100, 100)

   g1 = Group([f1, f2, f3, f4])
   io.view(g1)
