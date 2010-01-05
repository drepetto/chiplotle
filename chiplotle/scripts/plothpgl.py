#!/usr/bin/env python
from chiplotle.utils.instantiate_plotter import instantiate_plotter
import sys
import time

def plot_hpgl(file):
   '''Send an HPGL file to the plotter found connected to the computer.'''
   plotter = instantiate_plotter( )
   plotter.writeFile(file)
   ## call flush( ) to wait till all data is written before exiting...
   plotter._serialPort.flush( )


if __name__ == '__main__':
   if len(sys.argv) < 2:
      print 'Must give HPGL file to plot.\nExample: $ plothpgl myfile.hpgl'
      sys.exit(2)
   file = sys.argv[1]

   plot_hpgl(file) 
