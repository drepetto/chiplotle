from chiplotle.geometry.shapes.ellipse import ellipse

def circle(radius, segments = 36):
   return ellipse(radius * 2, radius * 2, segments)


## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.tools import io
   from chiplotle.geometry.core.path import Path
   e = circle(10)
   assert isinstance(e, Path)
   print e.format
   io.view(e)
