from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from builtins import open
from future import standard_library
standard_library.install_aliases()
def write_log_file(path):
    f = open(path, 'w')
    f.write('')
    f.close()
