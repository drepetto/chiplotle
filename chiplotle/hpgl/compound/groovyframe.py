from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.commands import PA, PD, PU

class GroovyFrame(_CompoundHPGL):
   
   _scalable = ['xy', 'w1', 'h1', 'w2', 'h2']

   def __init__(self, xy, w1, h1, w2, h2, lines_per_side, pen=None):
      _CompoundHPGL.__init__(self, xy, pen)
      self.w1 = w1
      self.h1 = h1
      self.w2 = w2
      self.h2 = h2
      self.lines_per_side = lines_per_side


   ## PRIVATE PROPERTIES ##

   @property
   def _subcommands(self):
      result = _CompoundHPGL._subcommands.fget(self)
      for element in self._compute_squares( ):
         for coords in element:
            coords = list(coords)
            coords[0] += self.xabsolute
            coords[2] += self.xabsolute
            coords[1] += self.yabsolute
            coords[3] += self.yabsolute
            ## draw straight line...
            r = [PU( ), PA(coords[:2]), PD( ), PA(coords[2:])]
            result += r
      result.append(PU( ))
      return result


   ## PRIVATE METHODS ##

   def _compute_point_locations(self, line):
      result = [ ]
      for i in range(self.lines_per_side + 1):
        result.append( line / self.lines_per_side * i)
      return result 
 
   def _compute_coordinates(self, w, h):
      xs = self._compute_point_locations(w)
      for i in range(len(xs)):
         xs[i] -= w / 2.
      ys = self._compute_point_locations(h)
      for i in range(len(ys)):
         ys[i] -= h / 2.
         
      top_coords = [(x, ys[-1]) for x in xs]
      bottom_coords = [(x, ys[0]) for x in xs]
      left_coords = [(xs[0], y) for y in ys]
      right_coords = [(ys[-1], y) for y in ys]
      return (top_coords, bottom_coords, left_coords, right_coords)

   def _compute_squares(self):
      t_1, b_1, l_1, r_1 = self._compute_coordinates(self.w1, self.h1)      
      t_2, b_2, l_2, r_2 = self._compute_coordinates(self.w2, self.h2)      
      top = [x + y for x, y in zip(t_1, t_2)] 
      bottom = [x + y for x, y in zip(b_1, b_2)] 
      left = [x + y for x, y in zip(l_1, l_2)] 
      right = [x + y for x, y in zip(r_1, r_2)] 
      return (top, bottom, left, right)


