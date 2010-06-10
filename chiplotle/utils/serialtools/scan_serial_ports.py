import platform

def scan_serial_ports( ):
   '''Scan for available ports. return a list of tuples (num, name).
   Based on the scan.py example from pySerial (http://pyserial.sf.net).
   '''
   from chiplotle.utils.serialtools import scan_serial_ports_linux
   from chiplotle.utils.serialtools import scan_serial_ports_windows
   #print platform.system( ).lower( )
   #if platform.system( ).lower( ) == 'windows': 
   if platform.system( ).lower( ).startswith('windows') or \
      platform.system( ).lower( ).startswith('cygwin'): 
      return scan_serial_ports_windows( )
   else:
      return scan_serial_ports_linux( )
