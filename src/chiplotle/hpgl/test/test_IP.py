from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import pytest
from future import standard_library

standard_library.install_aliases()
from chiplotle import *
from chiplotle.hpgl.commands import IP


def test_IP_01():
    """IP can be empty."""
    t = IP()
    assert t.format == b"IP;"
    assert isinstance(t.coords, CoordinateArray)


def test_IP_02():
    """IP cannot take a flat tuple."""
    with pytest.raises(ValueError):
        IP((1, 2, 3, 4))


def test_IP_03():
    """IP can take a tuple or list of pairs."""
    t = IP([(1, 2), (3, 4)])
    assert t.coords == CoordinateArray([(1, 2), (3, 4)])


def test_IP_04():
    """IP can take two an only two coordinate pairs."""
    with pytest.raises(ValueError):
        t = IP([Coordinate(1, 2)])

    with pytest.raises(ValueError):
        IP([Coordinate(1, 2), Coordinate(3, 4), Coordinate(5, 6)])


def test_IP_05():
    """Coordinates of IP can be reset."""
    t = IP()
    t.coords = (Coordinate(5, 6), Coordinate(7, 8))
    assert isinstance(t.coords, CoordinateArray)
    assert t.coords == CoordinateArray([(5, 6), (7, 8)])
