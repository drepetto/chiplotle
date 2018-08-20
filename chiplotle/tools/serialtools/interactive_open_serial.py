from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from builtins import input
from builtins import int
from future import standard_library
standard_library.install_aliases()
from chiplotle.tools.serialtools.scan_serial_ports import scan_serial_ports

## TODO: DELETE. No longer used.
def interactive_open_serial(baudrate, bytesize, parity, stopbits, timeout,
    xonxoff, rtscts):
    '''The function scans for all serial ports, lists them and prompts
    the user to select a port.  The function returns a Serial instance.
    '''
    ports = scan_serial_ports( )
    print("Available ports:\n")
    for k, port in list(ports.items( )):
        print("(%d) %s" % (k, port.portstr))
    ## get user's input...
    while True:
        sp = input("\nChoose serial port number: ")
        ## check response...
        try:
            sp = int(sp)
            if not sp in list(ports.keys( )):
                raise ValueError
            else:
                break
        except ValueError:
            print('Whoops! wrong port number. Try again...')
    ## configure port...
    selected_serial = ports[sp]
    selected_serial.baudrate = baudrate
    selected_serial.bytesize = bytesize
    selected_serial.parity = parity
    selected_serial.stopbits = stopbits
    selected_serial.timeout = timeout
    selected_serial.xonxoff = xonxoff
    selected_serial.rtscts = rtscts
    selected_serial.open( )
    print("Okay, opening %s." % selected_serial.portstr)
    return selected_serial
