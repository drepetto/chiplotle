from chiplotle.hpgl.abstract.hpgl import _HPGL
#from chiplotle.hpgl.compound.container import Container
#from chiplotle.hpgl.compound.hpglcontainer import HPGLContainer
from chiplotle.hpgl.compound.group import Group

def _scale_command(obj, val):
   attrs = obj.__dict__.keys()
   for scalable_attr in obj.__class__._scalable:
      a = getattr(obj, scalable_attr)
      setattr(obj, scalable_attr, a * val)

def scale(obj, val):
   if isinstance(obj, _HPGL):
      _scale_command(obj, val)
   #if isinstance(obj, (list, tuple, Container, HPGLContainer)):
   if isinstance(obj, (list, tuple, Group)):
      for c in obj:
         _scale_command(c, val)
