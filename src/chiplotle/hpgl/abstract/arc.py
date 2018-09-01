from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle.hpgl.abstract.positional import _Positional
from chiplotle.hpgl.abstract.hpglprimitive import _HPGLPrimitive


class _Arc(_Positional):
    def __init__(self, xy, angle, chordtolerance=None):
        self.angle = angle
        self.chordtolerance = chordtolerance
        _Positional.__init__(self, xy)

    def angle():
        def fget(self):
            return self._angle

        def fset(self, arg):
            if abs(arg) > 360:
                raise ValueError("angle must be between -360 and 360.")
            self._angle = arg

        return property(**locals())

    angle = angle()

    @property
    def format(self):
        if isinstance(self.x, int) and isinstance(self.y, int):
            coordinates = b"%i,%i" % (self.x, self.y)
        else:
            coordinates = b"%.2f,%.2f" % (self.x, self.y)
        result = b"%s%s,%.2f" % (self._name, coordinates, self.angle)
        if self.chordtolerance:
            result += b",%.2f" % self.chordtolerance
        result += _HPGLPrimitive._terminator
        return result
