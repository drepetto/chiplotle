## DEPRECATE ####
#from chiplotle.hpgl.abstract.hpglcommand import _HPGLCommand
#from chiplotle.hpgl.scalable import Scalable
#
#class _Wedge(_HPGLCommand):
#   '''Abstract wedge.'''
#   def __init__(self, radius, startangle, sweepangle, chordangle=None):
#      self.radius = Scalable(radius)
#      self.startangle = startangle
#      self.sweepangle = sweepangle
#      self.chordangle = chordangle
#
#   @property
#   def format(self):
#      if self.chordangle:
#         return '%s%s,%.2f,%.2f,%.2f%s' % (self._name, self.radius, 
#         self.startangle, self.sweepangle, self.chordangle, 
#         _HPGLCommand._terminator)
#      else:
#         return '%s%s,%.2f,%.2f%s' % (self._name, self.radius, 
#         self.startangle, self.sweepangle, _HPGLCommand._terminator)
