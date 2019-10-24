from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle.hpgl.commands import CP


def test_CP_01():
    """Empty initialization."""
    t = CP()
    assert t.spaces is None
    assert t.lines is None
    assert t.format == b"CP;"


def test_CP_02():
    """Initialize with spaces only."""
    t = CP(2)
    assert t.spaces == 2
    assert t.lines is None
    assert t.format == b"CP2;"


def test_CP_03():
    """Initialize with spaces and lines."""
    t = CP(2, 1)
    assert t.spaces == 2
    assert t.lines == 1
    assert t.format == b"CP2,1;"
