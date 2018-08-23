from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from builtins import range
from future import standard_library

standard_library.install_aliases()


def difference(seq):
    """Returns the difference between consecutive elements in `seq`.
    i.e., first derivative.
    """
    result = []
    for i in range(len(seq) - 1):
        result.append(seq[i + 1] - seq[i])
    return type(seq)(result)
