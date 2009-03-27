
"""
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
"""

from chiplotle import *
from chiplotle.utils.interactive_open_serial import interactive_open_serial
from chiplotle.cfg.get_serial_port import get_serial_port
from chiplotle.cfg.verify_config_file import verify_config_file
import serial

print "\n* * * CHIPLOTLE in the house! * * *\n"

verify_config_file( )
port = get_serial_port( )
if port:
   ser = serial.Serial(port, 9600, timeout=.1)
else:
   ser = interactive_open_serial( )
#print ser

### TODO: go to 'offline' mode if plotter is not found?
plotter = plotters.Plotter(ser)
print "\nPlotter with ID %s found in selected port." % plotter.id

print "\nChoose a plotter type:"
for i, plotter in enumerate(dir(plotters)):
   print '[%d] %s' % (i,  plotter)

plotter = plotters.__dict__[ dir(plotters)[int(raw_input())] ](ser)

print "\nPlotter [plotter] with ID %s opened. " % plotter.id
print "Drawing area: %s" % plotter.marginSoft
print "Status: %s" % plotter.status
print "Buffer Size: %s" % plotter.bufferSize
print "\n"


