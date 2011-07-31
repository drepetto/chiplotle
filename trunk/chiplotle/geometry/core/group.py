from chiplotle.geometry.core.coordinatearray import CoordinateArray
from chiplotle.geometry.core.shape import _Shape
import copy

class Group(_Shape):
   '''A group collects together multiple _Shapes, so they
   can be treated as a single object. 
   The elements in a group are stored in order, like a list, so that
   order-specific operation can be performed on groups. 
   i.e., Groups are lists, not sets.
   '''
   def __init__(self, shapes=None):
      _Shape.__init__(self)
      self._shapes = [ ]
      if shapes is None: shapes = [ ]
      self.extend(shapes)


   ## PUBLIC PROPERTIES ##

   @property
   def points(self):
      '''Returns a flat list of all the Coordinates that form this shape.
      This property is useful in computing some property of the shape based
      on all it's points. e.g., centroid, bounding box, etc. '''
      coords = [ ]
      for shape in self:
         coords += list(shape.points)
      return CoordinateArray(coords)
      #return coords


   ## PUBLIC METHODS ##

   def append(self, arg):
      self._check_init_shape(arg)
      self._shapes.append(arg)

   def extend(self, arg):
      self._check_init_shapes(arg)
      self._shapes.extend(arg)

   def insert(self, i, arg):
      self._check_init_shape(arg)
      self._shapes.insert(i, arg)

   def remove(self, arg):
      self._shapes.remove(arg)

   def pop(self, indx=-1):
      result = self._shapes.pop(indx)
      return result


   ## private properties ##

#   @property
#   def _infix_commands(self):
#      result = [ ]
#      for shape in self:
#         result += shape._subcommands
#      return result


   ## private methods ##

   def _check_init_shape(self, shape):
      if not isinstance(shape, _Shape):
         raise TypeError('shape must be an _Shape object.')

   def _check_init_shapes(self, shapes):
      for s in shapes:
         self._check_init_shape(s)


   ## OVERRIDES ##

   def __delitem__(self, indx):
      del(self._shapes[indx])

   def __getitem__(self, indx):
      return self._shapes[indx]

   def __len__(self):
      return len(self._shapes)

   def __setitem__(self, i, arg):
      if isinstance(i, int):
         self._check_init_shape(arg)
         self._shapes[i] = arg
      else:
         self._check_init_shapes(arg)
         self._shapes[i.start : i.stop] = arg

   ## operators ##
   ## these are destructive transformations ##

   def __add__(self, arg):
      return Group([s.__add__(arg) for s in self])

   def __radd__(self, arg):
      return self + arg

   def __iadd__(self, arg):
      self._shapes = [s.__iadd__(arg) for s in self]
      return self

   def __mul__(self, arg):
      return Group([s.__mul__(arg) for s in self])

   def __rmul__(self, arg):
      return self * arg

   def __imul__(self, arg):
      self._shapes = [s.__imul__(arg) for s in self]
      return self

   def __sub__(self, arg):
      return self + (-arg)
   
   def __rsub__(self, arg):
      return (-self) + arg

   def __isub__(self, arg):
      self._shapes = [s.__isub__(arg) for s in self]
      return self

   def __neg__(self):
      self._shapes = [s.__neg__( ) for s in self]
      return self

   def __eq__(self, arg):
      try:
         return self._shapes == arg._shapes
      except AttributeError:
         return False

