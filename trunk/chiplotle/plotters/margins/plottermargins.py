from chiplotle.hpgl.coordinatepair import CoordinatePair

class _PlotterMargins(object):
   def __init__(self, plotter, queryCommand):  
      self._plotter = plotter
      self._queryCommand = queryCommand


   ## PROPERTIES ##

   @property
   def bottom(self):
      return self._get_all_coordinates( )[1]

   @property
   def top(self):
      return self._get_all_coordinates( )[3]

   @property
   def right(self):
      return self._get_all_coordinates( )[2]

   @property
   def left(self):
      return self._get_all_coordinates( )[0]

   @property
   def width(self):
      x1, y1, x2, y2 = self._get_all_coordinates( )
      return x2 - x1

   @property
   def height(self):
      x1, y1, x2, y2 = self._get_all_coordinates( )
      return y2 - y1
   
   @property
   def center(self):
      #return (self.right + self.left) / 2., (self.top + self.bottom) / 2.
      x = (self.right + self.left) / 2.
      y = (self.top + self.bottom) / 2.
      return CoordinatePair(x, y)

   @property
   def bottom_left(self):
      coords = self._get_all_coordinates( )
      #return coords[0:2]
      return CoordinatePair(coords[0:2])

   @property
   def bottom_right(self):
      coords = self._get_all_coordinates( )
      #return (coords[2], coords[1])
      return CoordinatePair(coords[2], coords[1])

   @property
   def top_right(self):
      coords = self._get_all_coordinates( )
      #return coords[2:4]
      return CoordinatePair(coords[2:4])

   @property
   def top_left(self):
      coords = self._get_all_coordinates( )
      #return (coords[0], coords[3])
      return CoordinatePair(coords[0], coords[3])

   ## METHODS ##

   def draw_outline(self, pen=1):
      pen = self._plotter._hpgl.SP(pen)
      pa = self._plotter._hpgl.PA(self.bottom_left)
      rec = self._plotter._hpgl.EA(self.top_right)
      self._plotter.write([pen, pa, rec])

   def draw_corners(self, pen=1):
      from chiplotle.hpgl.compound import Cross
      coords = self._get_all_coordinates( )
      size = 100
      corners = [ ]
      corners.append(Cross(coords[0:2], width = size, height = size, pen = 1))
      corners.append(Cross((coords[0], coords[3]), size,  size))
      corners.append(Cross((coords[2], coords[1]), size,  size))
      corners.append(Cross(coords[2:4], size,  size))
      self._plotter.write(corners)

   def _get_all_coordinates(self):
      self._plotter._serial_port.flushInput( )
      self._plotter._write_string_to_port(self._queryCommand.format)
      m = self._plotter._read_port( ).split(',')
      return tuple([float(n) for n in m])
#      return tuple([int(n) for n in m])
      

   ## OVERRIDES ##

   def __repr__(self):
      return str(self._get_all_coordinates( ))

