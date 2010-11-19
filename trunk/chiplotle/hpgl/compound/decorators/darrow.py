from chiplotle.hpgl.compound.decorators.hpglcompounddecorator \
   import _HPGLCompoundDecorator
from chiplotle.hpgl.compound.abstractpath import _AbstractPath
from chiplotle.hpgl.compound.isosceles import Isosceles
from chiplotle.tools.hpgltools.get_all_coordinates import get_all_coordinates
from chiplotle.tools.mathtools.xy_to_polar import xy_to_polar

class DArrow(_HPGLCompoundDecorator):
   '''Adds an arrow head and / or tail to _Path shape.
   Only _Path shapes are allowed for this decorator.'''

   def __init__(self, hpglcompound, width, length):
      if not isinstance(hpglcompound, _AbstractPath):
         raise TypeError('DArrow can only take _Paths.')
      _HPGLCompoundDecorator.__init__(self, hpglcompound)

      self.width = width
      self.length = length


   def _get_head_subcommands(self, coords):
      head_vector = coords[-1] - coords[-2]
      r, a = xy_to_polar(head_vector)
      head = Isosceles(coords[-1], self.width, self.length, a)
      return [head]

   def _get_tail_subcommands(self, coords):
      tail_vector = coords[1] - coords[0]
      r, a = xy_to_polar(tail_vector)
      return [ ]


   @property
   def _subcommands(self):
      result = self.hpglcompound._subcommands
      coords = get_all_coordinates(result)
      result += self._get_head_subcommands(coords)
      result += self._get_tail_subcommands(coords)
      return result
