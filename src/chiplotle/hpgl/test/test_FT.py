from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle.hpgl.commands import FT
from pytest import raises


def test_FT_01():
    t = FT()
    assert t.type is None
    assert t.space is None
    assert t.angle is None
    assert t.format == b"FT;"


def test_FT_02():
    t = FT(2)
    assert t.type == 2
    assert t.format == b"FT2;"


def test_FT_03():
    t = FT(2, .23)
    assert t.type == 2
    assert t.space == 0.23
    assert t.format == b"FT2,0.23;"


def test_FT_04():
    t = FT(2, .23, 80.5)
    assert t.type == 2
    assert t.space == 0.23
    assert t.angle == 80.5
    assert t.format == b"FT2,0.23,80.50;"


def test_FT_05():
    """Mandatory parameters missing raises Warning at format time."""
    t = FT()
    t.space = .23
    assert t.type is None
    assert t.space == 0.23
    assert t.angle is None
    with raises(Warning):
        t.format
