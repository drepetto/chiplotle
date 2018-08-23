from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
import platform


def scan_serial_ports():
    """Scan for available ports. return a list of tuples (num, name).
    Based on the scan.py example from pySerial (http://pyserial.sf.net).
    """
    from chiplotle.tools.serialtools import scan_serial_ports_linux
    from chiplotle.tools.serialtools import scan_serial_ports_windows

    if platform.system().lower().startswith(
        "windows"
    ) or platform.system().lower().startswith("cygwin"):
        return scan_serial_ports_windows()
    else:
        return scan_serial_ports_linux()
