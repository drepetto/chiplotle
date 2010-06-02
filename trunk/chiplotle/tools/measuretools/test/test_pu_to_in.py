from chiplotle.tools.measuretools import *


def test_pu_to_in_01( ):
   assert pu_to_in(1016) == 1
   assert pu_to_in(0) == 0


