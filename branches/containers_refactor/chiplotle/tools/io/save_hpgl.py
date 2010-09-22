import os
import subprocess
#from chiplotle.hpgl.abstract.hpglprimitive import _HPGLPrimitive
from chiplotle.hpgl.abstract.hpgl import _HPGL

def save_hpgl(expr, filename):
   '''Save text HPGL from Chiplotle-HPGL.

   - `expr` can be an iterable (e.g., list) or a Chiplotle-HPGL object.
   - `filename` the file name, including path and extension (usually .hpgl or .plt)
   '''
   ## parse expr; extract pure text HPGL commands.
   hpgl = [ ]
   if isinstance(expr, (list, tuple)):
      for o in expr:
         #assert isinstance(o, _HPGLPrimitive)
         assert isinstance(o, _HPGL)
         hpgl.append(o.format)
   else:
      hpgl.append(expr.format)

   ## create HPGL file
   file = open('%s' % filename, 'w')
   file.writelines(hpgl)
   file.close( )
