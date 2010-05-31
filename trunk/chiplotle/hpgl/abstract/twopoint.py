from chiplotle.hpgl.abstract.hpglprimitive import _HPGLPrimitive

class _TwoPoint(_HPGLPrimitive):
   '''Abstract class for commands with 2 coordinate pairs: x1, y1, x2, y2.'''
   def __init__(self, coords=None):
      if coords:
         assert len(coords) == 4
      self.coords = coords

   @property
   def format(self):
      if self.coords:
         return '%s%s%s' % (self._name, ','.join([str(c) 
            for c in self.coords]), _HPGLPrimitive._terminator)
      else:
         return '%s%s' % (self._name, _HPGLPrimitive._terminator)

