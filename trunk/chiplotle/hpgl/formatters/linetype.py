from chiplotle.hpgl.commands import LT
from chiplotle.core.interfaces.formatdecorator import FormatDecorator

class LineType(FormatDecorator):
   
   __doc__ = LT.__doc__

   def __init__(self, linetype=None, length=4):
      FormatDecorator.__init__(self)
      self.linetype  = linetype
      self.length    = length

   @property
   def _subcommands(self):
      return [LT(self.linetype, self.length)]



## DEMO
if __name__ == '__main__':
   from chiplotle.geometry.shapes.rectangle import rectangle
   from chiplotle.geometry.core.group import Group
   from chiplotle.tools import io

   r1 = rectangle(1000, 200)
   r2 = rectangle(300, 800)
   ltd = LineType(2, .5)
   ltd(r1)
   g = Group([r1, r2])
   ltd = LineType(3, .1)
   ltd(g)
   print g.format
   io.view(g)
