from chiplotle.hpgl.pen import Pen
from chiplotle.hpgl.pendefaults import PenDefaults
from chiplotle.core.interfaces.formatdecorator import FormatDecorator

class PenDecorator(FormatDecorator):
   
   def __init__(self, pen, sticky=False):
      if not isinstance(pen, Pen):
         raise TypeError
      self.pen = pen
      FormatDecorator.__init__(self, sticky)

   @property
   def preformat_commands(self):
      return self.pen

   @property
   def postformat_commands(self):
      return PenDefaults()


## DEMO
if __name__ == '__main__':
   from chiplotle.geometry.factory.rectangle import rectangle

   p = Pen(2, 3, 4, 5, 0.1)
   pd = PenDecorator(p, False)
   r = rectangle(100, 20)
   pd(r)
   print r.format
