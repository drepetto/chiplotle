from chiplotle.geometry.shapes.path import Path

def rectangle(width, height):
   corners = []
   corners.append((-width / 2.0, -height / 2.0))
   corners.append((-width / 2.0, height / 2.0))
   corners.append((width / 2.0, height / 2.0))
   corners.append((width / 2.0, -height / 2.0))
   corners.append((-width / 2.0, -height / 2.0))
   return Path(corners)



## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.tools import io
   e = rectangle(10, 20)
   assert isinstance(e, Path)
   print e.format
   io.view(e)
