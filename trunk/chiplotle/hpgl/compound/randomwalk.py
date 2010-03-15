from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.commands import PU, PA, PD, PR
from chiplotle.utils.geometry import polar2xy
import math
import random


class RandomWalk(_CompoundHPGL):
   '''Random Walk.'''
   def __init__(self, xy, steps, step_size=500):
      _CompoundHPGL.__init__(self, xy) 
      self.steps = steps
      self.step_size = step_size

   @property
   def _subcommands(self):
      result = _CompoundHPGL._subcommands.fget(self)
      result += [ PU( ), PA(self.xyabsolute), PD( ) ]
      for i in range(self.steps):
        A = random.random() * math.pi * 2
        r = self.step_size
        xy = polar2xy(r,A)
        result.append( PR(xy) )
      result.append( PU() )
      return result


