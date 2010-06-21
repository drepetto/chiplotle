import glob
#import serial

def scan_serial_ports_linux( ):
   from chiplotle.tools.serialtools import scan_serial_ports_from_list
   ## NOTE: there are also /dev/tty.PL2303-xxxx ports. Should we assume
   ## all /dev/tty.* devices are valid? or should we just add
   ## /dev/tty.PL* to the list? will do the former and see what happens.
   ports = glob.glob('/dev/ttyS*') + glob.glob('/dev/ttyUSB*') +\
      glob.glob('/dev/tty.*')
      #glob.glob('/dev/tty.USA*') + glob.glob('/dev/tty.KeySerial*')
   return scan_serial_ports_from_list(ports)
