from __future__ import division
import numpy

class CoordinatePair(object):

   __slots__ = ('_x', '_y')

   def __init__(self, *args):
      if len(args) == 1 and isinstance(args[0], CoordinatePair):
         cp = args[0]
         self._x = cp.x
         self._y = cp.y
      elif len(args) == 1 and isinstance(args[0], (list, tuple)):
         self.__init__(*args[0])
      elif len(args) == 2:
         from chiplotle.tools.iterabletools.isiterable import isiterable
         if isiterable(args[0]) or isiterable(args[1]):
            raise TypeError('Each element in the pair must be a scalar')
         self._x = args[0]
         self._y = args[1]
      else:
         raise TypeError('args not recognized for CoordinatePair.')


   ## PUBLIC PROPERTIES ##

   @property
   def xy(self):
      return self.x, self.y

   @property
   def x(self):
      return self._x

   @property
   def y(self):
      return self._y


   ## OVERRIDES ##

   def __iter__(self):
      for e in self.xy:
         yield e

   def __getitem__(self, arg):
      return self.xy[arg]

   def __len__(self):
      return 2

   def __neg__(self):
      return CoordinatePair(-self.x, -self.y)

   def __eq__(self, arg):
      if isinstance(arg, CoordinatePair):
         return self.xy == arg.xy
      else:
         return self.xy == tuple(arg)

   def __hash__(self):
      ## TODO: what is the best way to hash this pair?
      return hash(('CP', self.x, self.y))

   def __ne__(self, arg):
      return not (self == arg)

   def __abs__(self):
      return CoordinatePair(abs(self.x), abs(self.y))

   def __add__(self, arg):
      from chiplotle.tools.iterabletools.ispair import ispair
      if isinstance(arg, CoordinatePair):
         return CoordinatePair(self.x + arg.x, self.y + arg.y)
      elif ispair(arg):
         return CoordinatePair(self.x + arg[0], self.y + arg[1])
      elif isinstance(arg, (int, float)):
         return CoordinatePair(self.x + arg, self.y + arg)
      else:
         raise TypeError

   def __radd__(self, arg):
      return self + arg

   def __sub__(self, arg):
      return self + -arg

   def __rsub__(self, arg):
      return arg + -self

   def __mul__(self, arg):
      return CoordinatePair(self.x * arg, self.y * arg)

   def __rmul__(self, arg):
      return self * arg

   def __div__(self, arg):
      if arg == 0:
         raise ZeroDivisionError
      return CoordinatePair(self.x / arg, self.y / arg)

   def __truediv__(self, arg):
      return self / arg

   def __repr__(self):
      return 'CoordinatePair(%s, %s)' % (self.x, self.y)

   def __str__(self):
      return '<%s,%s>' % (self.x, self.y)

