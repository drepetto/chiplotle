from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle.geometry.core.path import Path


def path(points):
    """A simple path."""
    return Path(points)


## DEMO CODE
if __name__ == "__main__":
    from chiplotle.tools import io

    points = [(0, 0), (10, 10), (-10, 10), (-10, -10), (10, -10), (0, 0)]
    p = path(points)
    io.view(p)
