from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from future import standard_library
standard_library.install_aliases()
def is_flat_list(lst):
    '''Returns True if list is flat, false otherwise.'''
    if isinstance(lst, (list, tuple)):
        for e in lst:
            if isinstance(e, (list, tuple)):
                return False
        else:
            return True
    else:
        return False
