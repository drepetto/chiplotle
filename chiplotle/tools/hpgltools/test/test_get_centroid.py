from chiplotle import *

def test_get_centroid_01( ):
   g = [PA([(0, 0), (10, 10), (0, 10), (10, 0)])]
   t = hpgltools.get_centroid(g)
   assert t == CoordinatePair(5, 5)


def test_get_centroid_02( ):
   g = Rectangle((5, 5), 10, 10)
   t = hpgltools.get_centroid(g)
   assert t == CoordinatePair(5, 5)
