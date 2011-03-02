from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.geometry.core.path import Path
from chiplotle.geometry.core.group import Group

def cross(width, height):
   '''Draws a cross shape.
   
   - `width` is the length of the horizontal line.
   - `height` is the length of the vertical line..
   '''
   
   l1 = Path([Coordinate(-width / 2.0, 0), Coordinate(width / 2.0, 0)])
   l2 = Path([Coordinate(0, -height / 2.0), Coordinate(0, height / 2.0)])
   return Group([l1, l2])


## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.tools import io
   from chiplotle.geometry.core.path import Path
   e = cross(100, 200)
   print e.format
   io.view(e)
