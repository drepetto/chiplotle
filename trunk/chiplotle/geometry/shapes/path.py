from chiplotle.geometry.shapes.shape import _Shape
from chiplotle.geometry.coordinate import Coordinate
from chiplotle.geometry.coordinatearray import CoordinateArray

class Path(_Shape):
   '''
      A generic path (connected points). 
      This is the most basic concrete drawing class.
   '''
   def __init__(self, points):  
      _Shape.__init__(self)
      self.points = CoordinateArray(points)

   ## PUBLIC PROPERTIES ##

#   @apply
#   def coords( ):
#      def fget(self):  
#         return self._coords
#      def fset(self, arg):
#         self._coords = CoordinateArray(arg)
#      return property(**locals( ))

   @property
   def points(self):
      return [self._points]

   @points.setter
   def points(self, arg):
      self._points = CoordinateArray(arg)


## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.tools import io
   
   p = Path([(1, 2), (4, 6), (0, 2), (5, 1)])
   
   print p.format
   io.view(p)

   ## displaced
