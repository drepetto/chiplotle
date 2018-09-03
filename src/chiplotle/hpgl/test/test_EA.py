from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle import *
from chiplotle.hpgl.commands import EA

from pytest import raises


def test_EA_01():
    """EA cannot initialize with a scalar."""
    with raises(TypeError):
        t = EA(1)


def test_EA_02():
    """EA cannot initialize with a list of length > 2."""
    with raises(ValueError):
        t = EA([1, 2, 3, 4])


def test_EA_03():
    """EA can initialize with a list of length 2."""
    t = EA([1, 2])
    assert t.xy == Coordinate(1, 2)
    assert t.format == b"EA1,2;"
