from chiplotle.hpgl.abstract.hpglcommand import _HPGLCommand
from chiplotle.hpgl.compound.container import Container
from chiplotle.hpgl.compound.hpglcontainer import HPGLContainer
from chiplotle.hpgl.scalable import Scalable

def _scale_command(arg, val):
   attrs = arg.__dict__.keys()
   for aname in attrs:
      a = getattr(arg, aname)
      if isinstance(a, Scalable):
         #a *= val
         setattr(arg, aname, a * val)

def scale(arg, val):
   if isinstance(arg, _HPGLCommand):
      _scale_command(arg, val)
   if isinstance(arg, (list, tuple, Container, HPGLContainer)):
      for c in arg:
         _scale_command(c, val)
