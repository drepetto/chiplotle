from chiplotle.geometry.coordinate import Coordinate
from chiplotle.core import errors

class CoordinateArray(object):

   __slots__ = ('_data', )

   def __init__(self, xy=None):
      if xy is None: xy = [ ]

      try:
         self._data = [Coordinate(*p) for p in xy]
      except (TypeError, errors.InitParameterError):
         try:
            from chiplotle.tools.iterabletools.flat_list_to_pairs \
               import flat_list_to_pairs
            self._data = [Coordinate(*p) for p in flat_list_to_pairs(xy)]
         except:
            raise errors.InitParameterError( )


   ## PUBLIC PROPERTIES ##

   @property
   def dtype(self):
      for e in self:
         if isinstance(e.x, (int, long)) and isinstance(e.y, (int, long)):
            return int
      return float


   @property
   def xy(self):
      return self._data

   @property
   def x(self):
      return tuple([xy.x for xy in self._data])

   @property
   def y(self):
      return tuple([xy.y for xy in self._data])

   @property
   def difference(self):
      '''Returns the difference between consecutive elements in `self`.
      i.e., first derivative.
      '''
      result = [ ]
      for i in range(len(self) - 1):
         result.append(self[i+1] - self[i])
      return type(self)(result)


   ## METHODS ##

   def as_list_of_pairs(self):
      '''Converts CoordinateArray into list of pairs.'''
      return [tuple(cp) for cp in self]


   def append(self, arg):
      if not isinstance(arg, Coordinate):
         raise TypeError('arg must be a Coordinate')
      self._data.append(arg)


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
         if not isinstance(arg, Coordinate):
            raise TypeError
         self._data[i] = arg
      else:
         arg = [Coordinate(xy) for xy in arg]
         self._data[i.start : i.stop] = arg

   ## math ##

   ## addition ##

   def __add__(self, arg):
      if isinstance(arg, (list, tuple)):
         try:
            arg = Coordinate(arg)
         except errors.InitParameterError:
            try:
               arg = CoordinateArray(arg)
            except errors.InitParameterError:
               raise errors.OperandError( )

      if isinstance(arg, CoordinateArray):
         if len(self) == len(arg):
            return CoordinateArray([a + b for a, b in zip(self.xy, arg.xy)])
         else:
            raise errors.OperandError("CoordinateArrays must have same length.")
      elif isinstance(arg, (Coordinate, int, long, float)):
         return CoordinateArray([val + arg for val in self.xy])
      
      raise errors.OperandError( )
      

   def __radd__(self, arg):
      return self + arg


   def __iadd__(self, arg):
      self._data = (self + arg)._data
      return self


   ## substraction ##

   def __sub__(self, arg):
      return self + (-arg)
      
   ## division ##

   def __div__(self, arg):
      if arg == 0:
         raise ZeroDivisionError
      return CoordinateArray([a / arg for a in self.xy])

   def __truediv__(self, arg):
      return self / arg

   def __idiv__(self, arg):
      self._data = (self / arg)._data
      return self

   ## multiplication ##

   def __mul__(self, arg):
      return CoordinateArray([a * arg for a in self.xy])
   
   def __rmul__(self, arg):
      return self * arg
         
   def __imul__(self, arg):
      self._data = (self * arg)._data
      return self

   ## ## 

   def __eq__(self, arg):
      #arg = CoordinateArray(arg)
      try:
         return self._data == arg._data
      except AttributeError:
         return False


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

