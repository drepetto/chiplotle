#import serial

def scan_serial_ports_windows( ):
    from chiplotle.tools.serialtools import scan_serial_ports_from_list
    return scan_serial_ports_from_list(list(range(256)))
