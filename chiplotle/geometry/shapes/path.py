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

   @property
   def points(self):
      return [self._points]

   @points.setter
   def points(self, arg):
      self._points = CoordinateArray(arg)


   ## OVERRIDES ##

   def __getitem__(self, arg):  
      return self.points[0][arg]

   def __setitem__(self, key, arg):
      self._points[key] = arg

   def __len__(self):
      return len(self.points[0])

   def __repr__(self):
      return '%s(%s)' % (self.__class__.__name__, self.points[0])

   def __str__(self):
      return '%s(%d)' % (self.__class__.__name__, len(self))


   ## operators ##

   ## TODO: implement path op path, 
   ## in addition to path op int or path op (x, y)?
   def __add__(self, arg):
      return Path(self.points[0] + arg)

   def __iadd__(self, arg):
      self.points = self.points[0] + arg
      return self

   def __radd__(self, arg):
      return self + arg

   def __mul__(self, arg):
      return Path(self.points[0] * arg)

   def __imul__(self, arg):
      self.points = self.points[0] * arg
      return self

   def __rmul__(self, arg):
      return self * arg

   def __sub__(self, arg):
      return self + (-arg)
   
   def __isub__(self, arg):
      self.points = self.points[0] - arg
      return self

   def __rsub__(self, arg):
      return (-self) + arg


   def __neg__(self):
      return Path(-self.points[0])



## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.tools import io
   
   p = Path([(1, 2), (4, 6), (0, 2), (5, 1)])
   
   print p.format
   io.view(p)

   ## displaced
