from chiplotle.tools.measuretools import *


def test_pu_to_mm_01( ):
   assert pu_to_mm(1) == 0.025
   assert pu_to_mm(40) == 1
   assert pu_to_mm(0) == 0

