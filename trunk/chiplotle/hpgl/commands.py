from chiplotle.hpgl.abstract.arc import _Arc
from chiplotle.hpgl.abstract.charsize import _CharSize
from chiplotle.hpgl.abstract.hpglcommand import _HPGLCommand
from chiplotle.hpgl.abstract.hpglescape import _HPGLEscape
from chiplotle.hpgl.abstract.positional import _Positional
from chiplotle.hpgl.abstract.twopoint import _TwoPoint
from chiplotle.hpgl.abstract.wedge import _Wedge
from chiplotle.hpgl.scalable import Scalable
from chiplotle.utils.ispair import ispair

class PU(_Positional):
   '''
   Pen Up.
   Raises the pen from the plotting surface. Use this instruction to prevent
   stray lines from being drawn.
   SYNTAX: PU X,Y(,...); or PU;
   '''
   def __init__(self, xy=None):
      _Positional.__init__(self, xy, True)


class PD(_Positional):
   '''
   Pen Down.
   Lowers the pen onto the writing surface for drawing and moves it to the 
   coordinates/increments you specified.
   SYNTAX: PD X,Y (,...); or PD;
   '''
   def __init__(self, xy=None):
      _Positional.__init__(self, xy, True)


class PA(_Positional):
   '''
   Plot Absolute.
   Establishes absolute plotting and moves the pen to specified absolute
   coordinates using the current pen position.
   SYNTAX: PA X,Y (,...); or PA;
   '''
   def __init__(self, xy=None):
      _Positional.__init__(self, xy, True)


class PR(_Positional):
   '''
   Plot Relative.
   Establishes relative plotting and moves the pen (using the current 
   position) to the specified points, each successive move relative to the
   last current pen location.
   SYNTAX: PR X,Y (,...) or PR;
   '''
   def __init__(self, xy=None):
      _Positional.__init__(self, xy, False)


class CI(_HPGLCommand):
   '''
   Circle.
   Draws a circle using the specified radius and chord tolerance. 
   If you want a filled circle, refer to the WB or PM instruction.
   SYNTAX: CI radius(, chord tolerance);
   '''
   def __init__(self, radius, chordangle=None):   
      self.radius = radius
      self.chordangle = chordangle

   @apply
   def radius( ):
      def fget(self):
         return self._radius
      def fset(self, arg):
         ### TODO: check for type here?
         self._radius = Scalable(arg)
      return property(**locals( ))

   @property
   def format(self):
      if self.chordangle:
         return '%s%s,%s%s' % (self._name, self.radius, self.chordangle, 
                              self.terminator)
      else:
         return '%s%s%s' % (self._name, self.radius, self.terminator)


class CC(_HPGLCommand):
   '''
   Character chord angle.
   Sets the chord angle that determines the smoothness of characters
   drawn when you select one of the arc-font character sets for labeling.
   SYNTAX: CC chord angle; or CC;
   '''
   def __init__(self, angle=None):   
      self.angle = angle

   @property
   def format(self):
      if self.angle:
         return '%s%i%s' % (self._name, self.angle, self.terminator)
      else:
         return '%s%s' % (self._name, self.terminator)


class AF(_HPGLCommand):
   '''
   Advance full page.
   Advances roll paper one full page length and establishes the 
   origin at the center of the new page.
   SYNTAX: AF;
   '''
   

class AH(_HPGLCommand):
   '''
   Advance half page.
   Advances roll paper one half page length and establishes the 
   origin at the center of the new page.
   SYNTAX: AH;
   '''
   

class AP(_HPGLCommand):
   '''
   Automatic Pen operations.
   Controls automatic pen operations sich as returning a pen
   to the carousel if it has been in the holder without drawing
   for a certain time.
   SYNTAX: AP; or AP n;

   For 7550:
   bit_no dec_val state meaning
   0     1      1    lift pen if down too long without motion
   0     0      0    do not lift pen until PU received
   1     2      1    put pen away if too long without  motion
   1     0      0    do not put pen away until SP0 received
   2     4      1    do not get new pen until drawing starts
   2     0      0    get pen immediately after SP command
   3     8      1    merge all pen up moves
   3     0      0    do not merge all pen up moves

   default is 7 on 7550
   codes are 0 to 255 with default of 95 on the DraftMaster
   '''
   def __init__(self, n=None):   
      self.n = n

   @property
   def format(self):
      if self.n:
         return '%s%i%s' % (self._name, self.n, self.terminator)
      else:
         return '%s%s' % (self._name, self.terminator)
         

class AA(_Arc):
   '''
   Arch Absolute.
   Draws an arc, using absolute coordinates, that starts at the
   current pen location and uses the specified center point.
   SYNTAX: AA X,Y,arc angle(,chord tolerance);
   '''
   def __init__(self, xy, angle, chordtolerance=None):
      _Arc.__init__(self, xy, angle, chordtolerance, True)


class AR(_Arc):
   '''
   Arch Relative.
   Draws an arc, using relative coordinates, that starts at the
   current pen location and uses the specified center point.
   SYNTAX: AR X,Y,arc angle(,chord tolerance);
   '''
   def __init__(self, xy, angle, chordtolerance=None):
      _Arc.__init__(self, xy, angle, chordtolerance, False)


class AS(_HPGLCommand):
   '''
   Acceleration Select.
   Sets pen acceleration for one or all pens. The default
   acceleration is suitable for all recommended pen and media
   combinations. Slowing the acceleration may improve line
   quality if you are using heavier than recommended media.
   SYNTAX: AS pen acceleration (, pen number); or AS;
   '''
   def __init__(self, accel=None, pen=None):   
      self.accel = accel
      self.pen = pen

   @property
   def format(self):
      if self.accel and self.pen:
         return '%s%i,%i%s' % (self._name, self.accel, self.pen, 
                              self.terminator)
      elif self.accel:
         return '%s%i%s' % (self._name, self.accel, self.terminator)  
      else:
         return '%s%s' % (self._name, self.terminator) 


### TODO: remove redundancy in rectangles.
class EA(_Positional):
   '''
   Edge Rectangle Absolute.
   Defines and outlines a rectangle using absolute coordinates.
   SYNTAX: EA X,Y;
   '''
   def __init__(self, xy):
      if not ispair(xy):
         raise ValueError('xy position must be of length 2.')
      _Positional.__init__(self, xy, True)


class ER(_Positional):
   '''
   Edge Rectangle Relative.
   Defines and outlines a rectangle using relative coordinates.
   SYNTAX: ER X,Y;
   '''
   def __init__(self, xy):
      if not ispair(xy):
         raise ValueError('xy position must be of length 2.')
      _Positional.__init__(self, xy, False)


class RA(_Positional):
   '''
   Filled Rectangle Absolute.
   '''
   def __init__(self, xy):
      if not ispair(xy):
         raise ValueError('xy position must be of length 2.')
      _Positional.__init__(self, xy, True)


class RR(_Positional):
   '''
   Filled Rectangle Relative.
   '''
   def __init__(self, xy):
      if not ispair(xy):
         raise ValueError('xy position must be of length 2.')
      _Positional.__init__(self, xy, False)


class VS(_HPGLCommand):
   ''' 
   Pen Velocity.
   v valid range: 0.0-127.9999 (depends on plotter)
   default depends on plotter and carousel type
   pen valid range: 1-8
   '''
   def __init__(self, vel=None, pen=None):
      self.vel = vel
      self.pen = pen
     
   @property
   def format(self):
      if self.vel and self.pen:
         return '%s%i,%i%s' % (self._name, self.vel, self.pen, self.terminator)
      elif self.vel:
         return '%s%i%s' % (self._name, self.vel, self.terminator)
      else:
         return '%s%s' % (self._name, self.terminator)


class FS(_HPGLCommand):
   '''
   Force Select.
   Sets pen pressure to the paper for one or all pens. Use this instruction
   to optimize pen life and line quality for each pen and paper combination.
   Force range is 1-8
   Pen range is 1-8
   If pen is None then all pens are set.
   '''
   def __init__(self, force=None, pen=None):
      self.force = force
      self.pen = pen

   @property
   def format(self):
      if self.force and self.pen:
         return '%s%i,%i%s' % (self._name, self.force, self.pen, 
                              self.terminator)
      elif self.force:
         return '%s%i%s' % (self._name, self.force, self.terminator)
      else:
         return '%s%s' % (self._name, self.terminator)


class EP(_HPGLCommand):
   '''
   Edge Polygon.
   Outlines the polygin currently stored in the polygon buffer. 
   Use this instruction to edge polygons that you defined in polygon mode 
   (PM) and with the rectangle and wedge instructions (RA, RR and WG).
   SYNTAX: EP;
   '''


class BF(_HPGLCommand):
   '''
   Buffer plot.
   '''
   

class DC(_HPGLCommand):
   '''
   Digitizer Clear.
   Terminates digitize mode. For example, if you are using an interrupt
   routine in a digitizing program to branch to another plotting function,
   use DC to clear the digitize mode immediately after branching. 
   SYNTAX: DC;
   '''
   

class DF(_HPGLCommand):
   '''
   Default.
   Sets certain plotter functions to predefined default conditions.
   Use this instruction to return the plotter to a known state while 
   maintaining the current location of P1 and P2. When you use DF at 
   the beginning of a program, unwanted graphics parameters such as
   character size, slant, or scaling are not inherited from another
   program. 
   SYNTAX: DF;
   '''
   

class DP(_HPGLCommand):
   '''
   Digitize Point.
   Returns the X,Y coordinates of a selected point on a plot to the
   computer for later use. Use this instruction to input data for a
   graphics program or to obtain the coordinates of a point or points
   on plot.
   SYNTAX: DP;
   '''
   

class FP(_HPGLCommand):
   '''
   Fill Polygon.
   Fills the polygon currently in the polygon buffer. Use FP to fill
   polygons defined in polygon mode (PM) and defined with the edge 
   rectangle and wedge instructions (EA, ER, and EW).
   SYNTAX: FP;
   '''
   

class FR(_HPGLCommand):
   '''
   Advance Frame.
   Advances paper to the next plot frame and calculates a relative 
   coordinate system for that frame. Use FR to do multi-frame long-axis 
   plotting.
   SYNTAX: FP;
   '''
   

class NR(_HPGLCommand):
   '''
   Not Ready.
   Programmatically simulates pressing VIEW.
   However, you cannot take the plotter out of the view state with NR
   instruction.
   SYNTAX: NR;
   '''
   

class OA(_HPGLCommand):
   '''
   Output Actual Pen Status.
   Outputs the current pen location (in plotter units) and up/down position.
   Use this information to position a label or figure, to determine the
   parameters of a window, or to determine the pen's curent location if you 
   moved it using front-panel cursor buttons.
   SYNTAX: OA;
   '''
   

class OC(_HPGLCommand):
   '''
   Output Commanded Pen Status.
   Ouput the location and up/down position of the last commanded pen move 
   instruction. Use OC to position a label or determine the parameters of
   an instruction that tried to move the pen beyond the limits of some window.
   You can also use this instruction when you want to know the pen's location
   in user units.
   SYNTAX: OC;
   '''
   

class OD(_HPGLCommand):
   '''
   Output Digitized Point and Pen Status.
   Outputs the X,Y coordinates and up/down pen position associated with the
   last digitized point. Use this instruction after the DP instruction to
   return the coordinates of the digitized point to your computer.
   SYNTAX: OD;
   '''
   

class OE(_HPGLCommand):
   '''
   Output Error.
   Output a number corresponding to the type of HP-GL error (if any) received
   by the plotter after the most recent IN or OE instruction. Use this 
   instruction for debugging programs. 
   
   bit value   error no   meaning
   0         0         no error
   1         1         unrecognized command
   2         2         wrong num of parameters
   4         3         out-of-range parameter
   8         4         unused
   16        5         unknown character set
   32        6         position overflow
   64        7         unused
   128       8         pinch wheels raised
   
   SYNTAX: OE;
   
   NOTE: some error meanings change depending on the plotter!
   '''
   

class OF(_HPGLCommand):
   '''
   Output Factors.
   Outputs the number of plotter units per millimeter in each axis. This
   lets you use the plotter with sofware that needs to know the size of a
   plotter unit.
   SYNTAX: OF;
   '''
   

class OG(_HPGLCommand):
   '''
   Output Group Count.
   Outputs the data block number of the current group count and whether the 
   escape function has been activated. Use this instruction at the end of a
   data block in spooling applications, where it is important to know the 
   current data block number and whether the data block has been transferred.
   SYNTAX: OG;
   '''


class OH(_HPGLCommand):
   '''
   Output Hard-Clip Limits.
   Outputs the X,Y coordinates of the current hard-clip limits. Use this 
   instruction to determine the plotter unit dimension of the area in which 
   plotting can occur.
   SYNTAX: OH;
   '''
   

class OI(_HPGLCommand):
   '''
   Output Identification.
   Outputs the plotter's identifying model number. This information is useful
   in a remote operating configuration to determine which plotter model is
   on-line, or when software needs the plotter's model number.
   SYNTAX: OI;
   ''' 


class OK(_HPGLCommand):
   '''
   Output Key.
   Outputs a number that indicates which, if any, of the front-panel function
   keys has been pressed. use this instruction with the WD instruction when
   designing interactive programs.
   SYNTAX: OK;
   '''
   

class OL(_HPGLCommand):
   '''
   Output Label Length.
   Outputs information about the label contained in the label buffer.
   SYNTAX: OL;
   '''


class OO(_HPGLCommand):
   '''
   Output Options.
   Outputs eight option parameters indicating the features implemented on 
   the plotter. Some software packages use this feature to determine which 
   plotter capabilities exist.
   SYNTAX: OO;
   '''
   

class OP(_HPGLCommand):
   '''
   Output P1 and P2.
   Outputs the X,Y coordinates (in plotter units) of the current scaling 
   points P1 and P2. Use this instruction to determine the numberic 
   coordinates or P1 and P2 when they have been set manually, and to help 
   compute the number of plotter units per user units when scaling is on.
   This instruction can also be used with the input window (IW) instruction
   to programmatically set the window to P1 and P2.
   SYNTAX: OP;
   '''
   

class OS(_HPGLCommand):
   '''
   Output Status.
   Outputs the decimal value of the status byte. Use this instruction in 
   debugging operations and in digitizing applications.

   bit value   bit position   meaning
   1         0            pen down
   2         1            P1 or P2 changed ("OP" clears)
   4         2            digitized point ready ("OD" clears)
   8         3            initialized ("OS" clears)
   16        4            ready to recieve data (always 0)
   32        5            There is an error ("OE" clears)
   64        6            unused
   128       7            unused
   
   power-on status == 24 (bits 3 & 4 set)
   
   SYNTAX: OS; 
   '''
   

class OT(_HPGLCommand):
   '''
   Output Carousel Type.
   Outputs information on the type of carousel loaded and the stalls occupied.
   SYNTAX: OT;
   '''
   

class OW(_HPGLCommand):
   '''
   Output Window.
   Outputs the X,Y coordinates of the lower-left and upper-right corners of 
   the window area in which plotting can occur. This instruction is especially
   useful when the window area (defined by IW) extends beyond the hard-clip
   limits.
   SYNTAX: OW;
   '''
   

class PB(_HPGLCommand):
   '''
   Print Buffer Label.
   Prints the contents of the label buffer.
   SYNTAX: PB;
   '''
   
      
class PS(_HPGLCommand):
   '''
   Page Size.
   Changes the size of the hard clip limits.
   SYNTAX: PS length(,width); or PS;
   '''
   def __init__(self, length = None, width = None):
      self.length = length
      self.width = width

   @property
   def format(self):
      if self.length and self.width:
         return '%s%i,%i%s' % (self._name, self.length, self.width, 
            self.terminator)
      elif self.length:
         return '%s%i%s' % (self._name, self.length, self.terminator)
      else:
         return '%s%s' % (self._name, self.terminator)


class BL(_HPGLCommand):
   '''
   Buffer label.
   Stores a label in the label buffer. You can then use the
   output length (OL) instruction to determine its space requirement 
   prior to drawing it. Or, you can use the plot buffer (PB)
   instruction to repeatedly plot this label.
   SYNTAX: BL c...c CHR$(3) or BL CHR$(3)
   '''
   def __init__(self, label=None):
      self.label = label

   @property
   def format(self):
      if self.label:
         return '%s%s%s' % (self._name, chr(3), self.terminator)
      else:
         return '%s%s' % (self._name, self.terminator)


class IN(_HPGLCommand):
   '''
   Initialize.
   Resets most plotter functions to their default settings. Use this 
   instruction to return the plotter to a known state and to cancel settings
   that may have been changed by a previous program. 
   SYNTAX: IN; or IN-1 (what is this -1);
   '''
   

class SS(_HPGLCommand):
   '''
   Select standard character set.
   '''
   

class XT(_HPGLCommand):
   '''
   X tick.
   '''
   

class YT(_HPGLCommand):
   '''
   Y tick.
   '''
   

class CS(_HPGLCommand):
   '''
   Standard character set.
   Designates a character set as the standard character set for labeling 
   instruction. Use this instruction to change the default ANSI ASCII 
   english set to one with characters appropriate to your application. 
   This instruction is particularly useful if you plot most of your
   labels in a language other than english.
   SYNTAX: CS set; or CS;
   '''
   def __init__(self, set=0):   
      self.set = set

   @property
   def format(self):
      return '%s%i%s' % (self._name, self.set, self.terminator)


class CT(_HPGLCommand):
   '''
   Chord tolerance.
   Determines whether the chord tolerance parameter of the CI, AA, AR
   and WG instructions is interpreted as a chord angle in degrees or as
   a deviation distance in current units.
   SYNTAX: CT n; or CT;
   '''
   def __init__(self, type=0):   
      self.type = type

   @property
   def format(self):
      return '%s%i%s' % (self._name, self.type, self.terminator)


class CV(_HPGLCommand):
   '''
   Curved line generator.
   Collects vectors (line segments) in the vector buffer so that they
   can be plotted as a group. This allows the plotter to plot in a
   continuous motion, rather than stopping and starting at each vector 
   endpoint. As a result, curves appear smoother. 
   SYNTAX: CV n(,input delay); or CV;
   '''
   def __init__(self, n=None, inputdelay=None):
      self.n = n
      self.inputdelay = inputdelay

   @property
   def format(self):
      if self.n and self.inputdelay:
         return '%s%i%i%s' % (self._name, self.n, self.inputdelay, 
         self.terminator)
      elif self.n:
         return '%s%i%s' % (self._name, self.n, self.terminator)
      else:
         return '%s%s' % (self._name, self.terminator)
         

class CA(_HPGLCommand):
   '''
   Alternative character set.
   Designates a character set as the alternate character set to be used
   in labeling instructions. Use this instruction to provide an 
   additional character set that you can easily access in a program.
   SYNTAX: CA set; or CA;
   '''
   def __init__(self, n=0):   
      self.n = n

   @property
   def format(self):
      return '%s%i%s' % (self._name, self.n, self.terminator)


class CM(_HPGLCommand):
   '''
   Character selection mode.
   Specifies mode of character set selection and usage. Use this 
   instruction to select the alternate HP 8-bit, ISO 7-bit, or ISO 8-bit
   character modes.
   SYNTAX: CM switch mode(, fallback mode); or CM;
   '''
   def __init__(self, switch=None, fallback=None):   
      self.switch = switch
      self.fallback = fallback

   @property
   def format(self):
      if self.switch and self.fallback:
         return '%s%i,%i%s' % (self._name, self.switch, self.fallback, 
         self.terminator)
      elif self.switch:
         return '%s%i%s' % (self._name, self.switch, self.terminator)
      else:
         return '%s%s' % (self._name, self.terminator)


class CP(_HPGLCommand):
   '''
   Character Plot.
   Move the pen the specified number of character plot cells from the
   current pen location.
   SYNTAX: CP spaces, lines; or CP;
   '''
   def __init__(self, spaces=None, lines=None):   
      self.spaces = spaces
      self.lines = lines

   @property
   def format(self):
      if self.spaces and self.lines:
         return '%s%s,%s%s' % (self._name, self.spaces, self.lines, 
         self.terminator)
      elif self.spaces:
         return '%s%s%s' % (self._name, self.spaces, self.terminator)
      else:
         return '%s%s' % (self._name, self.terminator)


class DT(_HPGLCommand):
   '''
   Define Label Terminator.
   Specifies the ASCII character to be used as the label terminator.
   Use this instruction to define a new label terminator if your computer
   cannot use the default terminator (ETX, decimal code 3).
   SYNTAX: DT label terminator; or DT;
   '''
   def __init__(self, terminator=chr(3)):   
      self.labelterminator = terminator

   @property
   def format(self):
      return '%s%c%s' % (self._name, self.labelterminator, self.terminator)


class LB(_HPGLCommand):
   '''
   Label.
   Plots text using the currently defined character set.
   SYNTAX: LB c...c CHR$(3)
   '''
   def __init__(self, text):   
      self.text = text
      self.labelTerminator = chr(3)

   @property
   def format(self):
      return '%s%s%s%s' % (self._name, self.text, self.labelTerminator, 
         self.terminator)


class SP(_HPGLCommand):
   '''
   Select Pen.
   '''
   def __init__(self, pen = 0):   
      self.pen = pen

   @property
   def format(self):
      return '%s%i%s' % (self._name, self.pen, self.terminator)


class LT(_HPGLCommand):
   '''
   Line Type.
   Specifies the line pattern to be used when drawing linese and nonsolid
   fill types. Use LT to emphasize or de-emphasize other plotter lines and
   shapes.
   Parameter   Format   Range 
   pattern     integer  -6 to 6
   length      real     0 to 100

   0:  plot point at given point.
   1:  .   .   .   .   .   .
   2:  __   __   __   __   __
   3:  ___ ___ ___ ___ ___
   4:  __.__.__.__.__.__.
   5:  ___ _ ___ _ ___ _ ___ _
   6:  ___ _ _ ___ _ _ ___ _ _ ___

   SYNTAX: LT patter(,length); or LT
   '''
   def __init__(self, pattern=None, length=4):   
      self.pattern = pattern
      self.length = length

   @property
   def format(self):
      if self.pattern:
         return '%s%i,%.4f%s' % (self._name, self.pattern, 
         self.length, self.terminator)
      else:
         return '%s%s' % (self._name, self.terminator)


class FT(_HPGLCommand):
   '''
   Fill Type.
   Selects the shading pattern used in polygons (FP), rectangles (RA or RR),
   or wedges (WG). Use this instruction to enhance plots with solid fill,
   parallel lines (hatching), cross-hatching, or a fill pattern you designed
   using the user-defined fill type (UF) instruction.
   1 or 2:  Solid (space and angle ignored)
   3:  Hatching
   4:  Cross hatching
   SYNTAX: FT type (,spacing(,angle)); or FT;
   '''
   def __init__(self, type=None, space=None, angle=None):   
      self.type = type
      self.space = space
      self.angle = angle

   @property
   def format(self):
      if not None in (self.type, self.space, self.angle):
         return '%s%i,%s,%s%s' % (self._name, self.type, self.space,
         self.angle, self.terminator)
      elif not None in (self.type, self.space):
         return '%s%i,%s%s' % (self._name, self.type, self.space, 
         self.terminator)
      elif not self.type is None:
         return '%s%i%s' % (self._name, self.type, self.terminator)
      elif None == self.type == self.space == self.angle:
         return '%s%s' % (self._name, self.terminator)
      else:
         ### TODO: raise this type of warning in all other commands where
         ### this may be necessary.
         raise(Warning("Can't format %s with given parameters." % self._name)) 


class PM(_HPGLCommand):
   '''
   Polygon Mode.
   Enter polygon mode for defining shapes such as block letters, logos, 
   surface charts, or any unique or intricate area for subsequent filling 
   and/or edging. Fill polygons using the fill polygon (FP) instruction and/or
   outline them using the edge polygon (EP) instruction.
   SYNTAX: PM n; or PM;
   '''
   def __init__(self, n = 0):   
      self.n = n

   @property
   def format(self):
      return '%s%i%s' % (self._name, self.n, self.terminator)


class EC(_HPGLCommand):
   '''
   Enable Cut Line.
   Draws a dashed cut line between 'pages' on roll paper to indicate where 
   to cut the paper. Used with AF, AH and PG instructions.
   SYNTAX: EC; or EC n;
   '''
   def __init__(self, n = 0):   
      self.n = n

   @property
   def format(self):
      return '%s%i%s' % (self._name, self.n, self.terminator)


class PG(_HPGLCommand):
   '''
   Page Feed.
   Advances roll paper one page length and establishes the plotter-unit origin
   at the center of the new page.
   SYNTAX: PG (n); or PG;
   '''
   def __init__(self, n = None):   
      self.n = n

   @property
   def format(self):
      if self.n:
         return '%s%i%s' % (self._name, self.n, self.terminator)
      else:
         return '%s%s' % (self._name, self.terminator)


class GC(_HPGLCommand):
   '''
   Group Count.
   Allows you to assign an arbitrary number that will be output by the OG
   instruction. Use GC with the OG instruction to monitor the successful
   transfer of data blocks in spooling applications.
   SYNTAX; GC count number; or GC;
   '''
   def __init__(self, count=None):   
      self.count = count

   @property
   def format(self):
      if not self.count is None:
         return '%s%i%s' % (self._name, self.count, self.terminator)
      else:
         return '%s%s' % (self._name, self.terminator)


### TODO implement these:
#class GM(_HPGLCommand):

#class GP(_HPGLCommand):

#class IM(_HPGLCommand):

class SL(_HPGLCommand):
   ''' 
   Character Slant. Argument is tan of desired angle.
   '''
   def __init__(self, tan = 0):   
      self.tan = tan

   @property
   def format(self):
      return '%s%.4f%s' % (self._name, self.tan, self.terminator)


class SA(_HPGLCommand):
   '''
   Select alternate character set.
   '''
   

class RO(_HPGLCommand):
   ''' 
   Rotate coordinate system.  
   '''
   def __init__(self, angle = 0):   
      self.angle = angle

   @property
   def format(self):
      return '%s%i%s' % (self._name, self.angle, self.terminator)


class RP(_HPGLCommand):
   ''' 
   Replot.  
   '''
   def __init__(self, n = 1):   
      self.n = n

   @property
   def format(self):
      return '%s%i%s' % (self._name, self.n, self.terminator)


class SM(_HPGLCommand):
   ''' 
   Symbol Mode.  
   Plots the char at each plotted point. 
   char can be any printing ascii char, except ';'
   Calling without an argument cancels symbol mode.
   '''
   def __init__(self, char = None):
      self.char = char

   @property
   def format(self):
      if self.char:
         return '%s%c%s' % (self._name, self.char, self.terminator)
      else:
         return '%s%s' % (self._name, self.terminator)


class SC(_TwoPoint):
   '''
   Scale.
   NOTE: DraftMaster also has a more complex version 
   of 'SC' that is not implemented yet...
   '''
   def __init__(self, coords=None):
     _TwoPoint.__init__(self, coords) 


class IP(_TwoPoint):
   '''
   Input P1 and P2.
   Allows you to establish new or default locations for the scaling points 
   P1 and P2. P1 and P2 are used by the scale instruction (SC) to establish
   user-unit scaling. The IP instruction is often used to ensure that a plot
   is always the same size, regardless of how P1 and P2 might have been set
   from the front panel or the size of media loaded in the plotter.
   SYNTAX: IP p1_x, p1_y(, p2_x, p2_y); or IP;
   '''
   def __init__(self, coords=None):   
      if coords:
         assert len(coords) in (2, 4)
      _TwoPoint.__init__(self, coords) 


class IV(_HPGLCommand):
   '''
   Invoke Character Slot.
   Invokes a character set slot into either the right or left half of the
   in-use code table. Primarily used with ISO modes of character selection.
   SYNTAX: IV (slot(,left));
   '''
   def __init__(self, slot=None, left=None):
      self.slot = slot
      self.left = left

   @property
   def format(self):
      if not None in (self.slot, self.left):
         return '%s%i%i%s' % (self._name, self.slot, self.left,
            self.terminator)
      elif not self.slot is None:
         return '%s%i%s' % (self._name, self.slot, self.terminator)
      elif self.slot == self.left == None:
         return '%s%s' % (self._name, self.terminator)
      else:
         raise(Warning("Can't format %s with given parameters." % self._name)) 

class IW(_TwoPoint):
   '''
   Input Window.
   Defmines a rectangular area, or window, that establishes soft-clip limits.
   Subsequent programmed pen motion will be restricted to this area. Use this
   instruction when you want to be sure that your plot falls within a 
   specified area.
   SYNTAX: IW X1,Y1,X2,Y2; or IW;
   '''
   def __init__(self, coords=None):
      _TwoPoint.__init__(self, coords) 


### TODO this is the exact same pattern as that of all other commands with
### two parameters. Refactor.
class KY(_HPGLCommand):
   '''
   Define Key.
   Assigns a predefined function to one of the frontal panel function keys.
   Use this instruction with the WD instruction when designing interactive
   programs.
   SYNTAX: KY key(,function); or KY;
   '''
   def __init__(self, key=None, function=None):
      self.key = key
      self.function = left

   @property
   def format(self):
      if not None in (self.key, self.function):
         return '%s%i%i%s' % (self._name, self.key, self.function,
            self.terminator)
      elif not self.key is None:
         return '%s%i%s' % (self._name, self.key, self.terminator)
      elif self.key == self.function == None:
         return '%s%s' % (self._name, self.terminator)
      else:
         raise(Warning("Can't format %s with given parameters." % self._name)) 

class PT(_HPGLCommand):
   '''
   Pen Thickness.
   Determines the spacing between the parallel lines in solid fill patterns,
   according to the pen tip thickness.
   Parameter   Format   Range    Default
   thickness   real  0.1 to 5mm  0.3mm
   '''
   def __init__(self, thickness = 0.3):
      self.thickness = thickness

   @property
   def format(self):
      return '%s%.4f%s' % (self._name, self.thickness, self.terminator)
      

class SI(_CharSize):
   '''
   Absolute character size.
   Default values are width = 0.285cm, height=0.375cm
   '''
   

class SR(_HPGLCommand):
   '''
   Relative character size.
   '''
   
      
class DI(_HPGLCommand):
   '''
   Absolute direction.
   Specifies the direction in which labels are drawn, independent of
   P1 and P2 settings. Use this instruction to change labeling direction
   when you are labeling line charts, schematic drawings, blueprints, 
   and survey boudaries.
   run is cos(angle)
   rise is sin(angle)
   SYNTAX: DI run, rise; or DI;
   '''
   def __init__(self, run=None, rise=None):
      self.run = run
      self.rise = rise

   @property
   def format(self):
      if not None in (self.run, self.rise):
         return '%s%s,%s%s' % (self._name, self.run, self.rise, 
         self.terminator)
      elif None == self.run == self.rise:
         return '%s%s' % (self._name, self.terminator)
      else:
         raise(Warning("Can't format %s with given parameters." % self._name)) 
         

class DR(DI):
   '''
   Relative Direction.
   Specifies the direction in which labels are drawn relative to the
   scaling points P1 and P2. Label direction is adjusted when P1 and P2
   change so that labels maintain the same relationship to the plotted
   data. Use DI if you want label direction to be independent or P1 and P2.
   SYNTAX: DR run, rise; or DR;
   '''


### TODO: figure out how this works and implement.
#class DL(_HPGLCommand):
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


class DS(_HPGLCommand):
   '''
   Designate Character Set into Slot.
   Designates up to four character sets to be immediately available for 
   plotting. Used with ISO character sets and modes.
   SYNTAX: DS slot,set; or DS;
   '''
   def __init__(self, slot=None, set=None):
      self.slot = slot
      self.set = set

   @property
   def format(self):
      if self.slot and self.set:
         return '%s%i,%i%s' % (self._name, self.slot, self.set, 
         self.terminator)
      else:
         return '%s%s' % (self._name, self.terminator)


class RD(_HPGLCommand):
   '''
   Relative direction of label.
   '''
   def __init__(self, run = None, rise = None):
      self.run = run
      self.rise = rise

   @property
   def format(self):
      if self.run and self.rise:
         return '%s%.4f,%.4f%s' % (self._name, self.run, self.rise, 
            self.terminator)
      else:
         return '%s%s' % (self._name, self.terminator)
         

class DV(_HPGLCommand):
   '''
   Direction Vertical.
   Specifies vertical mode as the direction for subsequent labels.
   Use this instruction to 'stack' horizontal characters in a column.
   A carriage return and a line feed lace the next 'column' to the left 
   of the previous one. 
   SYNTAX: DV n; or DV;
   '''
   def __init__(self, vertical=0):
      self.vertical = bool(vertical)

   @property
   def format(self):
      return '%s%i%s' % (self._name, self.vertical, self.terminator)
         

class ES(_HPGLCommand):
   '''
   Extra space.
   Adjust space between characters and lines of labels without affecting
   character size.
   SYNTAX: ES spaces (,lines); or ES;
   '''
   def __init__(self, charspace = None, linespace = None):
      self.charspace = charspace
      self.linespace = linespace

   @property
   def format(self):
      if not None in (self.charspace, self.linespace):
         return '%s%.4f,%.4f%s' % (self._name, self.charspace, self.linespace, 
            self.terminator)
      elif not self.charspace is None:
         return '%s%.4f%s' % (self._name, self.charspace, self.terminator)
      else:
         return '%s%s' % (self._name, self.terminator)
         

class LO(_HPGLCommand):
   '''
   Label Origin.
   Positions labels relative to current pen location. Use LO to center, 
   left justify, or right justify label. The label can be drawn above or
   below the current pen location and can also be offset by an amount equal 
   to 1/2 the character's width and height.
   origin = [1-9] or [11-19]
   SYNTAX: LO origin; or LO;
   '''
   def __init__(self, origin = 1):
      self.origin = origin

   @property
   def format(self):
      return '%s%i%s' % (self._name, self.origin, self.terminator)


class WG(_Wedge):
   '''
   Filled wedge.
   '''


class EW(_Wedge):
   '''
   Edge Wedge.
   Outlines any wedge. Use these instructions to produce sectors of a pie
   chart.
   SYNTAX: EW radius, start angle, sweep angle (,chord tolerance);
   '''


class TL(_HPGLCommand):
   '''
   Length of ticks drawn with the XT and YT instructions.
   '''

   def __init__(self, tp = 0.5, tn = 0.5):
      '''
         tp: percentage of (P2y - P1y) for XT or (P2x - P1x) for YT
             Denotes portion above X-axis or to the right of the Y-axis when
             difference is positive.
         tn: same as tp except denotes portion below the X-axis and to the left
             of the Y-axis
         0.5 is default for both
      '''
      self.tp = tp
      self.tn = tn

   @property
   def format(self):
      return '%s%.4f,%.4f%s' % (self._name, self.tp, self.tn, self.terminator)
        

class WD(_HPGLCommand):
   '''
   Write to display.
   '''
   def __init__(self, text):
      self.text = text

   @property
   def format(self):
      return '%s%s%s' % (self._name, self.text, chr(3)) # no terminator??



### ESCAPES ###

class B(_HPGLEscape):
   '''
   Escape output buffer space.
   '''
   

class On(_HPGLEscape):
   '''
   Places the plotter in a programmed on-state.
   old description (from where?):
   Instructs the plotter to interpret data as HPGL and DCI instructions, 
   rather than plotting the data stream as literal text characters.
   '''
   @property
   def _name(self):
      return '('
   

class Off(_HPGLEscape):
   '''
   Places the plotter in a programmed off-state.
   '''
   @property
   def _name(self):
      return ')'


class ExtendedError(_HPGLEscape):
   '''
   Get RS-232-C related error message.
   0 == no error
   10-16 == error
   
   error num   meaning
   0         no i/o error
   10        output request received while still processing previous one
   11        invalid byte received after escape sequence ("ESC.")
   12        invalid byte received as part of a device control instruction
   13        parameter out of range
   14        too many parameters received
   15        framing, parity, or overrun error
   16        input buffer overflow
   
   '''
   @property
   def _name(self):
      return 'E'


class K(_HPGLEscape):
   '''
   Abort command: Tells the plotter to discard commands in its buffer.
   '''
