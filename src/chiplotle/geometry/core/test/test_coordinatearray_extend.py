from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle import *
from pytest import raises


def test_coordinatearray_extend_01():
    """CoordinateArray cannot be extended with a list of (x, y) pairs."""
    t = CoordinateArray()
    with raises(TypeError):
        t.extend([(0, 0), (1, 2)])


def test_coordinatearray_extend_02():
    """CoordinateArray can be extended with a list of Coordinate."""
    t = CoordinateArray()
    t.extend([Coordinate(0, 0), Coordinate(3, 2)])
    assert len(t) == 2
    assert isinstance(t[0], Coordinate)
    assert isinstance(t[1], Coordinate)


def test_coordinatearray_extend_03():
    """Mixtures are not allowed."""
    t = CoordinateArray()
    with raises(TypeError):
        t.extend([Coordinate(0, 0), (3, 2)])
