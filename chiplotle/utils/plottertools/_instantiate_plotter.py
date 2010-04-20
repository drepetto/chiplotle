from chiplotle.utils.serialtools import instantiate_serial_from_config_file
from chiplotle import plotters

def _instantiate_plotter(port, id):
   '''Instantiate a Plotter object with given `id` at port `port`. 
   
   - `port` a ``str`` address or number of serial port. 
      Usually something like '/def/ttyS0' in posix systems or 'COM1' Windowz.
   - `id` is the string ID of the plotter we wish to instantiate.
   '''
   ser = instantiate_serial_from_config_file(port)

   from chiplotle.utils.plottertools import instantiate_plotter_from_id
   from chiplotle.utils.plottertools import interactive_choose_plotter
   plotter = instantiate_plotter_from_id(ser, id)
   if not plotter:
      plotter = interactive_choose_plotter(ser)
   print "\nInstantiated plotter %s:" % plotter
   print "\tDrawing area: %s" % plotter.margins.soft
   print "\tBuffer Size: %s" % plotter.bufferSize
   return plotter
