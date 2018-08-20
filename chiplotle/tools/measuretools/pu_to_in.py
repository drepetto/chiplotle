from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

from future import standard_library
standard_library.install_aliases()
def pu_to_in(magnitude):
    '''Converts plotter units to inches.'''
    return magnitude / 1016.0
