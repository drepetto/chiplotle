from chiplotle.tools.serialtools.virtual_serial_port \
     import VirtualSerialPort
from chiplotle.tools.plottertools.instantiate_plotter_from_id \
     import instantiate_plotter_from_id
from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.core.cfg.get_config_value import get_config_value

def instantiate_virtual_plotter(left_bottom = Coordinate(0,0), 
                                right_top = Coordinate(10320, 7920), 
                                type=None):
   '''
   Instantiates a virtual plotter with 8.5x11" (ANSI A) paper.
   If you have a default plotter defined in your config.py file
   we will use that plotter definition file (ignoring the serial
   port setting).
   '''

   which_plotter = type
   
   if type is None:
      map = get_config_value('serial_port_to_plotter_map')
      ## if user has set fixed port to plotter mapping...
      if map is not None:
         for k, v in map.items( ):
            which_plotter = v
      else:
         which_plotter = "Plotter"
         
   ser = VirtualSerialPort(left_bottom, right_top)
   plotter = instantiate_plotter_from_id(ser, which_plotter)
   print "\nInstantiated plotter %s:" % plotter
   coords = plotter.margins.soft.all_coordinates
   print "   Drawing limits: (left %s; bottom %s; right %s; top %s)" % coords
   print "   Buffer Size: %s" % plotter.buffer_size
         
   return plotter


