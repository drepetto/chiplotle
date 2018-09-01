from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle import *
import py.test


def test_pen_01():
    """Pen must take one argument at least."""

    assert py.test.raises(TypeError, "t = Pen( )")


def test_pen_02():
    t = Pen(2)

    assert t.number == 2
    assert t.acceleration == None
    assert t.force == None
    assert t.velocity == None
    assert t.thickness == None

    assert t.format == b"SP2;"


def test_pen_03():
    t = Pen(2, 3, 4, 5, 0.1)

    assert t.number == 2
    assert t.acceleration == 5
    assert t.force == 4
    assert t.velocity == 3
    assert t.thickness == 0.1

    assert t.format == b"SP2;AS5,2;FS4,2;VS3,2;PT0.10;"


def test_pen_04():
    t = Pen(2, 3, 4)

    assert t.number == 2
    assert t.acceleration == None
    assert t.force == 4
    assert t.velocity == 3
    assert t.thickness == None

    assert t.format == b"SP2;FS4,2;VS3,2;"
