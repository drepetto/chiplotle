from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from chiplotle.tools.measuretools import *


def test_pu_to_in_01( ):
    assert pu_to_in(1016) == 1
    assert pu_to_in(0) == 0


