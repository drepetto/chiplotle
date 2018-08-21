from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from future import standard_library

standard_library.install_aliases()


def in_to_pu(magnitude):
    """Converts inches to plotter units."""
    return magnitude * 1016.0  ## == magnitude / 0.025 * 10 * 2.54
