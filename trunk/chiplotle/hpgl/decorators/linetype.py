from chiplotle.hpgl.commands import LT
from chiplotle.core.interfaces.formatdecorator import FormatDecorator

class LineTypeDecorator(FormatDecorator):
   
   def __init__(self, linetype):
      FormatDecorator.__init__(self)
      if not isinstance(linetype, LT):
         raise TypeError
      self.linetype = linetype

   @property
   def _subcommands(self):
      return [self.linetype]



## DEMO
if __name__ == '__main__':
   from chiplotle.geometry.shapes.rectangle import rectangle
   from chiplotle.geometry.core.group import Group
   from chiplotle.tools import io

   r1 = rectangle(1000, 200)
   r2 = rectangle(300, 800)
   ltd = LineTypeDecorator(LT(2, .5))
   ltd(r1)
   g = Group([r1, r2])
   ltd = LineTypeDecorator(LT(3, .1))
   ltd(g)
   print g.format
   io.view(g)
