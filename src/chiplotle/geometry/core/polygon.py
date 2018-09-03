from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle.geometry.core.coordinatearray import CoordinateArray
from chiplotle.geometry.core.path import Path


class Polygon(Path):
    """A closed path."""

    def __init__(self, points, filled=False):
        Path.__init__(self, points)
        self.filled = filled

    @property
    def _preformat_points(self):
        """Points (coordinates) ready for formatting (conversion to HPGL)."""
        coords = self.points[:]
        coords.append(coords[0])
        return CoordinateArray(coords)


if __name__ == "__main__":
    from chiplotle import io

    p = Polygon([(0, 0), (2000, 0), (1000, 1000), (0, 500)], 0)
    print(p.points)
    print(p._preformat_points)

    io.view(p)
