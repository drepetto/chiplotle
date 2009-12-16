from chiplotle.utils.interactive_choose_plotter import \
   interactive_choose_plotter
from chiplotle.utils.instantiate_serial import instantiate_serial
from chiplotle.utils.is_plotter_alive import is_plotter_alive
from chiplotle import plotters

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
   ser = instantiate_serial(port)

   if not is_plotter_alive(ser, wait_time):
      return None

   plotter = interactive_choose_plotter(ser)
   #print "\nDrawing area: %s" % plotter.marginSoft
   print "\nDrawing area: %s" % plotter.margins.soft
   print "Buffer Size: %s\n" % plotter.bufferSize

   return plotter
