
def cumsum(lst):
   '''Returns the cumulative sum of the values in `lst`.'''

   try:
      import numpy
      return numpy.cumsum(lst)
   except ImportError:
      r = 0
      result = []
      for n in lst:
         r += n
         result.append(r)
      return result
