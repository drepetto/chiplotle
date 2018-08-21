from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from future import standard_library

standard_library.install_aliases()


def cumsum(lst):
    """Returns the cumulative sum of the values in `lst`."""

    try:
        import numpy

        return numpy.cumsum(lst)
    except ImportError:
        r = 0
        result = []
        for n in lst:
            r += n
            result.append(r)
        return result
