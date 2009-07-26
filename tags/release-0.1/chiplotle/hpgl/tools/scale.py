from chiplotle.hpgl.abstract.hpglcommand import _HPGLCommand
from chiplotle.hpgl.compound.container import Container
from chiplotle.hpgl.scalable import Scalable

def _scale_command(arg, val):
   attrs = arg.__dict__.keys()
   for an in attrs:
      a = getattr(arg, an)
      if isinstance(a, Scalable):
         a *= val

def scale(arg, val):
   if isinstance(arg, Container):
      _scale_command(arg, val)
      for c in arg:
         _scale_command(c, val)
   elif isinstance(arg, _HPGLCommand):
      _scale_command(arg, val)
   elif isinstance(arg, (list, tuple)):
      for c in arg:
         _scale_command(c, val)
