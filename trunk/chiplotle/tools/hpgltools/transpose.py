from chiplotle.hpgl.abstract.hpgl import _HPGL
from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.utils.ispair import ispair
from chiplotle.tools.hpgltools.is_primitive_absolute import is_primitive_absolute

def _transpose_command(arg, val):
   if not ispair(val):
      raise ValueError('Transposing argument must be a pair (x, y).')
   if is_primitive_absolute(arg) or isinstance(arg, _CompoundHPGL):
      arg.xy = arg.xy + val

def transpose(arg, val):
   if isinstance(arg, _HPGL):
      _transpose_command(arg, val)
   elif isinstance(arg, (list, tuple)):
      for c in arg:
         _transpose_command(c, val)
