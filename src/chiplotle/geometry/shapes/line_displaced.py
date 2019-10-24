from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from builtins import range
from future import standard_library

standard_library.install_aliases()
from chiplotle.geometry.shapes.path import path
from chiplotle.geometry.transforms.perpendicular_displace import perpendicular_displace


def line_displaced(start_coord, end_coord, displacements):
    """Returns a Path defined as a line spanning points `start_coord` and
    `end_coord`, displaced by scalars `displacements`.
    The number of points in the path is determined by the lenght of
    `displacements`.
    """
    p = path([start_coord, end_coord])
    perpendicular_displace(p, displacements)
    return p


if __name__ == "__main__":
    from chiplotle import *
    import math

    disp = [math.sin(i ** 0.7 / 3.14159 * 2) * 100 for i in range(200)]
    line = line_displaced(Coordinate(0, 0), Coordinate(1000, 1000), disp)

    io.view(line)
