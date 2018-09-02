from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import open
from future import standard_library

standard_library.install_aliases()
from chiplotle.hpgl.abstract.hpgl import _HPGL


def save_hpgl(expr, filename):
    """Save text HPGL from Chiplotle-HPGL.

    - `expr` can be an iterable (e.g., list) or a Chiplotle-HPGL object.
    - `filename` the full file name, including path and extension
      (usually .hpgl or .plt)
    """
    ## parse expr; extract pure text HPGL commands.
    hpgl = []
    if isinstance(expr, (list, tuple)):
        for o in expr:
            if not isinstance(o, _HPGL):
                raise TypeError("Expected HPGL expression but got {}".format(o))
            hpgl.append(o.format)
    else:
        hpgl.append(expr.format)

    ## create HPGL file
    file = open("%s" % filename, "w")
    file.writelines([command.decode("ascii") for command in hpgl])
    file.close()
