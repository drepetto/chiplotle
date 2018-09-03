from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from builtins import int
from builtins import map
from builtins import str
from future import standard_library

standard_library.install_aliases()
import numbers
import operator
import math


class Coordinate(object):

    __slots__ = "_coords"

    #   def __new__(cls, *args):
    #      if len(args) == 1 and isinstance(args[0], Coordinate):
    #         return args[0]
    #      else:
    #         return super(Coordinate, cls).__new__(cls)

    def __init__(self, *coords):
        if coords and not isinstance(coords[0], numbers.Number):
            raise TypeError("Arguments must all be scalars")
        self._coords = list(coords)

    @property
    def xy(self):
        return self._coords[0:2]

    @property
    def x(self):
        return self.xy[0]

    @property
    def y(self):
        return self.xy[1]

    @property
    def magnitude(self):
        """The norm."""
        return math.sqrt(sum([c ** 2 for c in self._coords]))

    @property
    def normalized(self):
        return self / self.magnitude

    ## TODO: make multidimensional.
    @property
    def polar(self):
        from chiplotle.tools.mathtools.xy_to_polar import xy_to_polar

        return xy_to_polar(self.xy)

    @property
    def angle(self):
        return self.polar[1]

    ## TODO: make multidimensional.
    @property
    def perpendicular(self):
        return Coordinate(-self.y, self.x)

    ## OVERRIDES ##

    def __getitem__(self, arg):
        return self._coords[arg]

    def __iter__(self):
        for e in self._coords:
            yield e

    def __hash__(self):
        return hash(tuple(self._coords))

    def __len__(self):
        return len(self._coords)

    def __repr__(self):
        return "Coordinate({})".format(self._coords)

    def __str__(self):
        return "<%s>" % ",".join([str(c) for c in self._coords])

    ## math operators ##

    def __abs__(self):
        return Coordinate(*list(map(abs, self._coords)))

    def __add__(self, arg):
        if isinstance(arg, Coordinate):
            coords = list(map(operator.add, self._coords, arg._coords))
            return Coordinate(*coords)
        try:
            return arg.__radd__(self)
        except Exception:
            raise TypeError

    #   def __radd__(self, arg):
    #      return self + arg

    def __sub__(self, arg):
        if isinstance(arg, Coordinate):
            coords = list(map(operator.sub, self._coords, arg._coords))
            return Coordinate(*coords)
        try:
            return arg.__rsub__(self)
        except Exception:
            raise TypeError

    def __rsub__(self, arg):
        return -(self - arg)

    def __truediv__(self, arg):
        coords = [c / float(arg) for c in self._coords]
        return Coordinate(*coords)

    def __div__(self, arg):
        return self.__truediv__(arg)

    def __floordiv__(self, arg):
        coords = self.__div__(arg)._coords
        coords = [int(math.floor(c)) for c in coords]
        return Coordinate(*coords)

    def __mul__(self, arg):
        if not isinstance(arg, (Coordinate, int, float)):
            raise TypeError
        if isinstance(arg, Coordinate):
            coords = list(map(operator.mul, self._coords, arg._coords))
        else:
            coords = [c * arg for c in self._coords]
        return Coordinate(*coords)

    def __rmul__(self, arg):
        return self * arg

    def __eq__(self, arg):
        try:
            return self._coords == arg._coords
        except Exception:
            return False

    def __ne__(self, arg):
        return not (self == arg)

    def __neg__(self):
        coords = [-c for c in self._coords]
        return Coordinate(*coords)

    def __invert__(self):
        """Returns the perpendicular of self.
        http://mathworld.wolfram.com/PerpendicularCoordinate.html
        """
        return self.perpendicular


if __name__ == "__main__":

    c = Coordinate(1, 2, 3)
    cp = c + c
    cs = c - c
    cm = c * 2
    cd = c / 2
    cn = -c
    print("len(c) =", len(c))
    print(c)
    print(cp)
    print(cs)
    print(cm)
    print(cd)
