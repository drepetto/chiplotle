from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from chiplotle import *
import copy

def test_perpendicular_noise_path_01( ):
    c  = circle(1000, 200)
    cc = copy.deepcopy(c)
    perpendicular_noise(c, 360)
    assert c.points != cc.points
    assert c.points is not cc.points

