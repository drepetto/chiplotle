from chiplotle.geometry.core.coordinatearray import CoordinateArray
from chiplotle.geometry.core.path import Path
from chiplotle.tools.mathtools.interpolate_linear import interpolate_linear

def path_linear(coords, interpolation_unit):
   '''Returns a path with linearly interpolated segments. 
   Visually the result is the same as a plain path, but this is
   useful as an intermediate step in constructing more interesting
   shapes by deforming this one.
   
   - `coords` is a CoordinateArray.
   - `interpolation_unit` is the magnitude of the path segments created.
      Think of it as the sampling period in digital recording.
      If `interpolation_unit` > coord[i] - coord[i-1], the 
      coord[i] - coord[i-1] segment is not further segmented.
   '''
   coords = CoordinateArray(coords)
   
   def units_per_path_segment(coords, interpolation_unit):
      result = [ ]
      diffs = coords.difference
      for i in range(len(diffs)):
         segs = diffs[i].magnitude / float(interpolation_unit)
         coord_pair = (coords[i], coords[i + 1])
         if segs < 1:
            result.append((coord_pair, 1))
         else:
            result.append((coord_pair, int(round(segs))))
      return result


   divs = units_per_path_segment(coords, interpolation_unit)
   result = [ ]
   for cp, n in divs:
      newcoords = [interpolate_linear(cp[0], cp[1], float(i) / n) for i in range(n)]
      result.extend(newcoords)

   return Path(result)



## demo
if __name__ == '__main__':
   from chiplotle import *
   import random

   coords = CoordinateArray([random.randint(0, 1000) for i in range(10)])
   #coords = CoordinateArray([0, 0, 300, 0, 300, 300, 0, 300, 0, 0])
   p = path_linear(coords, 100)

   circs =  [ ]
   for coord in p.points:
      c = circle(10, 8)
      offset(c, coord)
      circs.append(c)


   io.view(group([p] + circs))
