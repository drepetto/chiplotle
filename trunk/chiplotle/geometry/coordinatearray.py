from chiplotle.geometry.coordinate import Coordinate
from chiplotle.core import errors

class CoordinateArray(object):

   __slots__ = ('_data', )

   def __init__(self, xy=None):
      xy = xy or [ ]
      try:
         self._data = [Coordinate(p) for p in xy]
      except errors.InitParameterError:
         from chiplotle.tools.iterabletools.flat_list_to_pairs \
            import flat_list_to_pairs
         self._data = [Coordinate(p) for p in flat_list_to_pairs(xy)]


   ## PUBLIC PROPERTIES ##

   @property
   def dtype(self):
      for e in self:
         if isinstance(e.x, (int, long)) and isinstance(e.y, (int, long)):
            return int
      return float


#   @apply
#   def xy( ):
#      def fget(self):
#         return self._data
#      def fset(self, arg):
#         if isinstance(arg, self.__class__):
#            self._data = arg[:]
#         elif isinstance(arg, Coordinate):
#            self._data = [arg]
#         elif arg is None:
#            self._data = [ ]
#         elif isinstance(arg, (tuple, list)):
#            self._data = [ ]
#            from chiplotle.tools.iterabletools.is_flat_list import is_flat_list
#            from chiplotle.tools.iterabletools.flat_list_to_pairs import flat_list_to_pairs
#            if len(arg) > 0 and is_flat_list(arg):
#               if isinstance(arg[0], Coordinate):
#                  self._data.extend(arg)
#               else:
#                  arg = flat_list_to_pairs(arg)
#                  self._data.extend([Coordinate(e) for e in arg])
#            else:
#               for e in arg:
#                  self._data.append(Coordinate(e))
#         else:
#            raise TypeError('unknown type for coordinates xy.')
#      return property(**locals( ))

   @property
   def xy(self):
      return self._data

   @property
   def x(self):
      return tuple([xy.x for xy in self._data])

   @property
   def y(self):
      return tuple([xy.y for xy in self._data])


   ## METHODS ##

   def as_list_of_pairs(self):
      '''Converts CoordinateArray into list of pairs.'''
      return [tuple(cp) for cp in self]


   def append(self, arg):
      self._data.append(Coordinate(arg))


   def extend(self, arg):
      if isinstance(arg, CoordinateArray):
         self._data.extend(arg.xy)
      elif isinstance(arg, (list, tuple)):
         for e in arg:
            self.append(e)
      else:
         raise TypeError('`arg` must be a list or CoordinateArray.')



   ## OVERRIDES ##

   def __len__(self):
      return len(self._data)

   def __repr__(self):
      return 'CoordinateArray(%s)' % self.xy

   def __str__(self):
      return 'CoordinateArray(%s)' % ', '.join([str(xy) for xy in self.xy])


   ## accessors / modifiers ##

   #def __iter__(self):
      
   def __delitem__(self, i):
      del(self._data[i])

   def __getitem__(self, arg):
      return self._data[arg]

   def __setitem__(self, i, arg):
      if isinstance(i, int):
         self._data[i] = Coordinate(arg)
      else:
         arg = [Coordinate(xy) for xy in arg]
         self._data[i.start : i.stop] = arg

   ## math ##

   ## addition ##

   def __add__(self, arg):
      if isinstance(arg, CoordinateArray):
         if len(self) == len(arg):
            return CoordinateArray([a + b for a, b in zip(self.xy, arg.xy)])
         else:
            raise ValueError("Both CoordinateArrays must be of the same length.")
      else:
         return CoordinateArray([val + arg for val in self.xy])
      
   def __radd__(self, arg):
      return self + arg

   ## division ##

   def __div__(self, arg):
      if arg == 0:
         raise ZeroDivisionError
      return CoordinateArray([a / arg for a in self.xy])

   def __truediv__(self, arg):
      return self / arg

   ## multiplication ##

   def __mul__(self, arg):
      return CoordinateArray([a * arg for a in self.xy])
   
   def __rmul__(self, arg):
      return self * arg
         
   ## substraction ##

   def __sub__(self, arg):
      if isinstance(arg, CoordinateArray):
         if len(self) == len(arg):
            return CoordinateArray([a + b for a, b in zip(self.xy, arg.xy)])
         else:
            raise ValueError("Both CoordinateArrays must be of the same length.")
      else:
         return CoordinateArray([val - arg for val in self.xy])
      
   ## ## 

   def __eq__(self, arg):
      arg = CoordinateArray(arg)
      return self._data == arg._data

   def __ne__(self, arg):
      return not (self == arg)

   def __neg__(self):
      result = [ ]
      for coord in self:
         result.append(-coord)
      return CoordinateArray(result)

   def __invert__(self):
      '''Returns the perpendiculars of the Coordinates contained in self.'''
      result = [ ]
      for v in self:
         result.append(~v)
      return CoordinateArray(result)

