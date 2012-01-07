from chiplotle.hpgl.abstract.hpgl import _HPGL
from chiplotle.tools.hpgltools.is_primitive_absolute import is_primitive_absolute
from chiplotle.geometry.core.coordinate import *

def _transpose_command(arg, val):
   from chiplotle.tools.iterabletools.ispair import ispair
   val = Coordinate(*val)
   if is_primitive_absolute(arg): 
      arg.xy = arg.xy + val

def transpose(arg, val):
   if isinstance(arg, _HPGL):
      _transpose_command(arg, val)
   elif isinstance(arg, (list, tuple)):
      for c in arg:
         _transpose_command(c, val)
