from chiplotle.hpgl import commands

class _PlotterMargins(object):
   def __init__(self, plotter, queryCommand):  
      self._plotter = plotter
      self._queryCommand = queryCommand

   def _get(self):
      self._plotter._serialPort.flushInput()
      self._plotter._writeStringToPort(self._queryCommand.format)
      m = self._plotter._readPort().split(',')
      return tuple([int(n) for n in m])
      
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

   def __repr__(self):
      return str(self._get())


class _MarginsSoft(_PlotterMargins):
   def __init__(self, plotter):
      _PlotterMargins.__init__(self, plotter, commands.OW( )) 


class _MarginsHard(_PlotterMargins):
   def __init__(self, plotter):
      _PlotterMargins.__init__(self, plotter, commands.OH( )) 
