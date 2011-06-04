from chiplotle.hpgl.pen import Pen
from chiplotle.core.interfaces.formatdecorator import FormatDecorator

class PenDecorator(FormatDecorator):
   '''The PenDecorator wraps HPGL Pen properties around a given Shape.

   - `pen` is the pen number to use.
   - `sticky` boolean; set to False to set plotter back to default values
      at the end of the decorated shape. Set to True to skip reset.
   '''
   
   def __init__(self, pen):
      if not isinstance(pen, Pen):
         raise TypeError
      FormatDecorator.__init__(self)
      self.pen = pen

   @property
   def _subcommands(self):
      return self.pen._subcommands
      #return [self.pen]



## DEMO
if __name__ == '__main__':
   from chiplotle.geometry.shapes.rectangle import rectangle

   p = Pen(2, 3, 4, 5, 0.1)
   pd = PenDecorator(p)
   r = rectangle(100, 20)
   pd(r)
   print r.format
