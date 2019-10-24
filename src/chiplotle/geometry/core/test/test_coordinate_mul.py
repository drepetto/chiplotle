from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle import *
from pytest import raises


def test_coordinate__mul__01():
    """A Coordinate can be multiplied with a scalar."""
    a = Coordinate(1, 2)
    b = 2.5
    t = a * b
    assert isinstance(t, Coordinate)
    assert t is not a
    assert t == Coordinate(2.5, 5)


def test_coordinate__mul__02():
    """A Coordinate cannot be multiplied with a pair."""
    a = Coordinate(2, 3)
    with raises(TypeError):
        a * (2, 3)


def test_coordinate__mul__03():
    """A Coordinate can be multiplied with another Coordinate."""
    a = Coordinate(2, 3)
    t = a * Coordinate(2, 3)
    assert isinstance(t, Coordinate)
    assert t == Coordinate(4, 9)
