from __future__ import division
from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.compound.bezier import Bezier

class RoundRectangle(_CompoundHPGL):
   '''Rectangle with round corners. Cannot be filled'''

   _scalable = _CompoundHPGL._scalable + ['width', 'height']

   def __init__(self, xy, width, height, interpolation_count=50, weight=3):
      _CompoundHPGL.__init__(self, xy) 
      self.width = width
      self.height = height
      self.interpolation_count = interpolation_count
      self.weight = weight

   @property
   def _subcommands(self):
      r = (self.width / 2, 0)
      tr= (self.width / 2, self.height / 2)
      t = (0, self.height / 2)
      tl= (-self.width / 2, self.height / 2)
      l = (-self.width / 2, 0)
      bl= (-self.width / 2, -self.height / 2)
      b = (0, -self.height / 2)
      br= (self.width / 2, -self.height / 2)

      weights = [1] + [self.weight] + [1]
      c1 = Bezier([r, tr, t], self.interpolation_count, weights, xy=self.xy)
      c2 = Bezier([t, tl, l], self.interpolation_count, weights, xy=self.xy)
      c3 = Bezier([l, bl, b], self.interpolation_count, weights, xy=self.xy)
      c4 = Bezier([b, br, r], self.interpolation_count, weights, xy=self.xy)

      result = _CompoundHPGL._subcommands.fget(self)
      result.extend([c1, c2, c3, c4])
      return result


