from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
#import serial

from builtins import range
from future import standard_library
standard_library.install_aliases()
def scan_serial_ports_windows( ):
    from chiplotle.tools.serialtools import scan_serial_ports_from_list
    return scan_serial_ports_from_list(list(range(256)))
