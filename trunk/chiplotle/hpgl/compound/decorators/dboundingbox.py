from chiplotle.hpgl.compound.decorators.hpglcompounddecorator \
   import _HPGLCompoundDecorator
from chiplotle.tools.hpgltools.get_bounding_box import get_bounding_box
from chiplotle.hpgl.commands  import PU, PA, EA


class DBoundingBox(_HPGLCompoundDecorator):
   '''This decorator adds a bounding box to the shape(s) passed to it.
   '''

   def __init__(self, hpglcompound):
      _HPGLCompoundDecorator.__init__(self, hpglcompound)


   @property
   def _subcommands(self):
      result = self.hpglcompound._subcommands
      coords = get_bounding_box(result)
      result += [PU( ), PA(coords[0]), EA(coords[1])]
      return result
