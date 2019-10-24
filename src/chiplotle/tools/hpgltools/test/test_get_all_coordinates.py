from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle import *
from chiplotle.hpgl.commands import *


def test_get_all_coordinates_01():
    """get_all_coordinates( ) works with _HPGLPrimitives."""
    t = [PA([(1, 2)]), PR([(1, 1)]), ER((1, 1)), CI(100)]
    c = hpgltools.get_all_coordinates(t)
    assert len(c) == 3
    assert c[0] == Coordinate(1, 2)
    assert c[1] == Coordinate(2, 3)
    assert c[2] == Coordinate(3, 4)
