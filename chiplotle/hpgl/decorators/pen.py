from chiplotle.hpgl.pen import Pen
from chiplotle.hpgl.pendefaults import PenDefaults
from chiplotle.core.interfaces.formatdecorator import FormatDecorator

class PenDecorator(FormatDecorator):
   '''The PenDecorator wraps HPGL Pen properties around a given Shape.

   - `pen` is the pen number to use.
   - `sticky` boolean; set to False to set plotter back to default values
      at the end of the decorated shape. Set to True to skip reset.
   '''
   
   def __init__(self, pen, sticky=False):
      if not isinstance(pen, Pen):
         raise TypeError
      self.pen = pen
      FormatDecorator.__init__(self, sticky)

   @property
   def preformat_commands(self):
      return [self.pen]

   @property
   def postformat_commands(self):
      return [PenDefaults()]


## DEMO
if __name__ == '__main__':
   from chiplotle.geometry.factory.rectangle import rectangle

   p = Pen(2, 3, 4, 5, 0.1)
   pd = PenDecorator(p, False)
   r = rectangle(100, 20)
   pd(r)
   print r.format
