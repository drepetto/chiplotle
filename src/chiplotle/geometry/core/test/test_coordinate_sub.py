from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle import *
from pytest import raises


def test_coordinate__sub__01():
    """Coordinate pair can substract with other coordinate pairs."""
    a = Coordinate(1, 2)
    b = Coordinate(0.5, 0.5)
    t = a - b
    assert isinstance(t, Coordinate)
    assert t == Coordinate(0.5, 1.5)


def test_coordinate__sub__02():
    """Coordinate pair cannot substract a tuple."""
    a = Coordinate(1, 2)
    with raises(TypeError):
        a - (0.5, 0.5)


def test_coordinate__rsub__02():
    """A tuple cannot substract a Coordinate."""
    a = Coordinate(1, 2)
    with raises(TypeError):
        (0.5, 0.5) - a


def test_coordinate__sub__03():
    """An int cannot be substracted from a Coordinate."""
    a = Coordinate(1, 2)
    with raises(TypeError):
        a - 1


def test_coordinate__rsub__03():
    """A Coordinate cannot be substracted from an int."""
    a = Coordinate(1, 2)
    with raises(TypeError):
        1 - a


def test_coordinate__sub__04():
    """An float cannot be substracted from a Coordinate."""
    a = Coordinate(1, 2)
    with raises(TypeError):
        t = a - 1.5


def test_coordinate__rsub__04():
    """A Coordinate cannot be substracted from a float."""
    a = Coordinate(1, 2)
    with raises(TypeError):
        t = 1.5 - a
