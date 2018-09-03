from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle.hpgl.commands import *
import pytest


def test_AA_01():
    t = AA((0, 0), 180)

    assert t.angle == 180
    assert t.chordtolerance is None
    assert t.format == b"AA0,0,180.00;"


def test_AA_02():
    t = AA((0, 0), 180, 45)

    assert t.angle == 180
    assert t.chordtolerance == 45
    assert t.format == b"AA0,0,180.00,45.00;"


def test_AA_03():
    """AA must take at least two arguments: position and angle."""
    assert pytest.raises(TypeError, "AA((0, 0))")


def test_AA_format_01():
    """Ints format as ints."""
    t = AA((0, 0), 180)

    assert t.format == b"AA0,0,180.00;"


def test_AA_format_02():
    """Floats format as floats."""
    t = AA((0, 0.0), 180)

    assert t.format == b"AA0.00,0.00,180.00;"


def test_AA_angle_01():
    """Angle must be between -360 and 360."""
    assert pytest.raises(ValueError, "AA((0, 0), 1200)")


## eq ##


def test_AA__eq__01():
    assert AA((1, 2), 120) == AA((1, 2), 120)
