from chiplotle.hpgl.commands import FT
from chiplotle.core.interfaces.formatdecorator import FormatDecorator


class FillType(FormatDecorator):
   
   __doc__ = FT.__doc__

   def __init__(self, filltype=None, space=None, angle=None):
      FormatDecorator.__init__(self)
      self.filltype = filltype
      self.space = space
      self.angle = angle


   @property
   def _subcommands(self):
      return [FT(self.filltype, self.space, self.angle)]
