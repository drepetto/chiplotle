#!/usr/bin/env python
from chiplotle import *
from chiplotle.tools.plottertools import instantiate_virtual_plotter
import sys
import time

def plot_hpgl_file(file):
   '''Send an HPGL file to the plotter found connected to the computer.'''
   plotter = instantiate_virtual_plotter((0,0), (20000,15000))

   plotter.set_origin_bottom_left()

   plotter.write_file(file)
   ## call flush( ) to wait till all data is written before exiting...
   plotter._serial_port.flush( )

   io.view(plotter)

if __name__ == '__main__':
   if len(sys.argv) < 2:
      print 'Must give HPGL file to plot.\nExample: $ plot_hpgl_file.py myfile.hpgl'
      sys.exit(2)
   file = sys.argv[1]

   plot_hpgl_file(file) 
