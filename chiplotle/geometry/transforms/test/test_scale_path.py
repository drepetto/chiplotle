from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle import *
import py.test


def test_scale_path_01():
    t = Path([(0, 0), (1, 1)])
    assert t.points == CoordinateArray([(0, 0), (1, 1)])
    scale(t, 2, Coordinate(0, 0))
    assert t.points == CoordinateArray([(0, 0), (2, 2)])


def test_scale_path_02():
    t = Path([(0, 0), (1, 1)])
    scale(t, 2, Coordinate(1, 1))
    assert t.points == CoordinateArray([(-1, -1), (1, 1)])
