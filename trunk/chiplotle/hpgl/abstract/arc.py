from chiplotle.hpgl.abstract.positional import _Positional

class _Arc(_Positional):
   def __init__(self, xy, a, chordangle=5, transposable=False):
      self.a = a
      self.chordangle = chordangle
      _Positional.__init__(self, xy, transposable)

   def __str__(self):
      result = _Positional.__str__(self)
      result = result.rstrip(self.terminator)
      return result + ',%d,%d%s' %(self.a, self.chordangle, self.terminator)

