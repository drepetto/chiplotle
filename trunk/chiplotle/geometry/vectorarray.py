from chiplotle.geometry.vector import Vector
from chiplotle.core import errors

class VectorArray(object):

   __slots__ = ('_data', )

   def __init__(self, xy=None):
      if xy is None: xy = [ ]

#      ## TODO check and clean up.
#      try:
#         xy = Vector(xy)
#      except errors.InitParameterError:
#         try:
#            xy = list(xy)
#         except:
#            raise errors.InitParameterError
#      if isinstance(xy, Vector):
#         self._data = [xy]
#      else:
#         try:
#            self._data = [Vector(p) for p in xy]
#         except errors.InitParameterError:
#            try:
#               from chiplotle.tools.iterabletools.flat_list_to_pairs \
#                  import flat_list_to_pairs
#               self._data = [Vector(p) for p in flat_list_to_pairs(xy)]
#            except:
#               raise errors.InitParameterError( )

#      if not isinstance(xy, (list, tuple, VectorArray)):
#         raise errors.InitParameterError( )
      try:
         self._data = [Vector(*p) for p in xy]
      except (TypeError, errors.InitParameterError):
         try:
            from chiplotle.tools.iterabletools.flat_list_to_pairs \
               import flat_list_to_pairs
            self._data = [Vector(*p) for p in flat_list_to_pairs(xy)]
         except:
            raise errors.InitParameterError( )


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
#         elif isinstance(arg, Vector):
#            self._data = [arg]
#         elif arg is None:
#            self._data = [ ]
#         elif isinstance(arg, (tuple, list)):
#            self._data = [ ]
#            from chiplotle.tools.iterabletools.is_flat_list import is_flat_list
#            from chiplotle.tools.iterabletools.flat_list_to_pairs import flat_list_to_pairs
#            if len(arg) > 0 and is_flat_list(arg):
#               if isinstance(arg[0], Vector):
#                  self._data.extend(arg)
#               else:
#                  arg = flat_list_to_pairs(arg)
#                  self._data.extend([Vector(e) for e in arg])
#            else:
#               for e in arg:
#                  self._data.append(Vector(e))
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
      '''Converts VectorArray into list of pairs.'''
      return [tuple(cp) for cp in self]


   def append(self, arg):
      self._data.append(Vector(arg))


   def extend(self, arg):
      if isinstance(arg, VectorArray):
         self._data.extend(arg.xy)
      elif isinstance(arg, (list, tuple)):
         for e in arg:
            self.append(e)
      else:
         raise TypeError('`arg` must be a list or VectorArray.')



   ## OVERRIDES ##

   def __len__(self):
      return len(self._data)

   def __repr__(self):
      return 'VectorArray(%s)' % self.xy

   def __str__(self):
      return 'VectorArray(%s)' % ', '.join([str(xy) for xy in self.xy])


   ## accessors / modifiers ##

   #def __iter__(self):
      
   def __delitem__(self, i):
      del(self._data[i])

   def __getitem__(self, arg):
      return self._data[arg]

   def __setitem__(self, i, arg):
      if isinstance(i, int):
         if not isinstance(arg, Vector):
            raise TypeError
         self._data[i] = arg
      else:
         arg = [Vector(xy) for xy in arg]
         self._data[i.start : i.stop] = arg

   ## math ##

   ## addition ##

   def __add__(self, arg):
      if isinstance(arg, (list, tuple)):
         try:
            arg = Vector(arg)
         except errors.InitParameterError:
            try:
               arg = VectorArray(arg)
            except errors.InitParameterError:
               raise errors.OperandError( )

      if isinstance(arg, VectorArray):
         if len(self) == len(arg):
            return VectorArray([a + b for a, b in zip(self.xy, arg.xy)])
         else:
            raise errors.OperandError("VectorArrays must have same length.")
      elif isinstance(arg, (Vector, int, long, float)):
         return VectorArray([val + arg for val in self.xy])
      
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
      return VectorArray([a / arg for a in self.xy])

   def __truediv__(self, arg):
      return self / arg

   def __idiv__(self, arg):
      self._data = (self / arg)._data
      return self

   ## multiplication ##

   def __mul__(self, arg):
      return VectorArray([a * arg for a in self.xy])
   
   def __rmul__(self, arg):
      return self * arg
         
   def __imul__(self, arg):
      self._data = (self * arg)._data
      return self

   ## ## 

   def __eq__(self, arg):
      #arg = VectorArray(arg)
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
      return VectorArray(result)

   def __invert__(self):
      '''Returns the perpendiculars of the Vectors contained in self.'''
      result = [ ]
      for v in self:
         result.append(~v)
      return VectorArray(result)

