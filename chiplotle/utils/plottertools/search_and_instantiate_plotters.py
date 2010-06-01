from chiplotle.cfg.verify_config_file import verify_config_file
from chiplotle.utils.serialtools import sniff_ports_for_plotters
from chiplotle.utils.serialtools import instantiate_serial_from_config_file
from chiplotle.utils.plottertools._instantiate_plotter import _instantiate_plotter
from chiplotle.utils.serialtools import scan_serial_ports

def search_and_instantiate_plotters( ):
   '''Dynamically searches and instantiates all found plotters.
   The function sniffs all serial ports in search for pen plotters and
   instantiates all plotters found. If a plotter is not recognized,
   the function interactively queries user for plotter type.'''

   from chiplotle.utils.plottertools import instantiate_plotter_from_id
   from chiplotle.utils.plottertools import interactive_choose_plotter

   verify_config_file( )
   
   print 'Scanning serial ports...'
   ports = scan_serial_ports( ).values( )
   print 'Found ports:' 
   print '  ' + '\n  '.join(ports)
   
   ## get serial ports that have a plotter connected...
   print '\nSniffing for plotters in all serial ports...'
   plotters_found = sniff_ports_for_plotters(ports)
   if len(plotters_found) == 0:
      print 'Found no plotter connected to any of the serial ports.'''
      print 'Is your plotter on?'''
      return None
   else:
      for serial_address, pln in plotters_found.items( ):
         print '   Found plotter %s in port %s' % (pln, serial_address)
   ## instantiate a plotter for every port with a plotter... 
   result = [ ]
   for serial_address, pln in plotters_found.items( ): 
      plotter = _instantiate_plotter(serial_address, pln)
      result.append(plotter)
   return result 
