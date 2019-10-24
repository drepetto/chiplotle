from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle.geometry.core.transformlock import TransformLock


def lock_group(shapes, lock_transforms):
    t = TransformLock(shapes, lock_transforms)
    return t


## ~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    from chiplotle.geometry.shapes.square import square
    from chiplotle.geometry.core.group import Group
    from chiplotle.geometry.transforms.rotate import rotate
    from chiplotle.geometry.transforms.offset import offset
    from chiplotle import io
    import math

    r1 = square(100)
    r2 = square(150)
    l = lock_group([r2], ["rotate"])
    g = Group([r1, l])
    offset(g, (200, 0))
    rotate(g, math.pi / 4)
    io.view(g)
