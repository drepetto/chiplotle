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
   from chiplotle import *

   lines = Group()
   for i in range(10):
      dot_space = i / 2.0
      line_space = i * 400

      lt = formatters.LineType(1, dot_space)
      l = line((0, line_space), (3000, line_space))
      lt(l)

      lb = label(str(dot_space), .1, .1)
      offset(lb, (-10, line_space))

      lines.append(l)
      lines.append(lb)

   formatters.Pen(1)(lines)
   offset(lines, (0, 1000))
   io.view(lines)
   #p = plottertools.instantiate_plotters()[0]
   #p.write(lines)
