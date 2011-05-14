from chiplotle.hpgl.commands import FT
from chiplotle.core.interfaces.formatdecorator import FormatDecorator

class FillTypeDecorator(FormatDecorator):
   
   def __init__(self, filltype, sticky=False):
      FormatDecorator.__init__(self, sticky)
      if not isinstance(filltype, FT):
         raise TypeError
      self.filltype = filltype

   @property
   def preformat_commands(self):
      return [self.filltype]

   @property
   def postformat_commands(self):
      return [FT( )]

