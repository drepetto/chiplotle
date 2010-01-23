from chiplotle.utils.scan_serial_ports_linux import scan_serial_ports_linux
from chiplotle.utils.scan_serial_ports_windows import scan_serial_ports_windows
import platform

def scan_serial_ports( ):
   """Scan for available ports. return a list of tuples (num, name).
   Based on the scan.py example from pySerial (http://pyserial.sf.net).
   """
   if platform.system( ).lower( ) == 'windows': 
      return scan_serial_ports_windows( )
   else:
      return scan_serial_ports_linux( )
