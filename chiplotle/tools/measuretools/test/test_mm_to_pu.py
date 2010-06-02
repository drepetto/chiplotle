from chiplotle.tools.measuretools import *


def test_mm_to_pu_01( ):
   assert mm_to_pu(1) == 40
   assert mm_to_pu(0.5) == 40 / 2.0
   assert mm_to_pu(0) == 0


