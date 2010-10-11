#!/usr/bin/env python
from chiplotle.tools import *
import sys

def find_hpgl_file_dimensions(file):
   '''
   prints width, height, and minimum and maximum x,y coordinates found in hpgl plot file
   '''

   f = io.import_hpgl_file(file)
   
   #dimensions = hpgltools.find_hpgl_dimensions(f)
   dimensions = hpgltools.get_bounding_box(f)

   minX = dimensions[0].x
   minY = dimensions[0].y
   maxX = dimensions[1].x
   maxY = dimensions[1].y
   width = maxX - minX
   height = maxY - minY
   
   print ""
   print "bounding box: ", dimensions
   print "width: %d height: %d" % (width, height)



if __name__ == '__main__':
   if len(sys.argv) < 2:
      print 'Must give HPGL file.\nExample: $ find_hpgl_file_dimensions myfile.hpgl'
      sys.exit(2)
   file = sys.argv[1]

   find_hpgl_file_dimensions(file) 
