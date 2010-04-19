import serial
import glob

def scan_serial_ports_linux( ):
   ports = glob.glob('/dev/ttyS*') + glob.glob('/dev/ttyUSB*') +\
      glob.glob('/dev/tty.USA*') + glob.glob('/dev/tty.KeySerial*')
   result = { }
   for i, port in enumerate(ports):
      try:
         s = serial.Serial(port)
         result[i] = s
         s.close( )
      except serial.SerialException:
         pass
   return result
