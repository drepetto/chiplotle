from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.commands import PU, PD, PA
from chiplotle.tools.mathtools import superformula
from math import pi


class Supershape(_CompoundHPGL):
   '''Supershape, generated using the superformula
   first proposed by Johan Gielis.
   arguments are:
   w - width
   h - height
   a=b=1.0, m, n1, n2, n3 - controls of shape
   '''

   _scalable = _CompoundHPGL._scalable + ['width', 'height']

   def __init__(self, xy, w, h, m, n1, n2, n3, 
      point_count=1000, percentage=1.0, a=1.0, b=1.0, range=None, pen=None):

      xy = xy or (0, 0)
      _CompoundHPGL.__init__(self, xy, pen)
      self.width = w
      self.height = h
      self.m = m
      self.n1 = n1
      self.n2 = n2
      self.n3 = n3
      self.a = a
      self.b = b
      self.point_count = point_count
      self.percentage = percentage
      self.range = range or (pi * 2)
      self.x, self.y = xy
       

   def _get_point_coordinates(self):
      ## compute points...
      phis = [i * self.range / self.point_count 
         for i in range(int(self.point_count * self.percentage))]
      f = lambda x: superformula(self.a, self.b, self.m, 
         self.n1, self.n2, self.n3, x)
      points = map(f, phis)
      ## scale and transpose...
      path = [ ]
      for x, y in points:
         x = x * self.width + self.x
         y = y * self.height + self.y
         path.append((x, y))
      return path
      
   @property
   def _subcommands(self):
      path = self._get_point_coordinates( )
      ## generate HPGL commands...
      result = _CompoundHPGL._subcommands.fget(self)
      result.append(PU( ))
      result.append(PA(path[0]))
      result.append(PD( ))
      for position in path[1:]:
         result.append(PA(position))
      result.append(PU( ))
      return result     
