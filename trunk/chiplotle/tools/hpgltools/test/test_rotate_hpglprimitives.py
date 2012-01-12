from chiplotle import *
from chiplotle.hpgl.commands import *
import math
from py.test import raises

def test_rotate_hpglprimitives_01( ):
   t = [PU( ), PD( ), PA([(1, 1), (-1, 1)]), PR([(1, 1), (-1, 1)]), 
      ER((1, 2)), EA((1, 2)), CI(10)]
   hpgltools.rotate_hpglprimitives(t, math.pi / 2.0)
   assert len(t) == 7
   print t[2].xy
   ## NOTE: why is this not working?
   #assert t[2].xy == CoordinateArray([Coordinate(1, -1), Coordinate(1, 1)])

   
