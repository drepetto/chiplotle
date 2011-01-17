from chiplotle.hpgl.abstract.hpglprimitive import _HPGLPrimitive
from chiplotle.tools.mathtools.rotate_2d import rotate_2d
from chiplotle.geometry.vectorarray import VectorArray
from chiplotle.geometry.vector import Vector


## TODO: implement rotation AXIS! 
## (options: center, centroid, left, right, top, bottom, and (x, y))

def rotate_hpglprimitives(arg, angle):
   for e in arg:
      if not isinstance(e, _HPGLPrimitive):
         raise TypeError('Elements must be of type _HPGLPrimitive')

      ## should we check for VectorArray and Vector instead?
      if hasattr(e, 'xy'): 
         if isinstance(e.xy, VectorArray):
            result = [ ]
            for cp in e.xy:
               result.append(Vector(rotate_2d(cp, angle)))
            e.xy = VectorArray(result)
         elif isinstance(e.xy, Vector):
            e.xy = Vector(rotate_2d(e.xy, angle))
         

