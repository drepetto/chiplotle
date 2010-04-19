import serial

def scan_serial_ports_windows( ):
   result = { }
   for i in range(256):
      try:
         s = serial.Serial(i)
         result[i] = s
         s.close( )   # explicit close 'cause of delayed GC in java
      except serial.SerialException:
         pass
   return result
   
