from __future__ import division
from chiplotle.geometry.core.coordinatearray import CoordinateArray
from chiplotle.tools.geometrytools.split_vector_equidistantly import \
   split_vector_equidistantly

def split_coordinatearray_proportionally(coord_array, count):
   '''Splits a CoordinateArray into `count` segments, in proportion to
   the length of each Coordinate segment.'''
   rounder = Rounder()
   total_length = coord_array.magnitude
   result = []
   for coord in coord_array.difference:
      ratio = coord.magnitude / total_length
      c = rounder.round(count * ratio)
      r = split_vector_equidistantly(coord, c) 
      r = r.difference
      result.extend(r)
   result =  CoordinateArray(result).cumsum + coord_array[0]
   assert len(result) == count + 1
   return result

class Rounder(object):
   '''Hack class to keep track of residues.
   Come up with a good structural / rational solution.
   '''
   def __init__(self):
      self.residue = 0

   def round(self, n):
      if abs(self.residue) >= 0.5:
         n = n - self.residue
         self.residue = 0
      rn = int(round(n))
      self.residue += rn - n
      return rn

if __name__ == '__main__':
   ca = CoordinateArray([(20, 0), (20, 500), (20, 1000)])
   print split_coordinatearray_proportionally(ca, 8)
