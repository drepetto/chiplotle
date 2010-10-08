from chiplotle import *
import math
from py.test import raises

def test_rotate_hpglprimitives_01( ):
   '''Arguments must be _HPGLPrimitives.'''
   t = [Circle((1, 2), 100), 'PD;']
   assert raises(TypeError, 'hpgltools.rotate_hpglprimitives(t, math.pi / 2.0)')

def test_rotate_hpglprimitives_02( ):
   t = [PU( ), PD( ), PA((1, 1, -1, 1)), PR((1, 1, -1, 1)), ER((1, 2)), EA((1, 2)), CI(10)]
   hpgltools.rotate_hpglprimitives(t, math.pi / 2.0)
   assert len(t) == 7
   print t[2].xy
   ## NOTE: why is this not working?
   #assert t[2].xy == CoordinateArray([CoordinatePair(1, -1), CoordinatePair(1, 1)])

   
