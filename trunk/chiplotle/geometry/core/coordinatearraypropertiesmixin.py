from chiplotle.geometry.core.coordinate import Coordinate
import numpy as np

class CoordinateArrayPropertiesMixin(object):

   @property
   def centroid(self):
      coords = set(self._data)
      return sum(coords, Coordinate(0, 0)) / float(len(coords))

   @property
   def center(self):
      '''"center" is defined as being half way between the top/bottom
      and left/right-most points. This will be different from the
      centroid, which takes the distribution of the points into
      consideration.
      '''
      return sum(self.minmax, Coordinate(0, 0)) / 2.0

   @property
   def minmax(self):
      '''Returns the minimum and maximum coordinates.'''
      if len(self._data) == 0:
         return None
      coords= [list(c) for c in self._data]
      mx    = np.max(coords, 0).tolist()
      mn    = np.min(coords, 0).tolist()
      return (Coordinate(*mn), Coordinate(*mx))

   @property
   def difference(self):
      '''Returns the difference between consecutive elements in `self`.
      i.e., first derivative.
      '''
      result = [ ]
      for i in range(len(self) - 1):
         result.append(self[i+1] - self[i])
      return type(self)(result)


   @property
   def cumsum(self):
      '''Returns the cumulative sum.'''
      dimensions = len(self[0])
      result = [Coordinate(*([0] * dimensions))]
      for coord in self:
         result.append(result[-1] + coord)
      return type(self)(result)

