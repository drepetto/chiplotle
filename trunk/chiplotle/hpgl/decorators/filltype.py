from chiplotle.hpgl.commands import FT
from chiplotle.core.interfaces.formatdecorator import FormatDecorator

class FillTypeDecorator(FormatDecorator):
   
   def __init__(self, filltype):
      FormatDecorator.__init__(self)
      if not isinstance(filltype, FT):
         raise TypeError
      self.filltype = filltype

   @property
   def _subcommands(self):
      return [self.filltype]
