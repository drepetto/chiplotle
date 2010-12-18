from chiplotle.hpgl.compound.hpglcompoundshape import _HPGLCompoundShape
from chiplotle.hpgl.coordinate import Coordinate
from chiplotle.hpgl.commands import PU, PD, PA
from chiplotle.tools.mathtools import superformula
from math import pi


class Supershape(_HPGLCompoundShape):
   '''Supershape, generated using the superformula
   first proposed by Johan Gielis.
   arguments are:
   w - width
   h - height
   a=b=1.0, m, n1, n2, n3 - controls of shape
   '''

   _scalable = _HPGLCompoundShape._scalable + ['width', 'height']

   def __init__(self, xy, w, h, m, n1, n2, n3, 
      point_count=1000, percentage=1.0, a=1.0, b=1.0, range=None):

      xy = xy or (0, 0)
      _HPGLCompoundShape.__init__(self, xy)
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
       
   @property
   def points(self):
      ## compute points...
      phis = [i * self.range / self.point_count 
         for i in range(int(self.point_count * self.percentage))]
      f = lambda x: superformula(self.a, self.b, self.m, 
         self.n1, self.n2, self.n3, x)
      the_points = map(f, phis)
      ## scale and transpose...
      path = [ ]
      for x, y in the_points:
         x = x * self.width + self.x
         y = y * self.height + self.y
         path.append(Coordinate(x, y))
      return [path]
      
   @property
   def _subcommands(self):
      path = self.points[0]
      ## generate HPGL commands...
      result = _HPGLCompoundShape._subcommands.fget(self)
      result.append(PU( ))
      result.append(PA(path[0]))
      result.append(PD( ))
      for position in path[1:]:
         result.append(PA(position))
      result.append(PU( ))
      return result     
