"""
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
"""

from chiplotle import *
from chiplotle.utils.interactive_open_serial import interactive_open_serial
from chiplotle.utils.interactive_choose_plotter import interactive_choose_plotter
from chiplotle.cfg.read_config_value import read_config_value
#from chiplotle.cfg.get_serial_port import get_serial_port
#from chiplotle.cfg.verify_config_file import verify_config_file
import serial

print "\n* * * CHIPLOTLE in the house! * * *\n"

#verify_config_file( )
#port = get_serial_port( )
## serial port
port = read_config_value('serial_port')
if port:
   ser = serial.Serial(port, 9600, timeout=.1)
else:
   ser = interactive_open_serial( )

## plotter
plt_name = read_config_value('plotter_type')
if plt_name:
   plotter = getattr(plotters, plt_name)(ser)
else:
   plotter = interactive_choose_plotter(ser)

print "Plotter 'plotter' with ID %s opened. " % plotter.id
print "Drawing area: %s" % plotter.marginSoft
print "Buffer Size: %s" % plotter.bufferSize
print "\n"
