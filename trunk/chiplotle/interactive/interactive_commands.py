

def interactive_set_plot_window(plotter):
   #Interactive routine to manually move the pen to set the margins of the plotting window.
   
   print "Setting plot window."
   print ""
   print "Move pen to lower left and press enter."
   raw_input()
   position = plotter.actual_position[0]
   x1 = position.x
   y1 = position.y
   print "left: %d bottom: %d" % (x1, y1)
   
   print ""
   print "Move pen to upper right and press enter."
   raw_input()
   position = plotter.actual_position[0]
   x2 = position.x
   y2 = position.y
   print "right: %d top: %d" % (x2, y2)
   
   plotter.write(plotter._hpgl.IP([x1, y1, x2, y2]))
   plotter.write(plotter._hpgl.IW([x1, y1, x2, y2]))
   
   print ""
   print "Plot window set to:"
   print plotter.output_p1p2

'''
class InteractiveCommands():
   def __init__(self):
      pass
      
   @staticmethod
   def interactive_set_plot_window(plotter):
      #Interactive routine to manually move the pen to set the margins of the plotting window.
      
      print "Setting plot window."
      print ""
      print "Move pen to lower left and press enter."
      raw_input()
      position = plotter.actual_position[0]
      x1 = position.x
      y1 = position.y
      print "left: %d bottom: %d" % (x1, y1)
      
      print ""
      print "Move pen to upper right and press enter."
      raw_input()
      position = plotter.actual_position[0]
      x2 = position.x
      y2 = position.y
      print "right: %d top: %d" % (x2, y2)
      
      plotter.write(plotter._hpgl.IP([x1, y1, x2, y2]))
      plotter.write(plotter._hpgl.IW([x1, y1, x2, y2]))
      
      print ""
      print "Plot window set to:"
      print plotter.output_p1p2
      

'''