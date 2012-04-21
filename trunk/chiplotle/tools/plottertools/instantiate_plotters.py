from chiplotle.core.cfg.get_config_value import get_config_value
from chiplotle.tools.plottertools._instantiate_plotter \
   import _instantiate_plotter

def instantiate_plotters( ):
   '''Instantiates all found and available plotters.
   The function sniffs all serial ports in search for pen plotters and
   instantiates all plotters found. If a plotter is not recognized,
   the function interactively queries user for plotter type.'''

   from chiplotle.tools.plottertools import search_and_instantiate_plotters
   
   map = get_config_value('serial_port_to_plotter_map')
   ## if user has set fixed port to plotter mapping...
   if map is not None:
      result = [ ]
      for k, v in map.items( ):
         p = _instantiate_plotter(k, v)
         result.append(p)
   else:
      result = search_and_instantiate_plotters( )
   return result
