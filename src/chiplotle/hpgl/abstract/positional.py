from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle.hpgl.abstract.hpglprimitive import _HPGLPrimitive
from chiplotle.geometry.core.coordinatearray import Coordinate


class _Positional(_HPGLPrimitive):
    """For those primitive HPGL commands that have an (x, y) position pair."""

    _scalable = ["xy"]

    def __init__(self, xy):
        self.xy = xy

    ## PUBLIC ATTRIBUTES ##

    def xy():
        def fget(self):
            return self._coords

        def fset(self, arg):
            if not len(arg) == 2:
                raise ValueError("Positional HPGL commands are 2D")
            self._coords = Coordinate(*arg)

        return property(**locals())

    xy = xy()

    def x():
        def fget(self):
            return self._coords.x

        def fset(self, arg):
            self.xy = Coordinate(arg, self.y)

        return property(**locals())

    x = x()

    def y():
        def fget(self):
            return self._coords.y

        def fset(self, arg):
            self.xy = Coordinate(self.x, arg)

        return property(**locals())

    y = y()

    ### FORMATTING ###

    @property
    def format(self):
        if isinstance(self.x, int) and isinstance(self.y, int):
            coordinates = b"%i,%i" % (self.x, self.y)
        else:
            coordinates = b"%.2f,%.2f" % (self.x, self.y)
        return b"%s%s%s" % (self._name, coordinates, _HPGLPrimitive._terminator)
