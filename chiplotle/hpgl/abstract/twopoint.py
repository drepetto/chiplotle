from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import map
from future import standard_library
standard_library.install_aliases()
from chiplotle.hpgl.abstract.hpglprimitive import _HPGLPrimitive
from chiplotle.geometry.core.coordinatearray import CoordinateArray

class _TwoPoint(_HPGLPrimitive):
    '''Abstract class for commands with 2 coordinate pairs: x1, y1, x2, y2.'''
    def __init__(self, coords=None):
        self.coords = coords
        if self.coords and len(self.coords) != 2:
                raise ValueError('Only two coordinate pairs allowed.')


    def coords( ):
        def fget(self):
            return self._coords
        def fset(self, arg):
            self._coords = CoordinateArray(arg)
        return property(**locals())
    coords = coords()


    @property
    def format(self):
        if self.coords:
            coords = self.coords[0].xy + self.coords[1].xy
            coords = list(map(str, coords))
            coords = ','.join(coords)
            return '%s%s%s' % (self._name, coords, _HPGLPrimitive._terminator)
        else:
            return '%s%s' % (self._name, _HPGLPrimitive._terminator)

