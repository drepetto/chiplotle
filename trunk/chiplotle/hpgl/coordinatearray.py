from chiplotle.hpgl.scalable import Scalable
import numpy

class CoordinateArray(Scalable):
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
         elif arg is None:
            #arg = numpy.array([ ], dtype = 'float32').reshape((-1, 2))
            arg = numpy.array([ ]).reshape((-1, 2))
            self._data = arg
         else:
            #arg = numpy.array(arg, dtype = 'float32').reshape((-1, 2))
            arg = numpy.array(arg).reshape((-1, 2))
            self._data = arg
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
      arg = self._binary_operand_massage(arg)
      return numpy.all(self._data == arg)

