from chiplotle import *
from chiplotle.cfg.read_config_value import read_config_value
from chiplotle.utils.instantiate_plotter import instantiate_plotter
from serial import Serial

def test_plotter_query_01( ):
   plotter = instantiate_plotter( )

   assert plotter._bufferSpace
   assert plotter.id
   assert plotter.actualPosition
   assert plotter.commandedPosition
   assert plotter.digitizedPoint
   assert plotter.outputError
   assert plotter.hardClipLimits
   assert plotter.options
   assert plotter.outputP1P2
   assert plotter.status
   assert plotter.window

