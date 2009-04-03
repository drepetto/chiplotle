from chiplotle.cfg.read_config_value import read_config_value
from chiplotle.utils.interactive_open_serial import interactive_open_serial
from chiplotle.utils.interactive_choose_plotter import \
   interactive_choose_plotter
import serial

def instantiate_plotter(port=None):
   '''Instantiate a Plotter object associated with a port `port`. 
   If port is not passed as an argument it will be read from the config
   file. If not found in the config file the user will be prompted with
   an interactive menu.'''
   ## serial port
   if not port:
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

   return plotter
