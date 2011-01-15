from chiplotle.geometry.shapes.shape import _Shape
from chiplotle.geometry.coordinate import Coordinate
from chiplotle.geometry.coordinatearray import CoordinateArray
from chiplotle.tools.hpgltools.convert_coordinates_to_hpgl_absolute_path \
   import convert_coordinates_to_hpgl_absolute_path
from chiplotle.tools.mathtools.rotate_2d import rotate_2d

class Path(_Shape):
   '''
      A generic path (connected points). 
      This is the most basic concrete drawing class.
   '''
   def __init__(self, points):  
      _Shape.__init__(self)
      self.points = CoordinateArray(points)
      self.closed = False


   ## PUBLIC PROPERTIES ##

   @property
   def points(self):
      return self._points

   @points.setter
   def points(self, arg):
      self._points = CoordinateArray(arg)


   ## PRIVATE PROPERTIES ##

   @property
   def _offset_points(self):
      return self.points + self.offset

   @property
   def _offset_rotated_points(self):
      return rotate_2d(self._offset_points, self.rotation, self.pivot)

   @property
   def _preformat_points(self):
      '''Points (coordinates) ready for formatting (conversion to HPGL).'''
      if self.closed:
         return self._offset_rotated_points + [self._offset_rotated_points[0]]
      else:
         return self._offset_rotated_points

   @property
   def _subcommands(self):
      if _Shape.language == 'HPGL':
         ## create hpgl commands...
         result = convert_coordinates_to_hpgl_absolute_path(self._preformat_points)
      elif _Shape.language == 'gcode':
         ## create gcode
         print 'Sorry, no g-code support!'
      return result 


   ## OVERRIDES ##

   def __getitem__(self, arg):  
      return self.points[arg]

   def __setitem__(self, key, arg):
      self._points[key] = arg

   def __len__(self):
      return len(self.points)

   def __repr__(self):
      return '%s(%s)' % (self.__class__.__name__, self.points)

   def __str__(self):
      return '%s(%d)' % (self.__class__.__name__, len(self))


   ## operators ##

   ## TODO: implement path op path, 
   ## in addition to path op int or path op (x, y)?
   def __add__(self, arg):
      return Path(self.points + arg)

   def __iadd__(self, arg):
      self.points = self.points + arg
      return self

   def __radd__(self, arg):
      return self + arg

   def __mul__(self, arg):
      return Path(self.points * arg)

   def __imul__(self, arg):
      self.points = self.points * arg
      return self

   def __rmul__(self, arg):
      return self * arg

   def __sub__(self, arg):
      return self + (-arg)
   
   def __isub__(self, arg):
      self.points = self.points - arg
      return self

   def __rsub__(self, arg):
      return (-self) + arg


   def __neg__(self):
      return Path(-self.points)



## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.tools import io
   
   p = Path([(1, 2), (4, 6), (0, 2), (5, 1)])
   
   print p.format
   io.view(p)

   ## displaced
