#######################################
#### TODO: Trash! this is deprecated.
#######################################

#import numpy
#
#class Scalable(numpy.ndarray):
#   def __new__(subtype, data, dtype='float32', copy=False):
#      # Make sure we are working with an array, and copy the data if requested
#      subarr = numpy.array(data, dtype=dtype, copy=copy)
#      # Transform 'subarr' from an ndarray to our new subclass.
#      subarr = subarr.view(subtype)
#      # Finally, we must return the newly created object:
#      return subarr
#
#   def __array_finalize__(self,obj):
#      pass
#
#   def __repr__(self):
#      return str(self)


class Scalable(object):
   def __init__(self, value):
      self._data = value


   ## PUBLIC PROPERTIES ##

   @property
   def dtype(self):
      return type(self._data)


## PRIVATE METHODS ##

   def _binary_operand_massage(self, arg):
      '''Checks binary operand and returns appropriate data.'''
      if isinstance(arg, self.__class__):
         arg = arg._data
      return arg


## OVERRIDES ##

   def __repr__(self):
      return str(self._data)

   def __float__(self):
      return float(self._data)

   def __int__(self):
      return int(self._data)

   def __add__(self, arg):
      arg = self._binary_operand_massage(arg)
      return self.__class__(self._data + arg)

   def __iadd__(self, arg):
      arg = self._binary_operand_massage(arg)
      self._data += arg
      return self

   def __radd__(self, arg):
      return self + arg

   def __div__(self, arg):
      arg = self._binary_operand_massage(arg)
      return self.__class__(self._data / arg)

   def __idiv__(self, arg):
      arg = self._binary_operand_massage(arg)
      self._data /= arg
      return self

   def __rdiv__(self, arg):
      arg = self._binary_operand_massage(arg)
      return self.__class__(arg / self._data)

   def __eq__(self, arg):
      arg = self._binary_operand_massage(arg)
      return self._data == arg

   def __sub__(self, arg):
      arg = self._binary_operand_massage(arg)
      return self.__class__(self._data - arg)

   def __isub__(self, arg):
      arg = self._binary_operand_massage(arg)
      self._data -= arg
      return self

   def __rsub__(self, arg):
      return self - arg

   def __mul__(self, arg):
      arg = self._binary_operand_massage(arg)
      return self.__class__(self._data * arg)

   def __imul__(self, arg):
      arg = self._binary_operand_massage(arg)
      self._data *= arg
      return self

   def __rmul__(self, arg):
      return self * arg

   def __neg__(self):
      return self.__class__(-self._data)

   def __pow__(self, arg):
      arg = self._binary_operand_massage(arg)
      return self.__class__(self._data ** arg)

   def __ipow__(self, arg):
      arg = self._binary_operand_massage(arg)
      self._data **= arg
      return self

   def __rpow__(self, arg):
      return self ** arg

