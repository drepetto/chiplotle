from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

from future import standard_library
standard_library.install_aliases()
def pu_to_cm(magnitude):
    '''Converts plotter units to centimeters.'''
    return magnitude / 400.0
