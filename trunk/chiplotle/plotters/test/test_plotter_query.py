from chiplotle import *
from chiplotle.cfg.get_serial_port import get_serial_port
from serial import Serial

def test_plotter_query_01( ):
   '''
   '''
   port = get_serial_port( )
   if port:
      s = Serial(port=port, baudrate=9600, timeout=0.1)
      plotter = Plotter(s)
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
