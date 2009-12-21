
class _PlotterMargins(object):
   def __init__(self, plotter, queryCommand):  
      self._plotter = plotter
      self._queryCommand = queryCommand

   def _get(self):
      self._plotter._serialPort.flushInput()
      self._plotter._writeStringToPort(self._queryCommand.format)
      m = self._plotter._readPort().split(',')
      return tuple([float(n) for n in m])
#      return tuple([int(n) for n in m])
      
   @property
   def bottom(self):
      return self._get()[1]

   @property
   def top(self):
      return self._get()[3]

   @property
   def right(self):
      return self._get()[2]

   @property
   def left(self):
      return self._get()[0]

   @property
   def width(self):
      x1, y1, x2, y2 = self._get()
      return x2 - x1

   @property
   def height(self):
      x1, y1, x2, y2 = self._get()
      return y2 - y1
   
   @property
   def center(self):
      return (self.right + self.left) / 2., (self.top + self.bottom) / 2.

   @property
   def bottom_left(self):
      coords = self._get( )
      return coords[0:2]

   @property
   def top_right(self):
      coords = self._get( )
      return coords[2:4]


   def __repr__(self):
      return str(self._get())



