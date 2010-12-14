from chiplotle.hpgl.compound.hpglcompoundshape import _HPGLCompoundShape
from chiplotle.hpgl.commands import PU, PA, PD, PR
from chiplotle.tools.mathtools import polar_to_xy
import math
import random


class RandomWalk(_HPGLCompoundShape):
   '''Random Walk.'''
   def __init__(self, xy, steps, step_size=500):
      _HPGLCompoundShape.__init__(self, xy) 
      self.steps = steps
      self.step_size = step_size
      self.the_points = []
      self.two_pi = math.pi * 2

   @property
   def points(self):
      if len(self.the_points) == 0:
        for i in range(self.steps):
           A = random.random() * self.two_pi
           r = self.step_size
           xy = polar_to_xy(r,A)
           self.the_points.append(xy)
      
      return [self.the_points]
   
   @property
   def _subcommands(self):
      
      rand_points = self.points[0]
      
      result = _HPGLCompoundShape._subcommands.fget(self)
      result.append(PD( ))
      for point in rand_points:
        result.append( PR(point) )
      result.append( PU() )
      return result


