from chiplotle import *
from chiplotle.tools.hpgltools import relativize

def test_relativize_01( ):
   t = [PA((1, 1)), PA((2, 2)), PA((3, 2))]
   r = relativize(t)
   'r = [PA((0, 0)), PR((1, 1)), PR((1, 1)), PR((1, 0))]'
   assert len(r) == len(t) + 1
   assert isinstance(r[0], PA)
   assert isinstance(r[1], PR)
   assert isinstance(r[2], PR)
   assert isinstance(r[3], PR)
   assert all(r[0].xy == (0, 0))
   assert all(r[1].xy == (1, 1))
   assert all(r[2].xy == (1, 1))
   assert all(r[3].xy == (1, 0))


def test_relativize_02( ):
   t = [PA((1, 1)), PU((2, 2)), PU((3, 2))]
   r = relativize(t)
   'r = [PA((0, 0)), PR((1, 1)), PU((1, 1)), PU((1, 0))]'
   assert len(r) == 4
   assert isinstance(r[0], PA)
   assert isinstance(r[1], PR)
   assert isinstance(r[2], PU)
   assert isinstance(r[3], PU)
   assert all(r[0].xy == (0, 0))
   assert all(r[1].xy == (1, 1))
   assert all(r[2].xy == (1, 1))
   assert all(r[3].xy == (1, 0))
