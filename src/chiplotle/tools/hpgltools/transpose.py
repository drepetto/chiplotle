from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle.hpgl.abstract.hpgl import _HPGL
from chiplotle.tools.hpgltools.is_primitive_absolute import is_primitive_absolute
from chiplotle.geometry.core.coordinate import *


def _transpose_command(arg, val):
    from chiplotle.tools.iterabletools.ispair import ispair

    val = Coordinate(*val)
    if is_primitive_absolute(arg):
        arg.xy = arg.xy + val


def transpose(arg, val):
    if isinstance(arg, _HPGL):
        _transpose_command(arg, val)
    elif isinstance(arg, (list, tuple)):
        for c in arg:
            _transpose_command(c, val)
