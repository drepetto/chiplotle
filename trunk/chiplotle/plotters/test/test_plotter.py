from chiplotle import *
from chiplotle.cfg.read_config_value import read_config_value
from serial import Serial

def test_plotter_01( ):
   '''
   Plotter must be initialized with a Serial object. 
   Timeout must not be None.
   '''
   port = read_config_value('serial_port')
   if port:
      s = Serial(port=port, baudrate=9600, timeout=0.1)
      plotter = Plotter(s)
      assert plotter

