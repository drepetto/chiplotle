import os
import subprocess
from chiplotle.hpgl.abstract.hpglcommand import _HPGLCommand

def save_hpgl(expr, filename):
   '''Save text HPGL from Chiplotle-HPGL.

   - `expr` can be an iterable (e.g., list) or a Chiplotle-HPGL object.
   - `filename` the file name, including path but without extension.
   '''
   ## parse expr; extract pure text HPGL commands.
   hpgl = [ ]
   if isinstance(expr, (list, tuple)):
      for o in expr:
         assert isinstance(o, _HPGLCommand)
         hpgl.append(o.format)
   else:
      hpgl.append(expr.format)

   ## create HPGL file
   file = open('%s.hpgl' % filename, 'w')
   file.writelines(hpgl)
   file.close( )
