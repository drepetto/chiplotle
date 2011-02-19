from chiplotle import *

def test_get_centroid_01( ):
   g = [PA([(0, 0), (10, 10), (0, 10), (10, 0)])]
   t = hpgltools.get_centroid(g)
   assert t == Coordinate(5, 5)


