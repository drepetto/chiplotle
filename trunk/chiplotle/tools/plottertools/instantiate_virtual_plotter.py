from chiplotle.cfg.get_config_value import get_config_value
from chiplotle.tools.plottertools._instantiate_plotter import _instantiate_plotter

def instantiate_virtual_plotter( ):
   '''Instantiates a virtual plotter'''

   return _instantiate_plotter(port=None, id="VirtualPlotter")

