from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from builtins import zip
from builtins import range
from future import standard_library

standard_library.install_aliases()
from chiplotle.tools.mathtools.interpolate_linear import interpolate_linear
from chiplotle.geometry.core.coordinatearray import CoordinateArray


def split_vector_equidistantly(vector, count):
    """Splits a vector/coordinate into `count` parts.
    Returns a CoordinateArray with the new Coordinate segments.

    >>> split_vector_equidistantly(Coordinate(-10, 12))
    CoordinateArray(<0,0>, <-2.5,3.0>, <-5.0,6.0>, <-7.5,9.0>, <-10,12>)
    """
    xs = [interpolate_linear(0, vector.x, i / count) for i in range(1, count)]
    ys = [interpolate_linear(0, vector.y, i / count) for i in range(1, count)]
    coords = [(0, 0)] + list(zip(xs, ys)) + [vector]
    return CoordinateArray(coords)


if __name__ == "__main__":
    from chiplotle import Coordinate

    v = Coordinate(-10, 12)
    c = 4
    print(split_vector_equidistantly(v, c))
