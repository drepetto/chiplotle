from chiplotle import *
from chiplotle.hpgl.commands import *

def test_convert_relatives_to_absolutes_01( ):
   g = [PA([(1, 2)]), PR([(1, 1), (1, 1)])]
   t = hpgltools.convert_relatives_to_absolutes(g)
   assert len(t) == 2
   assert t[0] == PA([(1, 2)])
   assert t[1] == PA([(2, 3), (3, 4)])


def test_convert_relatives_to_absolutes_02( ):
   '''Initial absolute position is set to (0, 0) when absolute commands are absent before PR.'''
   g = [PR([(1, 1), (1, 1)])]
   t = hpgltools.convert_relatives_to_absolutes(g)
   assert len(t) == 1
   assert t[0] == PA([(1, 1), (2, 2)])


def test_convert_relatives_to_absolutes_03( ):
   '''Edges and archs work.'''
   g = [ER((1, 1)), RR((1, 1)), AR((1, 1), 40), EA((0, 0))]
   t = hpgltools.convert_relatives_to_absolutes(g)
   assert len(t) == 4
   assert t[0] == EA((1, 1))
   assert t[1] == RA((2, 2))
   assert t[2] == AA((3, 3), 40)
   assert t[3] == EA((0, 0))

