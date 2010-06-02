#!/usr/bin/env python
from chiplotle.utils.plottertools import instantiate_plotters
from chiplotle.tools import *
import sys
import time

def plot_hpgl_file_max_size(file):
   '''
   Scale an HPGL file so that it will plot as large as possible on the
   the plotter found connected to the computer.
   
   Make sure your hpgl file does not include any IN, IP, or SC commands,
   as they will interfere with the scaling included here!
   
   Plot origin will be on the bottom, left and plot will be scaled
   to be as large as possible without distorting either axis.
   '''
   plotter = instantiate_plotters( )[0]
   
   f = io.import_hpgl_file(file)
   
   print f
   
   dimensions = hpgltools.find_hpgl_dimensions(f)
   
   print "original dimensions: "
   print dimensions
   
   minX = dimensions[0][0]
   minY = dimensions[0][1]
   maxX = dimensions[1][0]
   maxY = dimensions[1][1]
   
   widthPlot = maxX - minX
   heightPlot = maxY - minY
      
   width = plotter.margins.hard.width
   height = plotter.margins.hard.height
   
   maxScaleWidth = width/widthPlot
   maxScaleHeight = height/heightPlot
   
   if maxScaleWidth > maxScaleHeight:
      scaler = maxScaleHeight
   else:
      scaler = maxScaleWidth
      
   p1X = 0
   p1Y = 0
   p2X = int(widthPlot * scaler)
   p2Y = int(heightPlot * scaler)
   
   print minX, minY, maxX, maxY
   print widthPlot, heightPlot
   print p1X, p1Y, p2X, p2Y
   print scaler

   plotter.set_origin_bottom_left()
   
   hpgltools.scale(f, scaler)

   dimensions = hpgltools.find_hpgl_dimensions(f)
   
   hpgltools.transpose(f, [-dimensions[0][0], -dimensions[0][1]])
   
   dimensions = hpgltools.find_hpgl_dimensions(f)
   
   print "scaled dimensions: "
   print dimensions
   
   plotter.write(f)
   

   ## call flush( ) to wait till all data is written before exiting...
   plotter._serial_port.flush( )


if __name__ == '__main__':
   if len(sys.argv) < 2:
      print 'Must give HPGL file to plot.\nExample: $ plot_hpgl_file_max_size.py myfile.hpgl'
      sys.exit(2)
   file = sys.argv[1]

   plot_hpgl_file_max_size(file) 
