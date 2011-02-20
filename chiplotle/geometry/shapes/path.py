from chiplotle.geometry.shapes.shape import _Shape
#from chiplotle.geometry.coordinate import Coordinate
from chiplotle.geometry.coordinatearray import CoordinateArray
from chiplotle.tools.hpgltools.convert_coordinates_to_hpgl_absolute_path \
   import convert_coordinates_to_hpgl_absolute_path
#from chiplotle.tools.mathtools.rotate_2d import rotate_2d
from chiplotle.core import errors

## TODO: add a LineFormatter (or Formatter) class that can be pluged-in to 
## change the formatting of the line? e.g., dotted, solid, points, etc.

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
   ## FIXME should this be settable? Probably not...
   @points.setter
   def points(self, arg):
      self._points = CoordinateArray(arg)


   ## PRIVATE PROPERTIES ##

   @property
   def _preformat_points(self):
      '''Points (coordinates) ready for formatting (conversion to HPGL).'''
      if self.closed:
         #tp = self._transformed_points
         tp = self.points
         tp.append(tp[0])
         return tp
      else:
         #return self._transformed_points
         return self.points

   @property
   def _infix_commands(self):
      if _Shape.language == 'HPGL':
         ## create hpgl commands...
         #print self._preformat_points
         return convert_coordinates_to_hpgl_absolute_path(self._preformat_points)
      elif _Shape.language == 'gcode':
         ## create gcode
         print 'Sorry, no g-code support!'


   ## OVERRIDES ##

#   def __getitem__(self, arg):  
#      return self.points[arg]
#
#   def __setitem__(self, key, arg):
#      self._points[key] = arg

   def __len__(self):
      return len(self.points)

   def __repr__(self):
      return '%s(%s)' % (self.__class__.__name__, self.points)

   def __str__(self):
      return '%s(%d)' % (self.__class__.__name__, len(self))


   ## operators ##
   ## some are destructive transformations ##

   ## TODO: return a copy of self rather than a fresh new instance?
   ## i.e., do we want to preserve whatever other attributes self has?
   def __add__(self, arg):
      return Path(self.points + arg)

   def __iadd__(self, arg):
      self.points = self.points + arg
      return self

   def __radd__(self, arg):
      return self.__add__(arg)

   def __mul__(self, arg):
      try:
         return Path(self.points * arg)
      except errors.InitParameterError:
         raise errors.OperandError( )

   def __imul__(self, arg):
      self.points = self.points * arg
      return self

   def __rmul__(self, arg):
      return self * arg

   def __sub__(self, arg):
      try:
         return self + (-arg)
      except:
         raise errors.OperandError( )
   
   def __isub__(self, arg):
      self.points = self.points - arg
      return self

   def __rsub__(self, arg):
      return -(self - arg)


   def __eq__(self, arg):
      try:
         return self.points == arg.points
      except AttributeError:
         return False

   def __ne__(self, arg):
      return not (self == arg)

   def __neg__(self):
      return Path(-self.points)



## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.tools import io
   
   p = Path([(1, 2), (4, 6), (0, 2), (5, 1)])
   io.view(p)

