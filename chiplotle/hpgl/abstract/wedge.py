from chiplotle.hpgl.abstract.hpglcommand import _HPGLCommand
from chiplotle.hpgl.scalable import Scalable

class _Wedge(_HPGLCommand):
   '''Abstract wedge.'''
   def __init__(self, radius, startangle, sweepangle, chordangle=None):
      self.radius = Scalable(radius)
      self.startangle = startangle
      self.sweepangle = sweepangle
      self.chordangle = chordangle

   @property
   def format(self):
      if self.chordangle:
         return '%s%s,%s,%s,%s%s' % (self._name, self.radius, 
         self.startangle, self.sweepangle, self.chordangle, 
         self.terminator)
      else:
         return '%s%s,%s,%s%s' % (self._name, self.radius, 
         self.startangle, self.sweepangle, self.terminator)
