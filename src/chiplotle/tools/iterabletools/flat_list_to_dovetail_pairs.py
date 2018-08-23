from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from builtins import zip
from future import standard_library

standard_library.install_aliases()


def flat_list_to_dovetail_pairs(lst):
    return list(zip(lst[0:-1], lst[1:]))
