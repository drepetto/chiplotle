from chiplotle.hpgl.abstract.positional import _Positional
from chiplotle.hpgl.abstract.hpglprimitive import _HPGLPrimitive
from chiplotle.utils.ispair import ispair

class _Arc(_Positional):
   def __init__(self, xy, angle, chordtolerance=None):
      self.angle = angle
      self.chordtolerance = chordtolerance
      _Positional.__init__(self, xy)

   @apply
   def angle( ):
      def fget(self):
         return self._angle
      def fset(self, arg):
         if abs(arg) > 360:
            raise ValueError('angle must be between -360 and 360.')
         self._angle = arg
      return property(**locals( ))

   @property
   def format(self):
      if isinstance(self.x, int) and isinstance(self.y, int):
         coordinates = '%i,%i' % (self.x, self.y)
      else:
         coordinates = '%.2f,%.2f' % (self.x, self.y)
      result = '%s%s,%.2f' % (self._name, coordinates, self.angle)
      if self.chordtolerance:
         result += ',%.2f' % self.chordtolerance
      result += _HPGLPrimitive._terminator
      return result
