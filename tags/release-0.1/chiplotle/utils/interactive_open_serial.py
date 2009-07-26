import os
import re
import serial

def interactive_open_serial( ):
   ### get available ports
   availablePorts = os.listdir("/dev")
   ttyTest = re.compile("tty")
   ttys = filter(ttyTest.search, availablePorts)

   print "Available ports:\r"
   for i,port in enumerate(ttys):
      print "[%d] %s\t" % (i, port),
      if i % 5 == 4:
         print '\r'

   sp = raw_input("\n\nChoose serial port [0 - %d]: " % (i - 1))

   print "okay, opening %s..." % ttys[int(sp)]
   ser = serial.Serial("/dev/" + ttys[int(sp)], 9600, timeout=.1)
   return ser

