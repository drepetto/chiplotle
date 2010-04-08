from chiplotle.hpgl.abstract.positional import _Positional
from chiplotle.hpgl.abstract.hpglcommand import _HPGLCommand
from chiplotle.utils.ispair import ispair

class _Arc(_Positional):
   def __init__(self, xy, angle, chordtolerance=None, transposable=False):
      self.angle = angle
      self.chordtolerance = chordtolerance
      assert ispair(xy)
      _Positional.__init__(self, xy, transposable)

   @property
   def format(self):
      if self._coords.dtype == int:
         coordinates = ['%i,%i' % tuple(p) for p in self.xy]
      else:
         coordinates = ['%.2f,%.2f' % tuple(p) for p in self.xy]
      result = '%s%s,%.2f' % (self._name, ','.join(coordinates), 
         self.angle)
      if self.chordtolerance:
         result += ',%.2f' % self.chordtolerance
      result += _HPGLCommand._terminator
      return result
