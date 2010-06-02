#!/usr/bin/env python
from chiplotle.utils.plottertools import instantiate_plotters
import sys
import time

def plot_hpgl_file(file):
   '''Send an HPGL file to the plotter found connected to the computer.'''
   plotter = instantiate_plotters( )[0]
   plotter.write_file(file)
   ## call flush( ) to wait till all data is written before exiting...
   plotter._serial_port.flush( )


if __name__ == '__main__':
   if len(sys.argv) < 2:
      print 'Must give HPGL file to plot.\nExample: $ plot_hpgl_file.py myfile.hpgl'
      sys.exit(2)
   file = sys.argv[1]

   plot_hpgl_file(file) 
