from chiplotle.cfg.read_config_file import read_config_file
from chiplotle.utils.interactive_open_serial import interactive_open_serial
import serial

def instantiate_serial(port=None, baudrate=9600, bytesize=8, 
   parity='N', stopbits=1, timeout=1, xonxoff=0, rtscts=0):

   if not port:
      port = read_config_file( )['serial_port']
   if port:
      ser = serial.Serial(port, baudrate = baudrate, bytesize = bytesize,
         parity = parity, stopbits = stopbits, timeout = timeout,
         xonxoff = xonxoff, rtscts = rtscts)
   else:
      ser = interactive_open_serial(baudrate = baudrate, bytesize = bytesize,
         parity = parity, stopbits = stopbits, timeout = timeout, 
         xonxoff = xonxoff, rtscts = rtscts)

   return ser
