#from chiplotle.hpgl.abstract.hpglcommand import _HPGLCommand
#
#class _CharSize(_HPGLCommand):
#   """Abstract class for Character Size commands."""
#   def __init__(self, w = None, h = None):   
#      self.w = w
#      self.h = h
#
#   @property
#   def format(self):
#      if self.w and self.h:
#         #return '%s%.4f,%.4f%s' % (self._name, self.w, self.h, self.terminator)
#         return '%s%.4f,%.4f%s' % (self._name, self.w, self.h, _HPGLCommand._terminator)
#      else:
#         #return '%s%s' % (self._name, self.terminator)
#         return '%s%s' % (self._name, _HPGLCommand._terminator)
#
