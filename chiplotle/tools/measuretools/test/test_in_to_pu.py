from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from chiplotle.tools.measuretools import *


def test_in_to_pu_01( ):
    assert in_to_pu(1) == 1016
    assert in_to_pu(0.5) == 1016 / 2.0
    assert in_to_pu(0) == 0


