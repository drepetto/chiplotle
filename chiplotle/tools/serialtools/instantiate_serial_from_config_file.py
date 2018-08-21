from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle.core.cfg.get_config_value import get_config_value
import serial


def instantiate_serial_from_config_file(port):
    """Instantiates a Serial with port `port` and serial config
    parameters read from the configuration file."""
    bytesize = get_config_value("bytesize")
    parity = get_config_value("parity")
    stopbits = get_config_value("stopbits")
    timeout = get_config_value("timeout")
    xonxoff = get_config_value("xonxoff")
    rtscts = get_config_value("rtscts")
    ser = serial.Serial(
        port=port,
        bytesize=bytesize,
        parity=parity,
        stopbits=stopbits,
        timeout=timeout,
        xonxoff=xonxoff,
        rtscts=rtscts,
    )
    return ser
