from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from chiplotle.hpgl.abstract.hpglprimitive import _HPGLPrimitive
from chiplotle.geometry.core.coordinatearray import CoordinateArray


class _PenPlot(_HPGLPrimitive):
    '''For those primitive HPGL commands that can take multiple
    x,y,x,y,... coordinates.
    g.e., PA( ).'''

    _scalable = ['xy']

    def __init__(self, xy):
        self.xy = xy

    ### MANAGED ATTRIBUTES ###

    def xy( ):
        def fget(self):
            return self._coords
        def fset(self, arg):
            self._coords = CoordinateArray(arg)
        return property(**locals())
    xy = xy()

    def x( ):
        def fget(self):
            return self._coords.x
        def fset(self, arg):
            self.xy.x = arg
        return property(**locals())
    x = x()

    def y( ):
        def fget(self):
            return self._coords.y
        def fset(self, arg):
            self.xy.y = arg
        return property(**locals())
    y = y()


    ### FORMATTING ###

    @property
    def format(self):
        if self.xy.dtype == int:
            coordinates = ['%i,%i' % tuple(p) for p in self.xy]
        else:
            coordinates = ['%.2f,%.2f' % tuple(p) for p in self.xy]
        return '%s%s%s' % (self._name, ','.join(coordinates),
            _HPGLPrimitive._terminator)
