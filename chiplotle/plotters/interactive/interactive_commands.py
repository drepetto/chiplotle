from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.hpgl.commands import SC, IP, IW

'''
Interactive plotter routines.

Note that these routines may not work on your plotter. They are
known to work on most HP and Roland plotters, but they do NOT
work on the Houston Instruments DMP-60 (and probably other Houston
Instruments plotters). This is because the DMP-60 interprets manual 
pen moves as attempts to reset the origin, which interferes with 
these routines.

'''

def interactive_set_plot_window(plotter):
   '''
   Interactive routine to manually move the pen to set the margins of the plotting window.
   '''
   
   plotter.write(IP())
   plotter.write(IW())
   #plotter.write(SC())
   
   print "Interactive set plot window:"
   print "Move pen to lower left and press enter."
   raw_input()
   position = plotter.actual_position[0]
   x1 = position.x
   y1 = position.y
   
   print "Move pen to upper right and press enter."
   raw_input()
   position = plotter.actual_position[0]
   x2 = position.x
   y2 = position.y
   
   plotter.set_plot_window(Coordinate(x1, y1), Coordinate(x2, y2))

   '''
from chiplotle.plotters.interactive.interactive_commands import *
interactive_set_plot_window(plotter)
   '''
   
   

def interactive_set_plot_window_and_units(plotter):
   '''
   User sets window size and then defines units inside of that window.
   '''
   plotter.write(IP())
   plotter.write(IW())
   plotter.write(SC())

   interactive_set_plot_window(plotter)
   
   print "Enter value for left side (typically 0):"
   left = int(raw_input())
   print "Enter value for bottom side (typically 0):"
   bottom = int(raw_input())
   print "Enter value for right side (width of plot in your units):"
   right = int(raw_input())
   print "Enter value for top side (height of plot in your units):"
   top = int(raw_input())
   
   plotter.write(SC([left,right,bottom,top]))
   print "new soft margins:"
   print plotter.margins.soft

   '''
from chiplotle.interactive.interactive_commands import *
interactive_set_plot_window_and_units(plotter)
   '''
   

def interactive_set_plot_window_auto_units(plotter):
   '''
   User sets window size and then units are automatically set
   to user's choise of inches, millimeters, or centimeters.
   '''
   plotter.write(IP())
   plotter.write(IW())
   plotter.write(SC())
   
   interactive_set_plot_window(plotter)
   
   orig_right = plotter.margins.soft.right
   orig_top = plotter.margins.soft.top
   
   width = plotter.margins.soft.width
   height = plotter.margins.soft.height
   
   inches_w = width/1016.0
   inches_h = height/1016.0
   
   cm_w = width/400.0
   cm_h = height/400.0
   
   mm_w = width/40.0
   mm_h = width/40.0
   
   print "Window size is:"
   print "%f inches x %f inches" % (inches_w, inches_h)
   print "%f cm x %f cm" % (cm_w, cm_h)
   print "%f mm x %f mm" % (mm_w, mm_h)
   
   print "Choose units:"
   print "1) inches"
   print "2) cm"
   print "3) mm"
   
   units = int(raw_input())

   left = plotter.margins.soft.left
   bottom = plotter.margins.soft.bottom
   
   if units == 1:
      right = left + 1016
      top = bottom + 1016
   elif units == 2:
      right = left + 400
      top = bottom + 400
   elif units == 3:
      right = left + 40
      top = righ + 40
   else:
      print "That wasn't one of the choices!"
      return

   plotter.write(IP([left, bottom,right,top]))
   plotter.write(SC([0,1,0,1]))
   #plotter.write(IP([left, bottom, orig_right, orig_top]))
   
   
   #These margins will be WRONG!!! They'll be the floor integer margins,
   #not the margins set via the set_plot_window() above. ARRRRG!
   print "new soft margins:"
   print plotter.margins.soft

   '''
from chiplotle.plotters.interactive.interactive_commands import *
interactive_set_plot_window_auto_units(plotter)
   '''
   

def interactive_define_polygon_simple(plotter):
   '''
   Interactive routine to define points in a PolygonSimple object.
   '''
   from chiplotle.hpgl.compound.polygon_simple import PolygonSimple
   
   points = []

   print "Interactive define PolygonSimple:"
   print "Move pen to each point and press enter. Press x when finished adding points."
   print "The final point (a duplicate of first point) will be added automatically."
   while True:
      input = raw_input()
      if input is 'x':
         break;

      point = Coordinate(plotter.actual_position[0].x, plotter.actual_position[0].y)
      points.append(point)
      print "added:"
      print point
      
   poly = PolygonSimple([0,0], points)
      
   return poly


def interactive_define_rectangle(plotter):
   '''
   Interactive routine to define points in a Rectangle object.
   '''
   from chiplotle.hpgl.compound.rectangle import Rectangle
   
   points = []

   print "Interactive define Rectangle:"
   print "Move pen to lower, left corner and press enter."

   input = raw_input()
   lower_left = Coordinate(plotter.actual_position[0].x, plotter.actual_position[0].y)
   print "lower_left:"
   print lower_left
   
   print "Move pen to upper, right corner and press enter."
   input = raw_input()
   upper_right = Coordinate(plotter.actual_position[0].x, plotter.actual_position[0].y)
   print "upper_right:"
   print upper_right   
      
   rectangle = Rectangle([lower_left], upper_right.x, upper_right.y)
      
   return rectangle

'''
from chiplotle.plotters.interactive.interactive_commands import *
interactive_define_rectangle(plotter)
'''


def interactive_define_ellipse(plotter):
   '''
   Interactive routine to define center and radii of an ellipse.
   '''
   from chiplotle.hpgl.compound.rectangle import Ellipse
   
   points = []

   print "Interactive define Rectangle:"
   print "Move pen to lower, left corner and press enter."

   input = raw_input()
   lower_left = Coordinate(plotter.actual_position[0].x, plotter.actual_position[0].y)
   print "lower_left:"
   print lower_left
   
   print "Move pen to upper, right corner and press enter."
   input = raw_input()
   upper_right = Coordinate(plotter.actual_position[0].x, plotter.actual_position[0].y)
   print "upper_right:"
   print upper_right   
      
   rectangle = Rectangle([lower_left], upper_right.x, upper_right.y)
      
   return rectangle

'''
from chiplotle.plotters.interactive.interactive_commands import *
interactive_define_rectangle(plotter)
'''

