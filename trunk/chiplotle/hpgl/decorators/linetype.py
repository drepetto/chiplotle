from chiplotle.hpgl.commands import LT
from chiplotle.core.interfaces.formatdecorator import FormatDecorator

class LineTypeDecorator(FormatDecorator):
   
   def __init__(self, linetype, sticky=False):
      FormatDecorator.__init__(self, sticky)
      if not isinstance(linetype, LT):
         raise TypeError
      self.linetype = linetype

   @property
   def preformat_commands(self):
      return [self.linetype]

   @property
   def postformat_commands(self):
      return [LT( )]


## DEMO
if __name__ == '__main__':
   from chiplotle.geometry.shapes.rectangle import rectangle
   from chiplotle.geometry.core.group import Group
   from chiplotle.tools import io

   ltd = LineTypeDecorator(LT(2, .5), False)
   r1 = rectangle(1000, 200)
   r2 = rectangle(300, 800)
   ltd(r1)
   print r1.format
   g = Group([r1, r2])
   print g.format
   io.view(g)
