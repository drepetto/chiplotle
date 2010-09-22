from chiplotle.hpgl.abstract.arc import _Arc
from chiplotle.hpgl.abstract.hpglescape import _HPGLEscape
from chiplotle.hpgl.abstract.hpglprimitive import _HPGLPrimitive
from chiplotle.hpgl.abstract.penplot import _PenPlot
from chiplotle.hpgl.abstract.positional import _Positional
from chiplotle.hpgl.abstract.twopoint import _TwoPoint

class PU(_PenPlot):
   '''
   :Pen Up:
      Raises the pen from the plotting surface. Use this instruction 
      to prevent stray lines from being drawn.

   - `xy` : A ``list`` or ``tuple`` of x, y positions of the form \
   ``(x1, y2, x2, y2, x3, y3, ..., xn, yn)``.
   '''

   def __init__(self, xy=None):
      _PenPlot.__init__(self, xy)


class PD(_PenPlot):
   '''
   :Pen Down:
      Lowers the pen onto the writing surface for drawing and moves it 
      to the coordinates/increments you specified.

   - `xy` : A ``list`` or ``tuple`` of x, y positions of the form \
   ``(x1, y2, x2, y2, x3, y3, ..., xn, yn)``.
   '''

   def __init__(self, xy=None):
      _PenPlot.__init__(self, xy)


class PA(_PenPlot):
   '''
   :Plot Absolute:
      Establishes absolute plotting and moves the pen to specified 
      absolute coordinates using the current pen position.
   '''

   def __init__(self, xy=None):
      _PenPlot.__init__(self, xy)


class PR(_PenPlot):
   '''
   :Plot Relative:
      Establishes relative plotting and moves the pen (using the current 
      position) to the specified points, each successive move relative 
      to the last current pen location.
   '''

   def __init__(self, xy=None):
      _PenPlot.__init__(self, xy)


class CI(_HPGLPrimitive):
   '''
   :Circle:
      Draws a circle using the specified radius and chord tolerance. 
      If you want a filled circle, refer to the 
      :class:`~chiplotle.hpgl.commands.WG` or 
      :class:`~chiplotle.hpgl.commands.PM` instruction.
   '''
   _scalable = ['radius']

   def __init__(self, radius, chordangle=None):   
      self.radius = radius
      self.chordangle = chordangle

   @apply
   def radius( ):
      def fget(self):
         '''The radius of the circle.'''
         return self._radius
      def fset(self, arg):
         ### TODO: check for type here?
         self._radius = arg
      return property(**locals( ))

   @property
   def format(self):
      if self.chordangle:
         return '%s%.2f,%.2f%s' % (self._name, self.radius, self.chordangle, 
                              _HPGLPrimitive._terminator)
      else:
         return '%s%.2f%s' % (self._name, self.radius, _HPGLPrimitive._terminator)


class CC(_HPGLPrimitive):
   '''
   :Character chord angle:
      Sets the chord angle that determines the smoothness of characters
      drawn when you select one of the arc-font character sets for labeling.
   '''

   def __init__(self, angle=None):   
      self.angle = angle

   @property
   def format(self):
      if self.angle:
         return '%s%i%s' % (self._name, self.angle, _HPGLPrimitive._terminator)
      else:
         return '%s%s' % (self._name, _HPGLPrimitive._terminator)


class AF(_HPGLPrimitive):
   '''
   :Advance full page:
      Advances roll paper one full page length and establishes the 
      origin at the center of the new page.
   '''
   

class AH(_HPGLPrimitive):
   '''
   :Advance half page:
      Advances roll paper one half page length and establishes the 
      origin at the center of the new page.
   '''
   

class AP(_HPGLPrimitive):
   '''
   :Automatic Pen operations:
      Controls automatic pen operations such as returning a pen
      to the carousel if it has been in the holder without drawing
      for a certain time.

   For 7550:

   ====== ======= ===== =========================================
   bit_no dec_val state meaning
   ====== ======= ===== =========================================
   0        1      1    lift pen if down too long without motion
   0        0      0    do not lift pen until PU received
   1        2      1    put pen away if too long without  motion
   1        0      0    do not put pen away until SP0 received
   2        4      1    do not get new pen until drawing starts
   2        0      0    get pen immediately after SP command
   3        8      1    merge all pen up moves
   3        0      0    do not merge all pen up moves
   ====== ======= ===== =========================================

   default is 7 on 7550
   codes are 0 to 255 with default of 95 on the DraftMaster
   '''

   def __init__(self, n=None):   
      self.n = n

   @property
   def format(self):
      if self.n:
         return '%s%i%s' % (self._name, self.n, _HPGLPrimitive._terminator)
      else:
         return '%s%s' % (self._name, _HPGLPrimitive._terminator)
         

class AA(_Arc):
   '''
   :Arch Absolute:
      Draws an arc, using absolute coordinates, that starts at the
      current pen location and uses the specified center point.

   - `xy` : ``(x, y)`` position pair.
   - `angle` : ``float`` [-360 to 360]. The arch angle in degrees.
   - `chordtolerance` : ``float`` [0.36 to 180], ``None``.

   '''
   def __init__(self, xy, angle, chordtolerance=None):
      _Arc.__init__(self, xy, angle, chordtolerance)


class AR(_Arc):
   '''
   :Arch Relative:
      Draws an arc, using relative coordinates, that starts at the
      current pen location and uses the specified center point.

   - `xy` : ``(x, y)`` position pair.
   - `angle` : ``float`` [-360 to 360]. The arch angle in degrees.
   - `chordtolerance` : ``float`` [0.36 to 180], ``None``.
   '''

   def __init__(self, xy, angle, chordtolerance=None):
      _Arc.__init__(self, xy, angle, chordtolerance)


class AS(_HPGLPrimitive):
   '''
   :Acceleration Select:
      Sets pen acceleration for one or all pens. The default
      acceleration is suitable for all recommended pen and media
      combinations. Slowing the acceleration may improve line
      quality if you are using heavier than recommended media.

   - `accel` : ``int`` [1 to 4] , ``None``.  
   - `pen` : ``int`` [1 to 8], ``None``. When ``None``, accel is \
      applied to all pens.
   '''

   def __init__(self, accel=None, pen=None):   
      self.accel = accel
      self.pen = pen

   @property
   def format(self):
      if self.accel and self.pen:
         return '%s%i,%i%s' % (self._name, self.accel, self.pen, 
                              _HPGLPrimitive._terminator)
      elif self.accel:
         return '%s%i%s' % (self._name, self.accel, _HPGLPrimitive._terminator)  
      else:
         return '%s%s' % (self._name, _HPGLPrimitive._terminator) 


class EA(_Positional):
   '''
   :Edge Rectangle Absolute:
      Defines and outlines a rectangle using absolute coordinates.

   - `xy` : ``(x, y)``. The absolute coordinates of the remaining corner.
   '''

   def __init__(self, xy):
      _Positional.__init__(self, xy)


class ER(_Positional):
   '''
   :Edge Rectangle Relative:
      Defines and outlines a rectangle using relative coordinates.

   - `xy` : ``(x, y)``. The relative coordinates of the remaining corner.
   '''

   def __init__(self, xy):
      _Positional.__init__(self, xy)


class RA(_Positional):
   '''
   :Filled Rectangle Absolute:
      Defines and fills a rectangle using absolute coordinates.

   - `xy` : ``(x, y)`` tuple. The absolute coordinates of the \
      remaining corner.
   '''

   def __init__(self, xy):
      _Positional.__init__(self, xy)


class RR(_Positional):
   '''
   :Filled Rectangle Relative:
      Defines and fills a rectangle using relative coordinates.

   - `xy` : ``(x, y)`` tuple. The relative coordinates of the \
      remaining corner.
   '''

   def __init__(self, xy):
      _Positional.__init__(self, xy)


class VS(_HPGLPrimitive):
   ''' 
   :Pen Velocity:
      Set's pen velocity.

   - `vel` : ``float`` [0.0 to 127.9999] (depends on plotter), ``None``. 
   - `pen` : ``int`` [1 to 8].
   '''

   def __init__(self, vel=None, pen=None):
      self.vel = vel
      self.pen = pen
     
   @property
   def format(self):
      if self.vel and self.pen:
         return '%s%i,%i%s' % (self._name, self.vel, self.pen, 
            _HPGLPrimitive._terminator)
      elif self.vel:
         return '%s%i%s' % (self._name, self.vel, _HPGLPrimitive._terminator)
      else:
         return '%s%s' % (self._name, _HPGLPrimitive._terminator)


class FS(_HPGLPrimitive):
   '''
   :Force Select:
      Sets pen pressure to the paper for one or all pens. Use this 
      instruction to optimize pen life and line quality for each pen 
      and paper combination.

   - `force` : ``int`` [1 to 8]
   - `pen` : ``int`` [1 to 8]. If pen is ``None`` then all pens are set.
   '''

   def __init__(self, force=None, pen=None):
      self.force = force
      self.pen = pen

   @property
   def format(self):
      if self.force and self.pen:
         return '%s%i,%i%s' % (self._name, self.force, self.pen, 
                              _HPGLPrimitive._terminator)
      elif self.force:
         return '%s%i%s' % (self._name, self.force, _HPGLPrimitive._terminator)
      else:
         return '%s%s' % (self._name, _HPGLPrimitive._terminator)


class EP(_HPGLPrimitive):
   '''
   :Edge Polygon:
      Outlines the polygon currently stored in the polygon buffer. 
      Use this instruction to edge polygons that you defined in polygon mode 
      (:class:`~chiplotle.hpgl.commands.PM`) and with the rectangle and 
      wedge instructions (:class:`~chiplotle.hpgl.commands.RA`, 
      :class:`~chiplotle.hpgl.commands.RR` and 
      :class:`~chiplotle.hpgl.commands.WG`).
   '''


class BF(_HPGLPrimitive):
   '''
   Buffer plot.

   '''
   

class DC(_HPGLPrimitive):
   '''
   :Digitizer Clear:
      Terminates digitize mode. For example, if you are using an interrupt
      routine in a digitizing program to branch to another plotting function,
      use DC to clear the digitize mode immediately after branching. 
   '''
   

class DF(_HPGLPrimitive):
   '''
   :Default:
      Sets certain plotter functions to predefined default conditions.
      Use this instruction to return the plotter to a known state while 
      maintaining the current location of P1 and P2. When you use DF at 
      the beginning of a program, unwanted graphics parameters such as
      character size, slant, or scaling are not inherited from another
      program. 
   '''
   

class DP(_HPGLPrimitive):
   '''
   :Digitize Point:
      Returns the X,Y coordinates of a selected point on a plot to the
      computer for later use. Use this instruction to input data for a
      graphics program or to obtain the coordinates of a point or points
      on plot.
   '''
   

class FP(_HPGLPrimitive):
   '''
   :Fill Polygon:
      Fills the polygon currently in the polygon buffer. Use FP to fill
      polygons defined in polygon mode (
      :class:`~chiplotle.hpgl.commands.PM`) and defined with the edge 
      rectangle and wedge instructions (
      :class:`~chiplotle.hpgl.commands.EA`, 
      :class:`~chiplotle.hpgl.commands.ER`, and 
      :class:`~chiplotle.hpgl.commands.EW`).
   '''
   

class FR(_HPGLPrimitive):
   '''
   :Advance Frame:
      Advances paper to the next plot frame and calculates a relative 
      coordinate system for that frame. Use FR to do multi-frame long-axis 
      plotting.
   '''
   

class NR(_HPGLPrimitive):
   '''
   :Not Ready:
      Programmatically simulates pressing VIEW.
      However, you cannot take the plotter out of the view state with NR
      instruction.
   '''
   

class OA(_HPGLPrimitive):
   '''
   :Output Actual Pen Status:
      Outputs the current pen location (in plotter units) and up/down position.
      Use this information to position a label or figure, to determine the
      parameters of a window, or to determine the pen's curent location if you 
      moved it using front-panel cursor buttons.
   '''
   

class OC(_HPGLPrimitive):
   '''
   :Output Commanded Pen Status:
      Ouput the location and up/down position of the last commanded pen move 
      instruction. Use OC to position a label or determine the parameters of
      an instruction that tried to move the pen beyond the limits of some 
      window. You can also use this instruction when you want to know the 
      pen's location in user units.
   '''
   

class OD(_HPGLPrimitive):
   '''
   :Output Digitized Point and Pen Status:
      Outputs the X,Y coordinates and up/down pen position associated 
      with the last digitized point. Use this instruction after the 
      :class:`~chiplotle.hpgl.commands.DP` instruction to
      return the coordinates of the digitized point to your computer.
   '''
   

class OE(_HPGLPrimitive):
   '''
   :Output Error:
      Output a number corresponding to the type of HP-GL error (if any) 
      received by the plotter after the most recent 
      :class:`~chiplotle.hpgl.commands.IN` or 
      :class:`~chiplotle.hpgl.commands.OE` instruction. Use this 
      instruction for debugging programs. 
   
   =========  ========  ========================
   bit value  error no  meaning
   =========  ========  ========================
   0          0         no error
   1          1         unrecognized command
   2          2         wrong num of parameters
   4          3         out-of-range parameter
   8          4         unused
   16         5         unknown character set
   32         6         position overflow
   64         7         unused
   128        8         pinch wheels raised
   =========  ========  ========================
   
   .. note:: 
      some error meanings change depending on the plotter!
   '''
   

class OF(_HPGLPrimitive):
   '''
   :Output Factors:
      Outputs the number of plotter units per millimeter in each axis. 
      This lets you use the plotter with sofware that needs to know 
      the size of a plotter unit.
   '''
   

class OG(_HPGLPrimitive):
   '''
   :Output Group Count:
      Outputs the data block number of the current group count and 
      whether the escape function has been activated. Use this 
      instruction at the end of a data block in spooling applications, 
      where it is important to know the current data block number and 
      whether the data block has been transferred.
   '''


class OH(_HPGLPrimitive):
   '''
   :Output Hard-Clip Limits:
      Outputs the X,Y coordinates of the current hard-clip limits. 
      Use this instruction to determine the plotter unit dimension of 
      the area in which plotting can occur.
   '''
   

class OI(_HPGLPrimitive):
   '''
   :Output Identification:
      Outputs the plotter's identifying model number. This information is 
      useful in a remote operating configuration to determine which plotter 
      model is on-line, or when software needs the plotter's model number.
   ''' 


class OK(_HPGLPrimitive):
   '''
   :Output Key:
      Outputs a number that indicates which, if any, of the front-panel 
      function keys has been pressed. use this instruction with the 
      :class:`~chiplotle.hpgl.commands.WD` instruction when designing 
      interactive programs.
   '''
   

class OL(_HPGLPrimitive):
   '''
   :Output Label Length:
      Outputs information about the label contained in the label buffer.
   '''


class OO(_HPGLPrimitive):
   '''
   :Output Options:
      Outputs eight option parameters indicating the features implemented 
      on the plotter. Some software packages use this feature to determine 
      which plotter capabilities exist.
   '''
   

class OP(_HPGLPrimitive):
   '''
   :Output P1 and P2:
      Outputs the X,Y coordinates (in plotter units) of the current 
      scaling points P1 and P2. Use this instruction to determine the 
      numberic coordinates or P1 and P2 when they have been set manually, 
      and to help compute the number of plotter units per user units when 
      scaling is on.  This instruction can also be used with the input 
      window (:class:`~chiplotle.hpgl.commands.IW`) instruction to 
      programmatically set the window to P1 and P2.
   '''
   

class OS(_HPGLPrimitive):
   '''
   :Output Status:
      Outputs the decimal value of the status byte. Use this instruction in 
      debugging operations and in digitizing applications.

   =========  ============  =========
   bit value  bit position  meaning
   =========  ============  =========
   1          0             pen down
   2          1             P1 or P2 changed ("OP" clears)
   4          2             digitized point ready ("OD" clears)
   8          3             initialized ("OS" clears)
   16         4             ready to recieve data (always 0)
   32         5             There is an error ("OE" clears)
   64         6             unused
   128        7             unused
   =========  ============  =========
   
   power-on status == 24 (bits 3 & 4 set)
   '''
   

class OT(_HPGLPrimitive):
   '''
   :Output Carousel Type:
      Outputs information on the type of carousel loaded and the 
      stalls occupied.
   '''
   

class OW(_HPGLPrimitive):
   '''
   :Output Window:
      Outputs the X,Y coordinates of the lower-left and upper-right 
      corners of the window area in which plotting can occur. 
      This instruction is especially useful when the window area 
      (defined by :class:`~chiplotle.hpgl.commands.IW`) extends beyond 
      the hard-clip limits.
   '''
   

class PB(_HPGLPrimitive):
   '''
   :Print Buffer Label:
      Prints the contents of the label buffer.
   '''
   
      
class PS(_HPGLPrimitive):
   '''
   :Page Size:
      Changes the size of the hard clip limits.
   '''

   def __init__(self, length = None, width = None):
      self.length = length
      self.width = width

   @property
   def format(self):
      if self.length and self.width:
         return '%s%i,%i%s' % (self._name, self.length, self.width, 
            _HPGLPrimitive._terminator)
      elif self.length:
         return '%s%i%s' % (self._name, self.length, _HPGLPrimitive._terminator)
      else:
         return '%s%s' % (self._name, _HPGLPrimitive._terminator)


class BL(_HPGLPrimitive):
   '''
   :Buffer label:
      Stores a label in the label buffer. You can then use the
      output length (:class:`~chiplotle.hpgl.commands.OL`) instruction 
      to determine its space requirement prior to drawing it. Or, you 
      can use the plot buffer (:class:`~chiplotle.hpgl.commands.PB`)
      instruction to repeatedly plot this label.
   '''

   def __init__(self, label=None):
      self.label = label

   @property
   def format(self):
      if self.label:
         return '%s%s%s' % (self._name, chr(3), _HPGLPrimitive._terminator)
      else:
         return '%s%s' % (self._name, _HPGLPrimitive._terminator)


class IN(_HPGLPrimitive):
   '''
   :Initialize:
      Resets most plotter functions to their default settings. Use this 
      instruction to return the plotter to a known state and to cancel 
      settings that may have been changed by a previous program. 
   '''
   

class SS(_HPGLPrimitive):
   '''
   :Select standard character set:

   '''
   

class XT(_HPGLPrimitive):
   '''
   :X tick:

   '''
   

class YT(_HPGLPrimitive):
   '''
   :Y tick:
   
   '''
   

class CS(_HPGLPrimitive):
   '''
   :Standard character set:
      Designates a character set as the standard character set for labeling 
      instruction. Use this instruction to change the default ANSI ASCII 
      english set to one with characters appropriate to your application. 
      This instruction is particularly useful if you plot most of your
      labels in a language other than english.
   '''
   def __init__(self, set=0):   
      self.set = set

   @property
   def format(self):
      return '%s%i%s' % (self._name, self.set, _HPGLPrimitive._terminator)


class CT(_HPGLPrimitive):
   '''
   :Chord tolerance:
      Determines whether the chord tolerance parameter of the 
      :class:`~chiplotle.hpgl.commands.CI`, 
      :class:`~chiplotle.hpgl.commands.AA`, 
      :class:`~chiplotle.hpgl.commands.AR`
      and :class:`~chiplotle.hpgl.commands.WG` instructions is 
      interpreted as a chord angle in degrees or as a deviation distance 
      in current units.

   - `type` : ``int`` 0 or 1, default 0. 

   '''
   def __init__(self, type=0):   
      self.type = type

   @property
   def format(self):
      return '%s%i%s' % (self._name, self.type, _HPGLPrimitive._terminator)


class CV(_HPGLPrimitive):
   '''
   :Curved line generator:
      Collects vectors (line segments) in the vector buffer so that they
      can be plotted as a group. This allows the plotter to plot in a
      continuous motion, rather than stopping and starting at each vector 
      endpoint. As a result, curves appear smoother. 
   
   - `n` : ``int`` 0 or 1, default 1 (on).
   - `inputdelay` : ``int`` [0 to 8,388,607] msec, default 100.
   '''

   def __init__(self, n=None, inputdelay=None):
      self.n = n
      self.inputdelay = inputdelay

   @property
   def format(self):
      if self.n and self.inputdelay:
         return '%s%i%i%s' % (self._name, self.n, self.inputdelay, 
         _HPGLPrimitive._terminator)
      elif self.n:
         return '%s%i%s' % (self._name, self.n, _HPGLPrimitive._terminator)
      else:
         return '%s%s' % (self._name, _HPGLPrimitive._terminator)
         

class CA(_HPGLPrimitive):
   '''
   :Designate alternate character set:
      Designates a character set as the alternate character set to be 
      used in labeling instructions. Use this instruction to provide an 
      additional character set that you can easily access in a program.
   
   - `set` : ``int`` [-1, 0 to 59, 60, 70, 80, 99, 100, 101], default 0.
   '''

   def __init__(self, set=0):   
      self.set = set

   @property
   def format(self):
      return '%s%i%s' % (self._name, self.set, _HPGLPrimitive._terminator)


class CM(_HPGLPrimitive):
   '''
   :Character selection mode:
      Specifies mode of character set selection and usage. Use this 
      instruction to select the alternate HP 8-bit, ISO 7-bit, or 
      ISO 8-bit character modes.

   - `switch` : ``int`` [0 to 3], default 0.
   - `fallback` : ``int`` 0 or 1, default 0.
   '''

   def __init__(self, switch=None, fallback=None):   
      self.switch = switch
      self.fallback = fallback

   @property
   def format(self):
      if self.switch and self.fallback:
         return '%s%i,%i%s' % (self._name, self.switch, self.fallback, 
         _HPGLPrimitive._terminator)
      elif self.switch:
         return '%s%i%s' % (self._name, self.switch, _HPGLPrimitive._terminator)
      else:
         return '%s%s' % (self._name, _HPGLPrimitive._terminator)


class CP(_HPGLPrimitive):
   '''
   :Character Plot:
      Move the pen the specified number of character plot cells from the
      current pen location.
   '''

   def __init__(self, spaces=None, lines=None):   
      self.spaces = spaces
      self.lines = lines

   @property
   def format(self):
      if self.spaces and self.lines:
         return '%s%s,%s%s' % (self._name, self.spaces, self.lines, 
         _HPGLPrimitive._terminator)
      elif self.spaces:
         return '%s%s%s' % (self._name, self.spaces, _HPGLPrimitive._terminator)
      else:
         return '%s%s' % (self._name, _HPGLPrimitive._terminator)


class DT(_HPGLPrimitive):
   '''
   :Define Label Terminator:
      Specifies the ASCII character to be used as the label terminator.
      Use this instruction to define a new label terminator if your 
      computer cannot use the default terminator (ETX, decimal code 3).
   '''

   def __init__(self, terminator=chr(3)):   
      self.labelterminator = terminator

   @property
   def format(self):
      return '%s%c%s' % (self._name, self.labelterminator, 
      _HPGLPrimitive._terminator)


class LB(_HPGLPrimitive):
   '''
   :Label:
      Plots text using the currently defined character set.
   '''

   def __init__(self, text):   
      self.text = text
      self.labelTerminator = chr(3)

   @property
   def format(self):
      return '%s%s%s%s' % (self._name, self.text, self.labelTerminator, 
         _HPGLPrimitive._terminator)


class SP(_HPGLPrimitive):
   '''
   :Select Pen:

   '''

   def __init__(self, pen = 0):   
      self.pen = pen

   @property
   def format(self):
      return '%s%i%s' % (self._name, self.pen, _HPGLPrimitive._terminator)


class LT(_HPGLPrimitive):
   '''
   :Line Type:
      Specifies the line pattern to be used when drawing linese and nonsolid
      fill types. Use LT to emphasize or de-emphasize other plotter lines and
      shapes.

   - `pattern` : ``int`` [-6 to 6]
   - `length` : ``float`` [0 to 100]

   =  ============================
   0  plot point at given point.
   1  .   .   .   .   .   .
   2  __   __   __   __   __
   3  ___ ___ ___ ___ ___
   4  __.__.__.__.__.__.
   5  ___ _ ___ _ ___ _ ___ _
   6  ___ _ _ ___ _ _ ___ _ _ ___
   =  ============================
   '''

   def __init__(self, pattern=None, length=4):   
      self.pattern = pattern
      self.length = length

   @property
   def format(self):
      if self.pattern:
         return '%s%i,%.4f%s' % (self._name, self.pattern, 
         self.length, _HPGLPrimitive._terminator)
      else:
         return '%s%s' % (self._name, _HPGLPrimitive._terminator)


class FT(_HPGLPrimitive):
   '''
   :Fill Type:
      Selects the shading pattern used in polygons 
      (:class:`~chiplotle.hpgl.commands.FP`), rectangles 
      (:class:`~chiplotle.hpgl.commands.RA` or 
      :class:`~chiplotle.hpgl.commands.RR`), or wedges 
      (:class:`~chiplotle.hpgl.commands.WG`). Use this instruction to 
      enhance plots with solid fill, parallel lines (hatching), 
      cross-hatching, or a fill pattern you designed using the 
      user-defined fill type (UF) instruction.
   
   - `type` : ``int`` 1 or 2,  Solid (space and angle ignored) \
      3:  Hatching, 4:  Cross hatching.
   '''

   def __init__(self, type=None, space=None, angle=None):   
      self.type = type
      self.space = space
      self.angle = angle

   @property
   def format(self):
      if not None in (self.type, self.space, self.angle):
         return '%s%i,%s,%s%s' % (self._name, self.type, self.space,
         self.angle, _HPGLPrimitive._terminator)
      elif not None in (self.type, self.space):
         return '%s%i,%s%s' % (self._name, self.type, self.space, 
         _HPGLPrimitive._terminator)
      elif not self.type is None:
         return '%s%i%s' % (self._name, self.type, _HPGLPrimitive._terminator)
      elif None == self.type == self.space == self.angle:
         return '%s%s' % (self._name, _HPGLPrimitive._terminator)
      else:
         ### TODO: raise this type of warning in all other commands where
         ### this may be necessary.
         raise(Warning("Can't format %s with given parameters." % self._name)) 


class PM(_HPGLPrimitive):
   '''
   :Polygon Mode:
      Enter polygon mode for defining shapes such as block letters, 
      logos, surface charts, or any unique or intricate area for 
      subsequent filling and/or edging. Fill polygons using the fill 
      polygon (FP) instruction and/or outline them using the edge polygon 
      (EP) instruction.
   '''
   def __init__(self, n = 0):   
      self.n = n

   @property
   def format(self):
      return '%s%i%s' % (self._name, self.n, _HPGLPrimitive._terminator)


class EC(_HPGLPrimitive):
   '''
   :Enable Cut Line:
      Draws a dashed cut line between 'pages' on roll paper to indicate 
      where to cut the paper. Used with 
      :class:`~chiplotle.hpgl.commands.AF`, 
      :class:`~chiplotle.hpgl.commands.AH` and 
      :class:`~chiplotle.hpgl.commands.PG` instructions.
   '''

   def __init__(self, n = 0):   
      self.n = n

   @property
   def format(self):
      return '%s%i%s' % (self._name, self.n, _HPGLPrimitive._terminator)


class PG(_HPGLPrimitive):
   '''
   :Page Feed:
      Advances roll paper one page length and establishes the plotter-unit 
      origin at the center of the new page.
   '''

   def __init__(self, n = None):   
      self.n = n

   @property
   def format(self):
      if self.n:
         return '%s%i%s' % (self._name, self.n, _HPGLPrimitive._terminator)
      else:
         return '%s%s' % (self._name, _HPGLPrimitive._terminator)


class GC(_HPGLPrimitive):
   '''
   :Group Count:
      Allows you to assign an arbitrary number that will be output by the 
      :class:`~chiplotle.hpgl.commands.OG` instruction. Use 
      :class:`~chiplotle.hpgl.commands.GC` with the 
      :class:`~chiplotle.hpgl.commands.OG` instruction to monitor the 
      successful transfer of data blocks in spooling applications.
   '''

   def __init__(self, count=None):   
      self.count = count

   @property
   def format(self):
      if not self.count is None:
         return '%s%i%s' % (self._name, self.count, _HPGLPrimitive._terminator)
      else:
         return '%s%s' % (self._name, _HPGLPrimitive._terminator)


### TODO implement these:
#class GM(_HPGLPrimitive):

#class GP(_HPGLPrimitive):

#class IM(_HPGLPrimitive):

class SL(_HPGLPrimitive):
   ''' 
   :Character Slant: 
      Argument is tan of desired angle.
   '''

   def __init__(self, tan = 0):   
      self.tan = tan

   @property
   def format(self):
      return '%s%.4f%s' % (self._name, self.tan, _HPGLPrimitive._terminator)


class SA(_HPGLPrimitive):
   '''
   :Select alternate character set:
   
   '''
   

class RO(_HPGLPrimitive):
   ''' 
   :Rotate coordinate system:
   
   '''

   def __init__(self, angle = 0):   
      self.angle = angle

   @property
   def format(self):
      return '%s%i%s' % (self._name, self.angle, _HPGLPrimitive._terminator)


class RP(_HPGLPrimitive):
   ''' 
   :Replot:  
   
   '''

   def __init__(self, n = 1):   
      self.n = n

   @property
   def format(self):
      return '%s%i%s' % (self._name, self.n, _HPGLPrimitive._terminator)


class SM(_HPGLPrimitive):
   ''' 
   :Symbol Mode:  
      Plots the char at each plotted point. 
      char can be any printing ascii char, except ';'
      Calling without an argument cancels symbol mode.
   '''

   def __init__(self, char = None):
      self.char = char

   @property
   def format(self):
      if self.char:
         return '%s%c%s' % (self._name, self.char, _HPGLPrimitive._terminator)
      else:
         return '%s%s' % (self._name, _HPGLPrimitive._terminator)


class SC(_TwoPoint):
   '''
   :Scale:
      Establishes a user-unit coordinate system by mapping user-defined
      values onto the scaling points P1 and P2. Thus, you can plot in 
      units convenient to your application. In addition, you can use this
      instruction to establish automatic isotropic scaling or to relocate
      the origin and set a specific ratio of plotter units to user units.
      
   .. note:: DraftMaster also has a more complex version of 'SC' that \
      is not implemented yet.
   '''

   def __init__(self, coords=None):
     _TwoPoint.__init__(self, coords) 


class IP(_TwoPoint):
   '''
   :Input P1 and P2:
      Allows you to establish new or default locations for the scaling 
      points P1 and P2. P1 and P2 are used by the scale instruction 
      (:class:`~chiplotle.hpgl.commands.SC`) 
      to establish user-unit scaling. 
      The :class:`~chiplotle.hpgl.commands.IP` instruction is often used to 
      ensure that a plot is always the same size, regardless of how P1 
      and P2 might have been set from the front panel or the size of media 
      loaded in the plotter.
   '''

   def __init__(self, coords=None):   
      if coords:
         assert len(coords) in (2, 4)
      _TwoPoint.__init__(self, coords) 


class IV(_HPGLPrimitive):
   '''
   :Invoke Character Slot:
      Invokes a character set slot into either the right or left half of 
      the in-use code table. Primarily used with ISO modes of character 
      selection.
   '''

   def __init__(self, slot=None, left=None):
      self.slot = slot
      self.left = left

   @property
   def format(self):
      if not None in (self.slot, self.left):
         return '%s%i%i%s' % (self._name, self.slot, self.left,
            _HPGLPrimitive._terminator)
      elif not self.slot is None:
         return '%s%i%s' % (self._name, self.slot, _HPGLPrimitive._terminator)
      elif self.slot == self.left == None:
         return '%s%s' % (self._name, _HPGLPrimitive._terminator)
      else:
         raise(Warning("Can't format %s with given parameters." % self._name)) 


class IW(_TwoPoint):
   '''
   :Input Window:
      Defines a rectangular area, or window, that establishes soft-clip 
      limits.  Subsequent programmed pen motion will be restricted to this 
      area. Use this instruction when you want to be sure that your plot 
      falls within a specified area.
   '''

   def __init__(self, coords=None):
      _TwoPoint.__init__(self, coords) 


### TODO this is the exact same pattern as that of all other commands with
### two parameters. Refactor.
class KY(_HPGLPrimitive):
   '''
   :Define Key:
      Assigns a predefined function to one of the frontal panel function 
      keys.  Use this instruction with the WD instruction when designing 
      interactive programs.
   '''

   def __init__(self, key=None, function=None):
      self.key = key
      self.function = left

   @property
   def format(self):
      if not None in (self.key, self.function):
         return '%s%i%i%s' % (self._name, self.key, self.function,
            _HPGLPrimitive._terminator)
      elif not self.key is None:
         return '%s%i%s' % (self._name, self.key, _HPGLPrimitive._terminator)
      elif self.key == self.function == None:
         return '%s%s' % (self._name, _HPGLPrimitive._terminator)
      else:
         raise(Warning("Can't format %s with given parameters." % self._name)) 


class PT(_HPGLPrimitive):
   '''
   :Pen Thickness:
      Determines the spacing between the parallel lines in solid fill 
      patterns, according to the pen tip thickness.

   - `thickness` : ``float`` [0.1 to 5] mm, default is 0.3mm.
   '''

   def __init__(self, thickness = 0.3):
      self.thickness = thickness

   @property
   def format(self):
      return '%s%.2f%s' % (self._name, self.thickness, _HPGLPrimitive._terminator)
      

class SI(_HPGLPrimitive):
   '''
   :Absolute character size:
      Specifies the size of labeling characters in centimeters. 
      Use this instruction to establish character sizing that is not 
      dependent on the settings of P1 and P2.

   - `width` : ``float`` [-110 to 110] cm, excluding 0. 
   - `height` : ``float`` [-110 to 110] cm, excluding 0. 
   '''

   def __init__(self, width = None, height = None):   
      assert width != 0
      assert height != 0

      self.width = width
      self.height = height

   @property
   def format(self):
      if self.width and self.height:
         return '%s%.2f,%.2f%s' % (self._name, self.width, self.height, 
            _HPGLPrimitive._terminator)
      elif None == self.width == self.height:
         return '%s%s' % (self._name, _HPGLPrimitive._terminator)
      else:
         raise(Warning("Can't format %s without all parameters." % self._name))


class SR(SI):
   '''
   :Relative character size:
      Specifies the relative size of characters as a percentage of the
      distance between P1 and P2. Use this instruction to establish
      relative character sizes so that if the P1/P2 distance changes,
      the character sizes adjust to occupy the same relative ammount of
      space.

   - `width` : ``float`` [-100 to 100] percent, excluding 0. 
   - `height` : ``float`` [-100 to 100] percent, excluding 0. 
   '''
   
      
class DI(_HPGLPrimitive):
   '''
   :Absolute direction:
      Specifies the direction in which labels are drawn, independent of
      P1 and P2 settings. Use this instruction to change labeling 
      direction when you are labeling line charts, schematic drawings, 
      blueprints, and survey boudaries.

   - `run` : ``float``. cos(angle)
   - `rise` : ``float``. sin(angle)
   '''

   def __init__(self, run=None, rise=None):
      self.run = run
      self.rise = rise

   @property
   def format(self):
      if not None in (self.run, self.rise):
         return '%s%.2f,%.2f%s' % (self._name, self.run, self.rise, 
         _HPGLPrimitive._terminator)
      elif None == self.run == self.rise:
         return '%s%s' % (self._name, _HPGLPrimitive._terminator)
      else:
         raise(Warning("Can't format %s without all parameters." % self._name))
         

class DR(DI):
   '''
   :Relative Direction:
      Specifies the direction in which labels are drawn relative to 
      the scaling points P1 and P2. Label direction is adjusted when 
      P1 and P2 change so that labels maintain the same relationship 
      to the plotted data. Use :class:`~chiplotle.hpgl.commands.DI` 
      if you want label direction to be independent or P1 and P2.

   - `run` : ``float``. cos(angle)
   - `rise` : ``float``. sin(angle)
   '''


### TODO: figure out how this works and implement.
#class DL(_HPGLPrimitive):
#   '''
#   Define Downloadable Character
#   Allows you to design characters and store them in a buffer for 
#   repeated use by character set -1.
#   SYNTAX: DL character number (,pen control), X-coordinate, Y-coordinate
#   (,..., (,pen control(,...,))); or DL character number; or DL;
#   '''
#   def __init__(self, charnumber, pencontrol, xy):
#      self.charnumber = charnumber
#      self.pencontrol = pencontrol
#      self.xy = xy


class DS(_HPGLPrimitive):
   '''
   :Designate Character Set into Slot:
      Designates up to four character sets to be immediately available for 
      plotting. Used with ISO character sets and modes.
   '''

   def __init__(self, slot=None, set=None):
      self.slot = slot
      self.set = set

   @property
   def format(self):
      if self.slot and self.set:
         return '%s%i,%i%s' % (self._name, self.slot, self.set, 
         _HPGLPrimitive._terminator)
      else:
         return '%s%s' % (self._name, _HPGLPrimitive._terminator)


class DV(_HPGLPrimitive):
   '''
   :Direction Vertical:
      Specifies vertical mode as the direction for subsequent labels.
      Use this instruction to 'stack' horizontal characters in a column.
      A carriage return and a line feed lace the next 'column' to the 
      left of the previous one. 
   '''

   def __init__(self, vertical=0):
      self.vertical = bool(vertical)

   @property
   def format(self):
      return '%s%i%s' % (self._name, self.vertical, _HPGLPrimitive._terminator)
         

class ES(_HPGLPrimitive):
   '''
   :Extra space:
      Adjust space between characters and lines of labels without affecting
      character size.

   - `charspace` : ``float``, ``None``. Spacing between characters.
   - `linespace` : ``float``, ``None``. Spacing between lines.

   Character and line spacing values add (or substract) a fraction of the 
   standard spacing. 0 is the standard, positive values increase
   space and negative values reduce space. 1 doubles the standard space,
   0.5 adds half the standard space, and -1 substracts the standar space,
   causing the characters to draw on top of each other.
   '''

   def __init__(self, charspace = None, linespace = None):
      self.charspace = charspace
      self.linespace = linespace

   @property
   def format(self):
      if not None in (self.charspace, self.linespace):
         return '%s%.2f,%.2f%s' % (self._name, self.charspace, self.linespace, 
            _HPGLPrimitive._terminator)
      elif not self.charspace is None:
         return '%s%.2f%s' % (self._name, self.charspace, _HPGLPrimitive._terminator)
      else:
         return '%s%s' % (self._name, _HPGLPrimitive._terminator)
         

class LO(_HPGLPrimitive):
   '''
   :Label Origin:
      Positions labels relative to current pen location. Use LO to center, 
      left justify, or right justify label. The label can be drawn above or
      below the current pen location and can also be offset by an amount equal 
      to 1/2 the character's width and height.
      
   - `origin` : ``int`` [1-9] or [11-19].
   '''

   def __init__(self, origin = 1):
      self.origin = origin

   @property
   def format(self):
      return '%s%i%s' % (self._name, self.origin, _HPGLPrimitive._terminator)


class EW(_HPGLPrimitive):
   '''
   :Edge Wedge:
      Outlines any wedge. Use these instructions to produce sectors of 
      a pie chart.

   - `radius` : ``float``. 
   - `startangle` : ``float`` [0 - 360] degrees.
   - `sweepangle` : ``float`` [0 - 360] degrees.
   - `chordangle` : ``float`` [0.36 - 50] degrees.
   '''

   _scalable = ['radius']

   def __init__(self, radius, startangle, sweepangle, chordangle=None):
      self.radius = radius
      self.startangle = startangle
      self.sweepangle = sweepangle
      self.chordangle = chordangle

   @property
   def format(self):
      if self.chordangle:
         return '%s%.2f,%.2f,%.2f,%.2f%s' % (self._name, self.radius, 
         self.startangle, self.sweepangle, self.chordangle, 
         _HPGLPrimitive._terminator)
      else:
         return '%s%.2f,%.2f,%.2f%s' % (self._name, self.radius, 
         self.startangle, self.sweepangle, _HPGLPrimitive._terminator)


class WG(EW):
   '''
   :Filled wedge:
   
   '''


class TL(_HPGLPrimitive):
   '''
   Length of ticks drawn with the XT and YT instructions.

   - `tp` : percentage of (P2y - P1y) for XT or (P2x - P1x) for YT. \
      Denotes portion above X-axis or to the right of the Y-axis when
       difference is positive.
   - `tn` : same as `tp` except denotes portion below the X-axis and to \
      the left of the Y-axis. 0.5 is default for both.
   '''

   def __init__(self, tp = 0.5, tn = 0.5):
      self.tp = tp
      self.tn = tn

   @property
   def format(self):
      return '%s%.4f,%.4f%s' % (self._name, self.tp, self.tn, _HPGLPrimitive._terminator)
        

class WD(_HPGLPrimitive):
   '''
   :Write to display:
   
   '''

   def __init__(self, text):
      self.text = text

   @property
   def format(self):
      return '%s%s%s' % (self._name, self.text, chr(3)) # no terminator??



### ESCAPES ###

class B(_HPGLEscape):
   '''
   :Escape output buffer space:
   
   '''
   

class On(_HPGLEscape):
   '''
   :On:
      Places the plotter in a programmed on-state.
      Instructs the plotter to interpret data as HPGL and DCI instructions, 
      rather than plotting the data stream as literal text characters.
   '''

   @property
   def _name(self):
      return '('
   

class Off(_HPGLEscape):
   '''
   :Off: 
      Places the plotter in a programmed off-state.
   '''
   @property
   def _name(self):
      return ')'


class ExtendedError(_HPGLEscape):
   '''
   :ExtendedError:
      Get RS-232-C related error message.

   =========  ========
   error num  meaning
   =========  ========
   0          no i/o error
   10         output request received while still processing previous one
   11         invalid byte received after escape sequence ("ESC.")
   12         invalid byte received as part of a device control instruction
   13         parameter out of range
   14         too many parameters received
   15         framing, parity, or overrun error
   16         input buffer overflow
   =========  ========
   
   '''
   @property
   def _name(self):
      return 'E'


class K(_HPGLEscape):
   '''
   :Abort command: 
      Tells the plotter to discard commands in its buffer.
   '''

class SetHandshakeMode(_HPGLEscape):
   '''
   :Set Handshake Mode:
      Set one of three standard handshakes.

   0 (none)
   1 (Xon-Xoff)
   2 (ENQ-ACK)
   3 (hardwire)
   '''
   def __init__(self, mode=None):   
      self.mode = mode

   @apply
   def mode( ):
      def fget(self):
         return self._mode
      def fset(self, mode):
         if not mode in (None, 0,1,2,3):
            raise ValueError('mode must be in (0,1,2,3).')
         self._mode = mode
      return property(**locals( ))
         
   @property
   def _name(self):
      return 'P'

   @property
   def format(self):
      if self.mode is None:
         return '%s.%s' % (self.escape, self._name)
      else:
         return '%s.%s%i' % (self.escape, self._name, self.mode)
