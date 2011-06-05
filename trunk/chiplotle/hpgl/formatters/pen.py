from chiplotle.hpgl.pen import Pen as HPGLPen
from chiplotle.core.interfaces.formatdecorator import FormatDecorator

class Pen(FormatDecorator):
   '''The Pen wraps HPGL Pen properties around a given Shape.

   - `pen` is the pen number to use.
   - `sticky` boolean; set to False to set plotter back to default values
      at the end of the decorated shape. Set to True to skip reset.
   '''
   
   def __init__(self, 
                number, 
                velocity    = None, 
                force       = None, 
                acceleration= None, 
                thickness   = None):
      FormatDecorator.__init__(self)
      self.number       = number
      self.velocity     = velocity
      self.force        = force
      self.acceleration = acceleration
      self.thickness    = thickness

   @property
   def _subcommands(self):
      p = HPGLPen(self.number, 
              self.velocity, 
              self.force, 
              self.acceleration, 
              self.thickness)
      return [p]



## DEMO
if __name__ == '__main__':
   from chiplotle.geometry.shapes.rectangle import rectangle

   pd = Pen(2, 3, 4, 5, 0.1)
   r = rectangle(100, 20)
   pd(r)
   print r.format
