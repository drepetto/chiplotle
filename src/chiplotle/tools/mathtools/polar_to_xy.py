from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle.geometry.core.coordinate import Coordinate
import math


# def polar_to_xy(*args):
def polar_to_xy(args):
    """Converts polar (r, A) to Cartesian (x y) coordinates,
    where r is the radius and A is the angle in radians.
    """
    try:
        r, A = tuple(Coordinate(*args))
    except:
        raise TypeError("`args` must be an (r, A) tuple.")
    x = r * math.cos(A)
    y = r * math.sin(A)
    return (x, y)
