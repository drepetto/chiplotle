from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle.tools.measuretools import *


def test_pu_to_mm_01():
    assert pu_to_mm(1) == 0.025
    assert pu_to_mm(40) == 1
    assert pu_to_mm(0) == 0
