from chiplotle.geometry.core.polygon import Polygon

def rectangle(width, height):
   corners = []
   corners.append((-width / 2.0, -height / 2.0))
   corners.append((-width / 2.0, height / 2.0))
   corners.append((width / 2.0, height / 2.0))
   corners.append((width / 2.0, -height / 2.0))
   corners.append((-width / 2.0, -height / 2.0))
   return Polygon(corners)



## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.tools import io
   e = rectangle(100, 200)
   e.filled = True
   assert isinstance(e, Polygon)
   print e.format
   io.view(e)
