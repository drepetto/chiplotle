from chiplotle.hpgl.abstract.hpglprimitive import _HPGLPrimitive
from chiplotle.tools.mathtools.rotate_2d import rotate_coordinate_2d
from chiplotle.geometry.core.coordinatearray import CoordinateArray
from chiplotle.geometry.core.coordinate import Coordinate


## TODO: implement rotation AXIS! 
## (options: center, centroid, left, right, top, bottom, and (x, y))

def rotate_hpglprimitives(arg, angle):
   for e in arg:
      if not isinstance(e, _HPGLPrimitive):
         raise TypeError('Elements must be of type _HPGLPrimitive')

      ## should we check for CoordinateArray and Coordinate instead?
      if hasattr(e, 'xy'): 
         pivot = Coordinate(0, 0)
         if isinstance(e.xy, CoordinateArray):
            result = [ ]
            for cp in e.xy:
               result.append(rotate_coordinate_2d(cp, angle, pivot))
            e.xy = CoordinateArray(result)
         elif isinstance(e.xy, Coordinate):
            e.xy = rotate_coordinate_2d(e.xy, angle, pivot)
         

