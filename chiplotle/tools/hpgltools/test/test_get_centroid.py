from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from chiplotle import *
from chiplotle.hpgl.commands import PA

def test_get_centroid_01( ):
    g = [PA([(0, 0), (10, 10), (0, 10), (10, 0)])]
    t = hpgltools.get_centroid(g)
    assert t == Coordinate(5, 5)


