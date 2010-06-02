#!/usr/bin/env python
from chiplotle.tools import *
import sys

def find_hpgl_file_dimensions(file):
   '''
   prints width, height, and minimum and maximum x,y coordinates found in hpgl plot file
   '''

   f = io.import_hpgl_file(file)
   
   dimensions = hpgltools.find_hpgl_dimensions(f)

   minX = dimensions[0][0]
   minY = dimensions[0][1]
   maxX = dimensions[1][0]
   maxY = dimensions[1][1]
   width = maxX - minX
   height = maxY - minY
   
   print ""
   print dimensions
   print "width: %d height: %d" % (width, height)



if __name__ == '__main__':
   if len(sys.argv) < 2:
      print 'Must give HPGL file.\nExample: $ find_hpgl_file_dimensions myfile.hpgl'
      sys.exit(2)
   file = sys.argv[1]

   find_hpgl_file_dimensions(file) 