from chiplotle.hpgl.abstract.hpglprimitive import _HPGLPrimitive
from chiplotle.tools.mathtools.rotate_2d import rotate_2d
from chiplotle.hpgl.coordinatearray import CoordinateArray
from chiplotle.hpgl.coordinatepair import CoordinatePair


def rotate_hpglprimitives(arg, val):
   for e in arg:
      if not isinstance(e, _HPGLPrimitive):
         raise TypeError('Elements must be of type _HPGLPrimitive')

      ## should we check for CoordinateArray and CoordinatePair instead?
      if hasattr(e, 'xy'): 
         if isinstance(e.xy, CoordinateArray):
            result = [ ]
            for cp in e.xy:
               result.append(CoordinatePair(rotate_2d(cp, val)))
            e.xy = CoordinateArray(result)
         elif isinstance(e.xy, CoordinatePair):
            e.xy = CoordinatePair(rotate_2d(e.xy, val))
         

