from chiplotle.tools.serialtools.virtual_serial_port import VirtualSerialPort
from chiplotle import plotters

def instantiate_virtual_plotter(left=0, bottom=0, right=15000, top=10000, type="Plotter"):
   '''Instantiates a virtual plotter'''

   ser = VirtualSerialPort(left, bottom, right, top)
   plotter = getattr(plotters, type)(ser)
   return plotter

