from chiplotle import *
from chiplotle.utils.interactive_open_serial import interactive_open_serial
from chiplotle.utils.interactive_choose_plotter import interactive_choose_plotter
from chiplotle.cfg.read_config_value import read_config_value
import serial

print "\n* * * CHIPLOTLE in the house! * * *\n"

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
