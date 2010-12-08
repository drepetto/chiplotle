from chiplotle.tools.serialtools.virtual_serial_port import VirtualSerialPort
from chiplotle.hpgl.coordinatepair import CoordinatePair
from chiplotle import plotters

def instantiate_virtual_plotter(left_bottom = CoordinatePair(0,0), 
    right_top = CoordinatePair(10320, 7920), 
    type="Plotter"):
   '''Instantiates a virtual plotter with 8.5x11" (ANSI A) paper.'''

   ser = VirtualSerialPort(left_bottom, right_top)
   plotter = getattr(plotters, type)(ser)
   print "\nInstantiated plotter %s:" % plotter
   coords = plotter.margins.soft.all_coordinates
   print "   Drawing limits: (left %s; bottom %s; right %s; top %s)" % coords
   print "   Buffer Size: %s" % plotter.buffer_size
   return plotter

