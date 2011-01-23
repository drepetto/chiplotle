from __future__ import division
from chiplotle.core import errors
import math

class Coordinate(object):

   __slots__ = ('_x', '_y')

#   def __new__(cls, *args):
#      if len(args) == 1 and isinstance(args[0], Coordinate):
#         return args[0]
#      else:
#         ## NOTE: Python 2.6.6... DeprecationWarning: object.__new__() takes no parameters
#         #return super(Coordinate, cls).__new__(cls, *args)
#         return super(Coordinate, cls).__new__(cls)

   def __init__(self, *args):
      if len(args) == 1:
         if isinstance(args[0], Coordinate):
            self._x, self._y = args[0].x, args[0].y
#         elif isinstance(args[0], (list, tuple)):
#            self.__init__(*args[0])
         else:
            #raise TypeError('argument not recognized by Coordinate.')
            raise errors.InitParameterError( )
      elif len(args) == 2:
         from chiplotle.tools.iterabletools.isiterable import isiterable
         if isiterable(args[0]) or isiterable(args[1]):
            #raise TypeError('Each element in the pair must be a scalar')
            raise errors.InitParameterError( )
         self._x = args[0]
         self._y = args[1]
      else:
         #raise ValueError('too many arguments Coordinate.')
         raise errors.InitParameterError( )


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

   @property
   def magnitude(self):
      return math.sqrt(self.x ** 2 + self.y ** 2)


   ## OVERRIDES ##

   def __getitem__(self, arg):
      return self.xy[arg]

   def __iter__(self):
      for e in self.xy:
         yield e

   def __hash__(self):
      ## TODO: what is the best way to hash this pair?
      return hash(('CP', self.x, self.y))

   def __len__(self):
      return 2

   def __repr__(self):
      return 'Coordinate(%s, %s)' % (self.x, self.y)

   def __str__(self):
      return '<%s,%s>' % (self.x, self.y)


   ## math operators ##

   ## addition ##

   def __abs__(self):
      return Coordinate(abs(self.x), abs(self.y))

   def __add__(self, arg):
      try:
         #arg = Coordinate(arg)
         return Coordinate(self.x + arg.x, self.y + arg.y)
      except:
         try:
            return Coordinate(self.x + arg, self.y + arg)
         except:
            try:
               return arg.__radd__(self)
            except:
               raise errors.OperandError

   def __radd__(self, arg):
      return self + arg


   ## substraction ##

   def __sub__(self, arg):
      try:
         #arg = Coordinate(arg)
         return Coordinate(self.x - arg.x, self.y - arg.y)
      except:
         try:
            return Coordinate(self.x - arg, self.y - arg)
         except:
            try:
               return arg.__rsub__(self)
            except:
               raise errors.OperandError

   def __rsub__(self, arg):
      return -(self - arg)


   ## division ##

   def __div__(self, arg):
      return self.__truediv__(arg)
   
   def __floordiv__(self, arg):
      result = self.__div__(arg)
      return Coordinate(int(math.floor(result.x)), int(math.floor(result.y)))

   def __truediv__(self, arg):
      try:
         return Coordinate(self.x / arg.x, self.y / arg.y)
      except AttributeError:
         try:
            return Coordinate(self.x / arg, self.y / arg)
         except (TypeError, errors.InitParameterError):
            raise errors.OperandError( )


   ## mul ##

   def __mul__(self, arg):
      try:
         #coord = Coordinate(arg)
         return Coordinate(self.x * arg.x, self.y * arg.y)
      except AttributeError:
         try:
            return Coordinate(self.x * arg, self.y * arg)
         except errors.InitParameterError:
            raise errors.OperandError( )


   def __rmul__(self, arg):
      return self * arg

   ## ## 

   def __eq__(self, arg):
      try:
         #arg = Coordinate(arg)
         return (self.x == arg.x) and (self.y == arg.y)
      except AttributeError:
         return False

   def __invert__(self):
      '''Returns the perpendicular of self.
      http://mathworld.wolfram.com/PerpendicularCoordinate.html
      '''
      return Coordinate(-self.y, self.x)

   def __ne__(self, arg):
      return not (self == arg)

   def __neg__(self):
      return Coordinate(-self.x, -self.y)

