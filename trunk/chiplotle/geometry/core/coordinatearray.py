from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.geometry.core.coordinatearraypropertiesmixin import \
   CoordinateArrayPropertiesMixin
import numpy as np

class CoordinateArray(CoordinateArrayPropertiesMixin):

   __slots__ = ('_data', )

   def __init__(self, coords=None):
      '''`coords` is a list of Coordinate objs or iterables.'''
      if coords is None: 
         coords = [ ]
      self._data = [Coordinate(*list(p)) for p in coords]


   ## PUBLIC PROPERTIES ##

   @property
   def ndim(self):
      return len(self._data[0]) if self._data else None

   @property
   def dtype(self):
      coords = [list(c) for c in self._data]
      return np.array(coords).dtype

   @property
   def coords(self):
      return np.array(self._data).transpose().tolist()

   @property
   def x(self):
      return tuple(self.coords[0] if self.coords else ())

   @property
   def y(self):
      return tuple(self.coords[1] if self.coords else ())


   ## METHODS ##

   def append(self, arg):
      if not isinstance(arg, Coordinate):
         raise TypeError('arg must be a Coordinate')
      self._data.append(arg)


   def extend(self, arg):
      if isinstance(arg, CoordinateArray):
         self._data.extend(arg._data)
      elif isinstance(arg, (list, tuple)):
         for e in arg:
            self.append(e)
      else:
         raise TypeError('`arg` must be a list or CoordinateArray.')


   ## OVERRIDES ##

   def __len__(self):
      return len(self._data)

   def __repr__(self):
      return 'CoordinateArray(%s)' % self._data

   def __str__(self):
      return 'CoordinateArray(%s)' % ', '.join([str(coord) for coord in self._data])


   ## accessors / modifiers ##

   def __iter__(self):
      for c in self._data:
         yield c
      
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
         arg = [Coordinate(*list(coord)) for coord in arg]
         self._data[i.start : i.stop] = arg

   ## math ##

   ## addition ##

   def __add__(self, arg):
      if isinstance(arg, Coordinate):
         return CoordinateArray([coord + arg for coord in self._data])
      if isinstance(arg, CoordinateArray):
         if len(self) != len(arg):
            raise ValueError("CoordinateArrays must have same length.")
         coords = [a + b for a, b in zip(self._data, arg._data)]
         return CoordinateArray(coords)
      raise TypeError('Unknown type for CoordinateArray addition')
      
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
      return CoordinateArray([a / arg for a in self._data])

   def __truediv__(self, arg):
      return self / arg

   def __idiv__(self, arg):
      self._data = (self / arg)._data
      return self

   ## multiplication ##

   def __mul__(self, arg):
      return CoordinateArray([a * arg for a in self._data])
   
   def __rmul__(self, arg):
      return self * arg
         
   def __imul__(self, arg):
      self._data = (self * arg)._data
      return self

   ## ## 

   def __eq__(self, arg):
      try:
         return self._data == arg._data
      except AttributeError:
         return False


   def __ne__(self, arg):
      return not (self == arg)

   def __neg__(self):
      return CoordinateArray([-c  for c in self])

   def __invert__(self):
      '''Returns the perpendiculars of the Coordinates contained in self.'''
      if self.ndim != 2:
         raise ValueError('inversion only works on 2D currently.')
      return CoordinateArray([~v for v in self])


if __name__ == '__main__':
   ca = CoordinateArray([(1, 2), (3, 4)])
   print ca
   print ca.coords
   print ca.x
   print ca.y
