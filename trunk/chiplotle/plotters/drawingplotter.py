'''
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
'''

from chiplotle.plotters.baseplotter import _BasePlotter
from chiplotle.hpgl.coordinatepair import CoordinatePair

class _DrawingPlotter(_BasePlotter):


   ## motion ##

   def goto(self, *args):
      '''
      Alias for PA( ) with only one point.
      Pass in either an x, y pair: goto(100, 100) 
      or a tuple pair: goto((x, y))
      or a CoordinatePair: goto(CoordinatePair(100,100))
      '''
      if len(args) == 1:
         self.write(self._hpgl.PA(args))
      elif len(args) == 2:
         self.write(self._hpgl.PA((args[0], args[1])))
      else:
         print "Please use either: goto(x, y) or goto(CoordinatePair(x, y))"

   def goto_center(self):
      self.write(self._hpgl.PA(self.margins.soft.center))

   def goto_bottom_left(self):
      self.write(self._hpgl.PA(self.margins.soft.bottom_left))

   def goto_bottom_right(self):
      self.write(self._hpgl.PA(self.margins.soft.bottom_right))

   def goto_origin(self):
      self.write(self._hpgl.PA([0,0]))

   def goto_top_left(self):
      self.write(self._hpgl.PA(self.margins.soft.top_left))

   def goto_top_right(self):
      self.write(self._hpgl.PA(self.margins.soft.top_right))

   def nudge(self, x, y):
      self.write(self._hpgl.PR((x,y)))


   ## pen control ##

   def pen_down(self, coords = None):
      """Pen Down."""
      self.write(self._hpgl.PD(coords))

   def pen_up(self, coords = None):
      """Pen Up."""
      self.write(self._hpgl.PU(coords))

   def select_pen(self, penNum = 0):
      self.write(self._hpgl.SP(penNum))


   ## origin setting ##

   def set_origin_bottom_left(self):
      """
         Set origin to bottom, left
      """   
      self.write(self._hpgl.SC()) #reset scaling first!
      self.write(self._hpgl.IP([self.margins.soft.left,
         self.margins.soft.bottom,
         self.margins.soft.right,
         self.margins.soft.top]))
      self.write(self._hpgl.SC([0, self.margins.soft.width, 0, self.margins.soft.height]))
 
   def set_origin_top_left(self):
      """
         Set origin to upper, left
      """   
      self.write(self._hpgl.SC()) #reset scaling first!
      self.write(self._hpgl.IP([self.margins.soft.left,
         self.margins.soft.top,
         self.margins.soft.right,
         self.margins.soft.bottom]))
      self.write(self._hpgl.SC([0, self.margins.soft.width, 0, -self.margins.soft.height]))


   def set_origin_bottom_right(self):
      """
         Set origin to bottom, right
      """   
      self.write(self._hpgl.SC()) #reset scaling first!
      self.write(self._hpgl.IP([self.margins.soft.left,
         self.margins.soft.top,
         self.margins.soft.right,
         self.margins.soft.bottom]))
      self.write(self._hpgl.SC([-self.margins.soft.width,0,self.margins.soft.height,0]))

   def set_origin_top_right(self):
      """
         Set origin to top, right
      """   
      self.write(self._hpgl.SC()) #reset scaling first!
      self.write(self._hpgl.IP([self.margins.soft.left,
         self.margins.soft.bottom,
         self.margins.soft.right,
         self.margins.soft.top]))
      self.write(self._hpgl.SC([-self.margins.soft.width,0,-self.margins.soft.height,0]))
      
   def set_origin_center(self):
      """
         Set origin to center, center
      """   
      self.write(self._hpgl.SC()) #reset scaling first!
      self.write(self._hpgl.IP([self.margins.soft.left,
         self.margins.soft.bottom,
         self.margins.soft.right,
         self.margins.soft.top]))
      
      w_div_2 = self.margins.soft.width/2
      h_div_2 = self.margins.soft.height/2
      
      self.write(self._hpgl.SC([-w_div_2, w_div_2, 
         -h_div_2, h_div_2]))

   def set_origin_current_location(self):
      """
         Set origin to current location
      """
      
      self.write(self._hpgl.SC()) #reset scaling first!
      self.write(self._hpgl.IP([self.margins.soft.left,
         self.margins.soft.bottom,
         self.margins.soft.right,
         self.margins.soft.top]))
         
      posx = float(self.actual_position[0])
      posy = float(self.actual_position[1])
      p1x = self.margins.hard.left - posx
      p1y = self.margins.hard.bottom - posy
      p2x = p1x + self.margins.hard.width
      p2y = p1y + self.margins.hard.height
      
      self.write(self._hpgl.SC([p1x,p2x,p1y,p2y]))
      posx = float(self.actual_position[0])
      posy = float(self.actual_position[1])
      
      self.set_origin_to_point([posx, posy])
      
   def set_origin_to_point(self, point):
      """
         Set origin to given point [x, y]
      """   
      self.write(self._hpgl.SC()) #reset scaling first!
      self.write(self._hpgl.IP([self.margins.soft.left,
         self.margins.soft.bottom,
         self.margins.soft.right,
         self.margins.soft.top]))
         
      posx = point[0]
      posy = point[1]
      p1x = self.margins.hard.left - posx
      p1y = self.margins.hard.bottom - posy
      p2x = p1x + self.margins.hard.width
      p2y = p1y + self.margins.hard.height
      
      self.write(self._hpgl.SC([p1x,p2x,p1y,p2y]))   

   def rotate(self, angle = 0):
      self.write(self._hpgl.RO(angle))

   def scale(self, xMin, xMax, yMin, yMax):
      self.write(self._hpgl.SC((xMin, xMax, yMin, yMax)))

   ## window setting ##
   
   def interactive_set_plot_window(self):
      print "Setting plot window."
      print ""
      print "Move pen to lower left and press enter."
      raw_input()
      x1 = self.actual_position[0].x
      y1 = self.actual_position[0].y
      print "left: %d bottom: %d" % (x1, y1)

      print ""
      print "Move pen to upper right and press enter."
      raw_input()
      x2 = self.actual_position[0].x
      y2 = self.actual_position[0].y
      print "right: %d top: %d" % (x2, y2)
      
      self.write(self._hpgl.IP([x1, y1, x2, y2]))
      self.write(self._hpgl.IW([x1, y1, x2, y2]))
      
      print ""
      print "Plot window set to:"
      print self.output_p1p2


   def set_plot_window(self, left_bottom, right_top):
      '''The function sets new margins for the plotting window.
      Arguments must be two tuple pairs (x, y) or two CoordinatePairs.'''
      try:
         left_bottom = CoordinatePair(left_bottom)
         right_top = CoordinatePair(right_top)
      except TypeError:
         print "Please pass in two coordinate pairs."
         return
         
      print "Setting plot window..."
      x1 = left_bottom.x
      y1 = left_bottom.y
      print "left: %d bottom: %d" % (x1, y1)
      x2 = right_top.x
      y2 = right_top.y
      print "right: %d top: %d" % (x2, y2)
      
      self.write(self._hpgl.IP([x1, y1, x2, y2]))
      self.write(self._hpgl.IW([x1, y1, x2, y2]))

      print "Plot window set to:"
      print self.output_p1p2     


   ## paper control ##

   def advance_frame(self):
      self.write(self._hpgl.FR())

   def advance_full_page(self):
      self.write(self._hpgl.AF())

   def advance_half_page(self):
      self.write(self._hpgl.AH())   

   def enable_cut_line(self, n):
      self.write(self._hpgl.EC(n))

   def page_feed(self, n = None):
      self.write(self._hpgl.PG(n))


   ## digitizer control ##

   def clear_digitizer(self):
      self.write(self._hpgl.DC())

   def digitize_point(self):
      self.write(self._hpgl.DP())


   ## misc i/o, plotter queries, errors, setup ##

   def replot(self, n = 1):
      self.write(self._hpgl.RP(n))

