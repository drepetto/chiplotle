
"""
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
"""

from chiplotle import *
#from plotters import *

print "\n* * * CHIPLOTLE in the house! * * *\n"

def open_port( ):
   import os
   import re
   import serial
   # get available ports
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

ser = open_port( )
print ser

# ------------------------

p = plotters.Plotter(ser)
print "\nPlotter with ID %s found in selected port." % p.id

print "\nChoose a plotter type:"
for i, p in enumerate(dir(plotters)):
   print '[%d] %s' % (i,  p)

p = plotters.__dict__[ dir(plotters)[int(raw_input())] ](ser)

print "\nPlotter [p] with ID %s opened. " % p.id
print "Drawing area: %s" % p.marginSoft
print "Status: %s" % p.status


