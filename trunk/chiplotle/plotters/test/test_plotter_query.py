from chiplotle import *
from chiplotle.utils.instantiate_plotter import instantiate_plotter

plotter = instantiate_plotter(wait_time = 3)
if plotter:

   def test_plotter_query_01( ):

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

