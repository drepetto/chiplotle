from chiplotle.geometry.core.coordinate import Coordinate

class CoordinateArrayPropertiesMixin(object):

   @property
   def centroid(self):
      coords = set(self._data)
      return sum(coords) / float(len(coords))


   @property
   def center(self):
      '''"center" is defined as being half way between the top/bottom
      and left/right-most points. This will be different from the
      centroid, which takes the distribution of the points into
      consideration.
      '''
      min_coord, max_coord = self.minmax
      w, h = max_coord - min_coord
      x_center = min_coord.x + (w / 2.0)
      y_center = min_coord.y + (h / 2.0)
      return Coordinate(x_center, y_center)
   

   @property
   def minmax(self):
      '''Returns the pair of minimum and maximum coordinates.'''
      if len(self._data) == 0:
         return None
      max_x = max(self.x)
      min_x = min(self.x)
      max_y = max(self.y)
      min_y = min(self.y)
      return (Coordinate(min_x, min_y), Coordinate(max_x, max_y))


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
      result = [Coordinate(0, 0)]
      for coord in self:
         result.append(result[-1] + coord)
      return type(self)(result)

