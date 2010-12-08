from chiplotle.hpgl.coordinatepair import CoordinatePair

'''Interactive plotter routines.'''

def interactive_set_plot_window(plotter):
   #Interactive routine to manually move the pen to set the margins of the plotting window.
   
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
   
   plotter.set_plot_window(CoordinatePair(x1, y1), CoordinatePair(x2, y2))

   '''
from chiplotle.interactive.interactive_commands import *
interactive_set_plot_window(plotter)
   '''
   
def interactive_define_polygon_simple(plotter):
   from chiplotle.hpgl.compound.polygon_simple import PolygonSimple
   
   points = []

   print "Interactive define polygon simple:"
   print "Move pen to each point and press enter. Press x when finished adding points."
   print "The final point (a duplicate of first point) will be added automatically."
   while True:
      input = raw_input()
      if input is 'x':
         break;

      point = CoordinatePair(plotter.actual_position[0].x, plotter.actual_position[0].y)
      points.append(point)
      print "added:"
      print point
      
   poly = PolygonSimple([0,0], points)
      
   return poly

