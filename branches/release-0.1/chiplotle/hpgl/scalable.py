import numpy

class Scalable(numpy.ndarray):
   def __new__(subtype, data, dtype='float32', copy=False):
      # Make sure we are working with an array, and copy the data if requested
      subarr = numpy.array(data, dtype=dtype, copy=copy)
      # Transform 'subarr' from an ndarray to our new subclass.
      subarr = subarr.view(subtype)
      # Finally, we must return the newly created object:
      return subarr

   def __array_finalize__(self,obj):
      pass

   def __repr__(self):
      return str(self)

