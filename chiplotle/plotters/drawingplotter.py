'''
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
'''

from chiplotle.plotters.baseplotter import _BasePlotter

class _DrawingPlotter(_BasePlotter):

   ## TEXT OUTPUT & SETTINGS ##

   def absolute_char_size(self, w = None, h = None):
      self.write(self._hpgl.SI(w, h))

   def absolute_direction(self, run = 1, rise = 0):
      print 'not implemented yet.'

   def character_chord_angle(self, angle = 5):
      self.write(self._hpgl.CC(angle))

   def buffer_label(self, text = None):
      self.write(self._hpgl.BL(text))

   def character_plot(self, spaces = None, lines = None):
      self.write(self._hpgl.CP(spaces, lines))

   def character_selection_mode(self, switch = 0, fallback = 0):
      self.write(self._hpgl.CM(switch, fallback))

   def character_set(self, set = 0):
      self.write(self._hpgl.CS(set))        

   def character_slant(self, tan = 0):
      self.write(self._hpgl.SL(tan))

   def define_label_terminator(self, t = chr(3)):
      self.write(self._hpgl.DT(t))

   def designate_alternate_character_set(self, n = 0):
      self.write(self._hpgl.CA(n))

#   def direction_vertical(self, dir = 0):

#   def extra_space(self, spaces = 0, lines = 0):

#   def invoke_character_slant(self, slot = 0, left = None):

   def label(self, text):
      self.write(self._hpgl.LB(text))

#   def label_origin(self, positionNum = 1):

#   def new_line(self):


   def print_buffered_label(self):
      self.write(self._hpgl.PB())

   def relative_character_size(self, w = None, h = None):
      self.write(self._hpgl.SR(w, h))

#   def relative_direction(self, run = 1, rise = 0):
          
   def select_alternate_character_set(self):
      self.write(self._hpgl.SA())

   def symbol_mode(self, char = None):
      self.write(self._hpgl.SM(char))

   def select_standard_character_set(self):
      self.write(self._hpgl.SS())



   ## DRAWING PRIMITIVES & SETTINGS

   def arch_absolute(self, x, y, aa, ca = 5):
      self.write(self._hpgl.AA((x, y), aa, ca))

   def arch_relative(self, x, y, aa, ca = 5):
      self.write(self._hpgl.AR((x, y), aa, ca))

   def chord_tolerance(self, type = 0):
      self.write(self._hpgl.CT(type))

   def circle(self, rad, ca = 5):
      self.write(self._hpgl.CI(rad, ca))

#   def curved_line_generator(self, n = None, inputDelay = None):

   def edge_polygon(self):
      self.write(self._hpgl.EP())

   def edge_rectangle_relative(self, x, y):
      self.write(self._hpgl.ER((x,y)))

   def edge_rectangle_absolute(self, x, y):
      self.write(self._hpgl.EA((x,y)))

#   def edge_wedge(self, r, sa, swa, ca=5):

   def fill_polygon(self):
      self.write(self._hpgl.FP())

   def filled_rectangle_absolute(self, x, y):        
      self.write(self._hpgl.RA((x, y)))

   def filled_rectangle_relative(self, x, y):
      self.write(self._hpgl.RR((x, y)))

#   def filled_wedge(self, r, sa, swa, ca = 5):

   def fill_type(self, type=1, space=None,  angle=0):
      self.write(self._hpgl.FT(type, space, angle))

   def line_type(self, pattern, length = 4):
      self.write(self._hpgl.LT(pattern, length))

   def plot_polygon(self, n = 0):
      self.write(self._hpgl.PM(n))



   ## DIRECT PEN CONTROL & INFO

   def acceleration_select(self, accel = None, pen = None):
      self.write(self._hpgl.AS(accel, pen))

   def force_select(self, force = None, pen = None):
      self.write(self._hpgl.FS(force, pen))

   def goto(self, x, y):
      """Alias for PA() with only one point"""
      self.write(self._hpgl.PA((x, y)))

   def goto_center(self):
      self.write(self._hpgl.PA(self.margins.soft.center))

   def goto_bottom_left(self):
      self.write(self._hpgl.PA(self.margins.soft.bottom_left))

   def goto_bottom_right(self):
      self.write(self._hpgl.PA(self.margins.soft.bottom_right))

   def goto_top_left(self):
      self.write(self._hpgl.PA(self.margins.soft.top_left))

   def goto_top_right(self):
      self.write(self._hpgl.PA(self.margins.soft.top_right))

   def nudge(self, x, y):
      self.write(self._hpgl.PR((x,y)))

   def plot_absolute(self, coords = None):
      """
         Plot Absolute.
         Takes a tuple of any number of sets of points:
         (0,0,100,100,2500,1000) will go to three different points:
             0,0 100,100 2500,1000
      """
      self.write(self._hpgl.PA(coords))

   def plot_relative(self, coords = None):
      """
         Plot Relative.
         Takes a tuple of any number of sets of points:
         (0,0,100,100,2500,1000) will go to three different points:
             0,0 100,100 2500,1000
      """
      self.write(self._hpgl.PR(coords))

   def pen_down(self, coords = None):
      """Pen Down."""
      self.write(self._hpgl.PD(coords))

   def pen_thickness(self, thickness = 0.3):
      self.write(self._hpgl.PT(thickness))

   def pen_up(self, coords = None):
      """Pen Up."""
      self.write(self._hpgl.PU(coords))

   def select_pen(self, penNum = 0):
      self.write(self._hpgl.SP(penNum))

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
         
      posx = float(self.actual_position.rsplit(',')[0])
      posy = float(self.actual_position.rsplit(',')[1])
      p1x = self.margins.hard.left - posx
      p1y = self.margins.hard.bottom - posy
      p2x = p1x + self.margins.hard.width
      p2y = p1y + self.margins.hard.height
      
      self.write(self._hpgl.SC([p1x,p2x,p1y,p2y]))
      posx = float(self.actual_position.rsplit(',')[0])
      posy = float(self.actual_position.rsplit(',')[1])
      
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
 
   def tick_length(self, tp = 0.5, tn = 0.5):
      self.write(self._hpgl.TL(tp, tn))

   def x_tick(self):
      self.write(self._hpgl.XT())

   def y_tick(self):
      self.write(self._hpgl.YT())        
              
   def velocity_select(self, v = None, pen = None):
      """ Set pen's velocity."""
      self.write(self._hpgl.VS(v, pen))

   def input_window(self, xLL = None, yLL = None, xUR = None, yUR = None):
      self.write(self._hpgl.IW((xLL, yLL, xUR, yUR)))

   def paper_size(self, size = None):
      self.write(self._hpgl.PS(size))

   def rotate(self, angle = 0):
      self.write(self._hpgl.RO(angle))

   def scale(self, xMin, xMax, yMin, yMax):
      self.write(self._hpgl.SC((xMin, xMax, yMin, yMax)))


   ## PAPER CONTROLS

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


   ## DIGITIZER CONTROLS

   def clear_digitizer(self):
      self.write(self._hpgl.DC())

   def digitize_point(self):
      self.write(self._hpgl.DP())


   ## MISC I/O, PLOTTER QUERIES, ERRORS, SETUP

   def abort_command(self):
      """Tells the plotter to discard commands in its buffer."""
      self.write(self._hpgl.K())

   def automatic_pen(self, p = None):
      self.write(self._hpgl.AP(p))

   def buffer_plot(self):
      self.write(self._hpgl.BF())

   def default_instruction(self):
      self.write(self._hpgl.DF())

#   def define_key(self, key = None, function = None):

#   def input_mask(self, e = 233, s = 0, p = 0):

   def not_ready(self):
      self.write(self._hpgl.NR())

   def replot(self, n = 1):
      self.write(self._hpgl.RP(n))

   def write_to_display(self, text):
      self.write(self._hpgl.WD(text))

