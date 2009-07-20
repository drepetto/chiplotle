#!/usr/bin/env python
from chiplotle.utils.instantiate_plotter import instantiate_plotter
import sys

def plot_hpgl(file):
   '''Send an HPGL file to the plotter found connected to the computer.'''
   f = open(file, 'r')
   data = f.read( ).splitlines( )
   f.close( )

   plotter = instantiate_plotter( )
   plotter.write(data)


if __name__ == '__main__':

   if len(sys.argv) < 2:
      print 'Must give HPGL file to plot.\nExample: $ plothpgl myfile.hpgl'
      sys.exit(2)

   file = sys.argv[1]

   plot_hpgl(file) 
