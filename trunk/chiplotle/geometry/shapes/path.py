from chiplotle.geometry.core.path import Path

def path(points):
   '''A simple path.'''
   return Path(points)



## DEMO CODE
if __name__ == '__main__':
   from chiplotle.tools import io
   points  = [(0, 0), (10, 10), (-10, 10), (-10, -10), (10, -10), (0, 0)]
   p = path(points)
   io.view(p)
