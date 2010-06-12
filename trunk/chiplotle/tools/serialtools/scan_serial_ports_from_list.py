import serial

def scan_serial_ports_from_list(portlist):
   
   result = { }
   ## keep track of previously opened ports to avoid including aliases
   ## in our list...
   ports_opened = [ ]
   for i, port in enumerate(portlist):
      try:
         s = serial.Serial(port)
         ports_opened.append(s)
         result[i] = s.portstr
         #result[i] = s
         #s.close( )   # explicit close 'cause of delayed GC in java
      except serial.SerialException:
         pass
   ## gracefully close all open ports...
   for port in ports_opened:
      port.close( )
   return result
