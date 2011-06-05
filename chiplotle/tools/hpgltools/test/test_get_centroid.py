from chiplotle import *
from chiplotle.hpgl.commands import PA

def test_get_centroid_01( ):
   g = [PA([(0, 0), (10, 10), (0, 10), (10, 0)])]
   t = hpgltools.get_centroid(g)
   assert t == Coordinate(5, 5)


