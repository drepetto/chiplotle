from chiplotle.geometry.core.path import Path

def isosceles(width, height):

   tip = (0, height)
   left = (- width / 2.0, 0)
   right = (width / 2.0, 0)

   return Path([tip, left, right, tip])



## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.tools import io
   e = isosceles(10, 20)
   assert isinstance(e, Path)
   print e.format
   io.view(e)
