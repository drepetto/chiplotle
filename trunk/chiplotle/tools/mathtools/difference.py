
def difference(seq):
   '''Returns the difference between consecutive elements in `seq`.
   i.e., first derivative.
   '''
   result = [ ]
   for i in range(len(seq) - 1):
      result.append(seq[i+1] - seq[i])
   return type(seq)(result)
