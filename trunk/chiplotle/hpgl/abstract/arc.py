from chiplotle.hpgl.abstract.positional import _Positional
from chiplotle.utils.ispair import ispair

class _Arc(_Positional):
   def __init__(self, xy, angle, chordtolerance=None, transposable=False):
      self.angle = angle
      self.chordtolerance = chordtolerance
      assert ispair(xy)
      _Positional.__init__(self, xy, transposable)

   @property
   def format(self):
      coordinates = ['%s' % p for p in self.xy]
      result = '%s%s,%s' % (self._name, ','.join(coordinates), 
         self.angle)
      if self.chordtolerance:
         result += ',%s' % self.chordtolerance
      result += self.terminator
      return result
