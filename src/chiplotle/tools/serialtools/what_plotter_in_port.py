from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
from six import text_type, string_types

standard_library.install_aliases()
import serial
import time


def what_plotter_in_port(port, wait_time=10):
    """Check if there's a powered-on plotter in `port` port.

    - `port` : a string with port path or name.
    - `wait_time` : ``int`` maximum time in seconds to wait for
        plotter response.

    Returns the ID of the plotter found or None."""

    assert isinstance(wait_time, int)
    if not isinstance(port, (string_types, text_type)):
        raise TypeError("`port` must be a string.")

    from chiplotle.tools.serialtools import instantiate_serial_from_config_file

    ser = instantiate_serial_from_config_file(port)
    try:
        ser.flushInput()
        ser.flushOutput()
        ser.write(b"IN;")
        ser.write(b"OI;")
    except serial.serialutil.SerialException:
        return None

    t = time.time()
    while time.time() - t < wait_time:
        if ser.inWaiting() > 0:
            try:
                id = ser.readline(eol="\r").strip("\r")  # <-- old pyserial
            except:
                id = ser.readline().strip("\r")

            ## if not just a repeater...
            if id != "OI;":
                return id
