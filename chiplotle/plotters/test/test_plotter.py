from chiplotle import *
from serial import Serial

def test_plotter_01( ):
   '''
   Plotter must be initialized with a Serial object. 
   Timeout must not be None.
   '''
   s = Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=0)
   plotter = Plotter(s)
   assert plotter

