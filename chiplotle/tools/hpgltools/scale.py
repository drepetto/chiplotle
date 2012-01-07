from chiplotle.hpgl.abstract.hpgl import _HPGL

def _scale_command(obj, val):
   attrs = obj.__dict__.keys()
   for scalable_attr in obj.__class__._scalable:
      a = getattr(obj, scalable_attr)
      setattr(obj, scalable_attr, a * val)

def scale(obj, val):
   if isinstance(obj, _HPGL):
      _scale_command(obj, val)
   if isinstance(obj, (list, tuple)):
      for c in obj:
         _scale_command(c, val)
