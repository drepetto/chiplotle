from chiplotle.tools.measuretools import *


def test_pu_to_cm_01( ):
   assert pu_to_cm(1) == 0.0025
   assert pu_to_cm(400) == 1
   assert pu_to_cm(0) == 0


