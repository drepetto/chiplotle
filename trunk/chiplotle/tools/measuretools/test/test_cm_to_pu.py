from chiplotle.tools.measuretools import *


def test_cm_to_pu_01( ):
   assert cm_to_pu(1) == 400
   assert cm_to_pu(0) == 0

