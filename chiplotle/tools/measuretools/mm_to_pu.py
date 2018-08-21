from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

from future import standard_library

standard_library.install_aliases()


def mm_to_pu(magnitude):
    """Converts millimeters to plotter units."""
    return magnitude / 0.025
