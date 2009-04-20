from chiplotle.hpgl.abstract.hpglcommand import _HPGLCommand
from chiplotle.hpgl.abstract.positional import _Positional
from chiplotle.utils.ispair import ispair

def _transpose_command(arg, val):
   if not ispair(val):
      raise ValueError('Transposing argument must be a pair (x, y).')
#   if hasattr(arg, '_xy'):
   if isinstance(arg, _Positional) and arg._transposable:
      arg._xy[0::2] += val[0]
      arg._xy[1::2] += val[1]

def transpose(arg, val):
   if isinstance(arg, _HPGLCommand):
      _transpose_command(arg, val)
   elif isinstance(arg, (list, tuple)):
      for c in arg:
         _transpose_command(c, val)


