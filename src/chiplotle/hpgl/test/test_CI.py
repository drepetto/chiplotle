from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle.hpgl.commands import CI
from pytest import raises


def test_CI_01():
    """CI must have at least one argument (radius)."""
    with raises(TypeError):
        CI()


def test_CI_02():
    """CI can take only radius argument."""
    t = CI(1)
    assert t.radius == 1


def test_CI_03():
    """CI takes at most 2 arguments: radius and chord angle."""
    t = CI(1, 90)
    assert t.radius == 1
    assert t.chordangle == 90
    assert t.format == b"CI1.00,90.00;"


## _scalable ##


def test_CI_scalable_01():
    assert CI._scalable == ["radius"]
