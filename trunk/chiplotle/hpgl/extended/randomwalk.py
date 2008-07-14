from chiplotle.hpgl.extended.extended import _ExtendedHPGL
from chiplotle.hpgl.commands import PU, PA, PD, PR
from chiplotle.utils.geometry import polar2xy
import math
import random


class RandomWalk(_ExtendedHPGL):
   '''Random Walk.'''
   def __init__(self, x, y, steps, stepSize=500):
      _ExtendedHPGL.__init__(self, (x, y)) 
      self.steps = steps
      self.stepSize = stepSize

   @property
   def _subcommands(self):
      result = _ExtendedHPGL._subcommands.fget(self)
      result += [ PU( ), PA(self.xyabsolute), PD( ) ]
      for i in range(self.steps):
        A = random.random() * math.pi * 2
        r = self.stepSize
        xy = polar2xy(r,A)
        result.append( PR(xy) )
      result.append( PU() )
      return result


