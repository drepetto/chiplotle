from chiplotle.hpgl.coordinatepair import CoordinatePair
from chiplotle.utils.ispair import ispair
import numpy

class CoordinateArray(object):
   def __init__(self, xy=None):
      self.xy = xy


   ## PUBLIC PROPERTIES ##

   @property
   def dtype(self):
      return self._data.dtype

   @apply
   def xy( ):
      def fget(self):
         return self._data
      def fset(self, arg):
         if isinstance(arg, self.__class__):
            self._data = arg._data
            #self._data = arg._data[:] ## copy
         elif isinstance(arg, CoordinatePair):
            self._data = numpy.array([arg.xy]).reshape((-1, 2))
         elif arg is None:
            arg = numpy.array([ ]).reshape((-1, 2))
            self._data = arg
         elif isinstance(arg, (tuple, list, numpy.ndarray)):
            arg = numpy.array(arg).reshape((-1, 2))
            self._data = arg
         else:
            arg = numpy.array([ ]).reshape((-1, 2))
            raise TypeError('unknown type for coordinates xy.')
      return property(**locals( ))

   @apply
   def x( ):
      def fget(self):
         return self._data[:, 0]
      def fset(self, arg):
         self._data[:, 0] = arg
      return property(**locals( ))

   @apply
   def y( ):
      def fget(self):
         return self._data[:, 1]
      def fset(self, arg):
         self._data[:, 1] = arg
      return property(**locals( ))


   ## OVERRIDES ##

   def __len__(self):
      return len(self._data)

   def __setitem__(self, i, arg):
      if isinstance(i, int):
         self._data[i] = arg
      else:
         assert isinstance(arg, (list, tuple, numpy.ndarray))
         self._data[i.start : i.stop] = arg

   def __delitem__(self, i):
      del(self._data[i])

   def __getitem__(self, arg):
      return self._data[arg]

   def __eq__(self, arg):
      arg = CoordinateArray(arg)
      return numpy.all(self._data == arg._data)

   def __ne__(self, arg):
      return not (self == arg)

   def __add__(self, arg):
      if isinstance(arg, CoordinateArray):
         return CoordinateArray(self.xy + arg.xy)
      elif isinstance(arg, CoordinatePair):
         return CoordinateArray(self.xy + arg.xy)
      elif isinstance(arg, (int, long, float)) or ispair(arg):
         return CoordinateArray(self.xy + arg) 
      else:
         raise TypeError
      
   def __radd__(self, arg):
      return self + arg

   def __div__(self, arg):
      if arg == 0:
         raise ZeroDivisionError
      return CoordinateArray(self.xy / arg)

   def __truediv__(self, arg):
      return self / arg

   def __mul__(self, arg):
      if isinstance(arg, (int, long, float)):
         return CoordinateArray(self.xy * arg)
      else:
         raise TypeError
         

   def __repr__(self):
      return 'CoordinateArray(%s)' % self.xy

