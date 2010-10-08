from chiplotle.hpgl.coordinatepair import CoordinatePair

class CoordinateArray(object):

   __slots__ = ('_data', )

   def __init__(self, xy=None):
      self.xy = xy

   @property
   def dtype(self):
      for e in self:
         if isinstance(e.x, (int, long)) and isinstance(e.y, (int, long)):
            return int
      return float

   ## TODO: very messy. fix.
   @apply
   def xy( ):
      def fget(self):
         return self._data
      def fset(self, arg):
         if isinstance(arg, self.__class__):
            self._data = arg._data[:]
         elif isinstance(arg, CoordinatePair):
            self._data = [arg]
         elif arg is None:
            self._data = [ ]
         elif isinstance(arg, (tuple, list)):
            self._data = [ ]
            from chiplotle.tools.iterabletools.is_flat_list import is_flat_list
            from chiplotle.tools.iterabletools.flat_list_to_pairs import flat_list_to_pairs
            if len(arg) > 0 and is_flat_list(arg):
               if isinstance(arg[0], CoordinatePair):
                  self._data.extend(arg)
               else:
                  arg = flat_list_to_pairs(arg)
                  self._data.extend([CoordinatePair(e) for e in arg])
            else:
               for e in arg:
                  self._data.append(CoordinatePair(e))
         else:
            raise TypeError('unknown type for coordinates xy.')
      return property(**locals( ))


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


   ## OVERRIDES ##

   def __len__(self):
      return len(self._data)

   def __setitem__(self, i, arg):
      ## TODO: check type?
      if isinstance(i, int):
         self._data[i] = arg
      else:
         assert isinstance(arg, (list, tuple))
         self._data[i.start : i.stop] = arg

   def __delitem__(self, i):
      del(self._data[i])

   def __getitem__(self, arg):
      return self._data[arg]

   def __eq__(self, arg):
      arg = CoordinateArray(arg)
      return self._data == arg._data

   def __ne__(self, arg):
      return not (self == arg)

   def __add__(self, arg):
      if isinstance(arg, (int, long, float, CoordinatePair)):
         return CoordinateArray([a + arg for a in self.xy]) 
      elif isinstance(arg, CoordinateArray):
         if len(self) == len(arg):
            return CoordinateArray([a + b for a, b in zip(self.xy, arg.xy)])
         else:
            raise ValueError("Both CoordinateArrays must be of the same length.")
      elif isinstance(arg, (list, tuple)) and len(arg) == 2:
         arg = CoordinatePair(arg)
         return CoordinateArray([a + arg for a in self.xy])
      else:
         raise TypeError
      
   def __radd__(self, arg):
      return self + arg

   def __div__(self, arg):
      if arg == 0:
         raise ZeroDivisionError
      return CoordinateArray([a / arg for a in self.xy])

   def __sub__(self, arg):
      from chiplotle.tools.iterabletools.ispair import ispair
      if isinstance(arg, CoordinateArray):
         return CoordinateArray([a - b for a, b in zip(self.xy, arg.xy)])
      elif isinstance(arg, (int, long, float, CoordinatePair)) or ispair(arg):
         return CoordinateArray([a - arg for a in self.xy]) 
      else:
         raise TypeError
      

   def __truediv__(self, arg):
      return self / arg

   def __mul__(self, arg):
      if isinstance(arg, (int, long, float)):
         return CoordinateArray([a * arg for a in self.xy])
      else:
         raise TypeError
         
   def __repr__(self):
      return 'CA(%s)' % self.xy

   def __str__(self):
      return 'CA(%s)' % self.xy



## TODO: add list-like methods (append, extend, etc)


##################################

#class CoordinateArray(object):
#   def __init__(self, xy=None):
#      self.xy = xy
#
#
#   ## PUBLIC PROPERTIES ##
#
#   @property
#   def dtype(self):
#      return self._data.dtype
#
#   @apply
#   def xy( ):
#      def fget(self):
#         return self._data
#      def fset(self, arg):
#         if isinstance(arg, self.__class__):
#            self._data = arg._data
#            #self._data = arg._data[:] ## copy
#         elif isinstance(arg, CoordinatePair):
#            self._data = numpy.array([arg.xy]).reshape((-1, 2))
#         elif arg is None:
#            arg = numpy.array([ ]).reshape((-1, 2))
#            self._data = arg
#         elif isinstance(arg, (tuple, list, numpy.ndarray)):
#            arg = numpy.array(arg).reshape((-1, 2))
#            self._data = arg
#         else:
#            arg = numpy.array([ ]).reshape((-1, 2))
#            raise TypeError('unknown type for coordinates xy.')
#      return property(**locals( ))
#
#   @apply
#   def x( ):
#      def fget(self):
#         return self._data[:, 0]
#      def fset(self, arg):
#         self._data[:, 0] = arg
#      return property(**locals( ))
#
#   @apply
#   def y( ):
#      def fget(self):
#         return self._data[:, 1]
#      def fset(self, arg):
#         self._data[:, 1] = arg
#      return property(**locals( ))
#
#
#   ## OVERRIDES ##
#
#   def __len__(self):
#      return len(self._data)
#
#   def __setitem__(self, i, arg):
#      if isinstance(i, int):
#         self._data[i] = arg
#      else:
#         assert isinstance(arg, (list, tuple, numpy.ndarray))
#         self._data[i.start : i.stop] = arg
#
#   def __delitem__(self, i):
#      del(self._data[i])
#
#   def __getitem__(self, arg):
#      return self._data[arg]
#
#   def __eq__(self, arg):
#      arg = CoordinateArray(arg)
#      return numpy.all(self._data == arg._data)
#
#   def __ne__(self, arg):
#      return not (self == arg)
#
#   def __add__(self, arg):
#      if isinstance(arg, CoordinateArray):
#         return CoordinateArray(self.xy + arg.xy)
#      elif isinstance(arg, CoordinatePair):
#         return CoordinateArray(self.xy + arg.xy)
#      elif isinstance(arg, (int, long, float)) or ispair(arg):
#         return CoordinateArray(self.xy + arg) 
#      else:
#         raise TypeError
#      
#   def __radd__(self, arg):
#      return self + arg
#
#   def __div__(self, arg):
#      if arg == 0:
#         raise ZeroDivisionError
#      return CoordinateArray(self.xy / arg)
#
#   def __truediv__(self, arg):
#      return self / arg
#
#   def __mul__(self, arg):
#      if isinstance(arg, (int, long, float)):
#         return CoordinateArray(self.xy * arg)
#      else:
#         raise TypeError
#         
#
#   def __repr__(self):
#      return 'CoordinateArray(%s)' % self.xy
#
