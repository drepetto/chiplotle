from chiplotle.cfg.read_config_value import read_config_value
from chiplotle.utils.interactive_open_serial import interactive_open_serial
from chiplotle.utils.interactive_choose_plotter import \
   interactive_choose_plotter
from chiplotle.utils.is_plotter_alive import is_plotter_alive
from chiplotle import plotters
import serial

def instantiate_plotter(port=None, wait_time=10):
   '''Instantiate a Plotter object associated with a port `port`. 
   If port is not passed as an argument it will be read from the config
   file. If not found in the config file the user will be prompted with
   an interactive menu.
   
   - *port* : ``str`` location of serial port. Usually something like
      '/def/ttyS0'. 
   - *wait_time* : ``int`` maximum wait time for plotter response. 
   '''
   ## serial port
   if not port:
      port = read_config_value('serial_port')
   if port:
      ser = serial.Serial(port, 9600, timeout=.1)
   else:
      ser = interactive_open_serial( )

   ## plotter
   if not is_plotter_alive(ser, wait_time):
      print '*** ERROR: no plotter found in %s or not powered on.' % ser.port
      return None

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
