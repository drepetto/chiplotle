from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle.hpgl.commands import DR
from pytest import raises


def test_DR_01():
    t = DR()

    assert t.run == t.rise == None
    assert t.format == b"DR;"


def test_DR_02():
    """both run and rise (or none) must be set for formatting."""

    t = DR(23)

    assert t.run == 23
    assert t.rise == None
    with raises(Warning):
        t.format


def test_DR_03():
    """run can be 0."""

    t = DR(0, 25.3)

    assert t.run == 0
    assert t.rise == 25.3
    assert t.format == b"DR0.00,25.30;"


def test_DR_04():
    """rise can be 0."""

    t = DR(10, 0)

    assert t.run == 10
    assert t.rise == 0
    assert t.format == b"DR10.00,0.00;"
