from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.compound.line import Line
from chiplotle.hpgl.scalable import Scalable
from chiplotle.utils.ispair import ispair

class GroovyFrame(_CompoundHPGL):
   def __init__(self, xy, wh1, wh2, linesPerSide, pen=None):
      _CompoundHPGL.__init__(self, xy, pen)
      assert ispair(wh1)
      assert ispair(wh2)
      self.wh1 = Scalable(wh1)
      self.wh2 = Scalable(wh2)
      self.linesPerSide = linesPerSide

   def _computePointLocations(self, line):
      result = [ ]
      for i in range(self.linesPerSide + 1):
        result.append( line / self.linesPerSide * i)
      return result 
 
   def _computeCoordinates(self, expr):
      w = expr[0]
      h = expr[1]
      xs = self._computePointLocations(w)
      for i in range(len(xs)):
         xs[i] -= w / 2.
      ys = self._computePointLocations(h)
      for i in range(len(ys)):
         ys[i] -= h / 2.
         
      top_coords = [(x, ys[-1]) for x in xs]
      bottom_coords = [(x, ys[0]) for x in xs]
      left_coords = [(xs[0], y) for y in ys]
      right_coords = [(ys[-1], y) for y in ys]
      return (top_coords, bottom_coords, left_coords, right_coords)

   def _computeSquares(self):
      t_1, b_1, l_1, r_1 = self._computeCoordinates(self.wh1)      
      t_2, b_2, l_2, r_2 = self._computeCoordinates(self.wh2)      
      top = [x + y for x, y in zip(t_1, t_2)] 
      bottom = [x + y for x, y in zip(b_1, b_2)] 
      left = [x + y for x, y in zip(l_1, l_2)] 
      right = [x + y for x, y in zip(r_1, r_2)] 
      return (top, bottom, left, right)


   @property
   def _subcommands(self):
      result = _CompoundHPGL._subcommands.fget(self)
      for element in self._computeSquares( ):
         for coords in element:
            coords = list(coords)
            coords[0] += self.xabsolute
            coords[2] += self.xabsolute
            coords[1] += self.yabsolute
            coords[3] += self.yabsolute
            result.append(Line(*coords))
      return result

