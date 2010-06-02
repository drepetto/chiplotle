from chiplotle.tools.measuretools import *


def test_in_to_pu_01( ):
   assert in_to_pu(1) == 1016
   assert in_to_pu(0.5) == 1016 / 2.0
   assert in_to_pu(0) == 0


