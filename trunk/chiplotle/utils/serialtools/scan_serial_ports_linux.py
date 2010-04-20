import glob
#import serial

def scan_serial_ports_linux( ):
   from chiplotle.utils.serialtools import scan_serial_ports_from_list
   ports = glob.glob('/dev/ttyS*') + glob.glob('/dev/ttyUSB*') +\
      glob.glob('/dev/tty.USA*') + glob.glob('/dev/tty.KeySerial*')
   return scan_serial_ports_from_list(ports)
#   result = { }
#   ## keep track of previously opened ports to avoid including aliases
#   ## in our list...
#   ports_opened = [ ]
#   for i, port in enumerate(ports):
#      try:
#         s = serial.Serial(port)
#         ports_opened.append(s)
#         result[i] = s.portstr
#         #result[i] = s
#         #s.close( )
#      except serial.SerialException:
#         pass
#   ## gracefully close all open ports...
#   for port in ports_opened:
#      port.close( )
#   return result
