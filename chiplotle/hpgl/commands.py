from chiplotle.hpgl.abstract.arc import _Arc
from chiplotle.hpgl.abstract.charsize import _CharSize
from chiplotle.hpgl.abstract.hpglcommand import _HPGLCommand
from chiplotle.hpgl.abstract.hpglescape import _HPGLEscape
from chiplotle.hpgl.abstract.positional import _Positional
from chiplotle.hpgl.abstract.twopoint import _TwoPoint
from chiplotle.hpgl.abstract.wedge import _Wedge
from chiplotle.hpgl.scalable import Scalable

class PU(_Positional):
   '''Pen Up. x,y coordinates are absolute.'''
   def __init__(self, xy=None):
      _Positional.__init__(self, xy, True)

class PD(_Positional):
   '''Pen Down. x,y coordinates are absolute.'''
   def __init__(self, xy=None):
      _Positional.__init__(self, xy, True)

class PA(_Positional):
   '''Pen Absolute'''
   def __init__(self, xy=None):
      _Positional.__init__(self, xy, True)

class PR(_Positional):
   '''Pen Relative'''
   def __init__(self, xy=None):
      _Positional.__init__(self, xy, False)

class CI(_HPGLCommand):
   '''Circle'''
   def __init__(self, radius, chordangle=11.25):   
      self.radius = Scalable(radius)
      self.chordangle = chordangle

   def __str__(self):
      return '%s%.4f,%d%s' % (self._name, self.radius, self.chordangle, self.terminator)

class CC(_HPGLCommand):
   '''Character chord angle???'''
   def __init__(self, angle=5):   
      self.angle = int(angle)

   def __str__(self):
      return '%s%d%s' % (self._name, self.angle, self.terminator)

class AF(_HPGLCommand):
   '''Advance full page.'''
   pass

class AH(_HPGLCommand):
   '''Advance half page.'''
   pass

class AP(_HPGLCommand):
   """
      Automatic Pen operations
      for 7550:
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
   """
   def __init__(self, p=''):   
      if p != '':
         self.p = int(p)
      else:
         self.p = p

   def __str__(self):
      return '%s%s%s' % (self._name, self.p, self.terminator)

class AR(_Arc):
   '''Arch Relative'''
   def __init__(self, xy, a, chordangle=5):
      _Arc.__init__(self, xy, a, chordangle, False)

class AA(_Arc):
   '''Arch Absolute'''
   def __init__(self, xy, a, chordangle=5):
      _Arc.__init__(self, xy, a, chordangle, True)

class AS(_HPGLCommand):
   """
      Acceleration Select
      Can be set per-pen or for all pens at once.

      default on 7550: 6
      default on DM: 4
   """
   def __init__(self, accel=None, pen=None):   
      self.accel = accel
      self.pen = pen

   def __str__(self):
      if self.accel:
         if self.pen:
            return '%s%d,%d%s' \
            % (self._name, self.accel, self.pen, self.terminator)
         else:
            return '%s%d%s' % (self._name, self.accel, self.terminator)  
      else:
         return '%s%s' % (self._name, self.terminator) 

class EA(_Positional):
   """Edge Rectangle Absolute."""
   def __init__(self, xy):
      assert type(xy) in (tuple, list) and len(xy) == 2
      _Positional.__init__(self, xy, True)

class ER(_Positional):
   """Edge Rectangle Relative."""
   def __init__(self, xy):
      assert type(xy) in (tuple, list) and len(xy) == 2
      _Positional.__init__(self, xy, False)

class FS(_HPGLCommand):
   """Set tip force for pen. 
      force range is 1-8
      pen range is 1-8
      if pen == None then all pens are set to force
   """
   def __init__(self, force = None, pen = None):
      self.force = force
      self.pen = pen

   def __str__(self):

      if self.force is None:
         return '%s%s' % (self._name, self.terminator)
      elif self.pen:
         return '%s%d,%d%s' % (self._name, self.force, self.pen, self.terminator)
      else:
         return '%s%d%s' % (self._name, self.force, self.terminator)


class RA(_Positional):
   """Filled Rectangle Absolute."""
   def __init__(self, xy):
      assert type(xy) in (tuple, list) and len(xy) == 2
      _Positional.__init__(self, xy, True)

class RR(_Positional):
   """Filled Rectangle Relative."""
   def __init__(self, xy):
      assert type(xy) in (tuple, list) and len(xy) == 2
      _Positional.__init__(self, xy, False)

class VS(_HPGLCommand):
   """ 
      Pen Velocity.
      v valid range: 0.0-127.9999 (depends on plotter)
      default depends on plotter and carousel type
      pen valid range: 1-8
   """
   def __init__(self, *args):
      ### this can be simpler/cleaner 
      self.vel = self.pen = None
      if len(args) == 1:
         self.vel = args[0]
      elif len(args) == 2:
         self.vel = args[0]
         self.pen = args[1]
     
   def __str__(self):
      if self.pen == None:
         if self.vel == None:
            return '%s%s' % (self._name, self.terminator)
         else:
            return '%s%d%s' % (self._name, self.vel, self.terminator)
      else:
         return '%s%d,%d%s' % (self._name, self.vel, 
                         self.pen, self.terminator)

class EP(_HPGLCommand):
   '''Edge Polygon.'''
   def __str__(self):
      return '%s%s' % (self._name, self.terminator)

class BF(_HPGLCommand):
   '''Buffer plot.'''
   pass

class DC(_HPGLCommand):
   '''Clear Digitizer.'''
   pass

class DF(_HPGLCommand):
   '''Default Instructions.'''
   pass

class DP(_HPGLCommand):
   '''Digitize Points.'''
   pass

class FP(_HPGLCommand):
   '''Fill Polygon.'''
   pass

class FR(_HPGLCommand):
   '''Advance Frame.'''
   pass

class NR(_HPGLCommand):
   '''Not Ready.'''
   pass

class OA(_HPGLCommand):
   """
      Returns current actual position of pen.
      X, Y, P (0 = PU, 1 = PD)
   """
   pass

class OC(_HPGLCommand):
   """
      Returns commanded position of pen.
      X, Y, P (0 = PU, 1 = PD)
   """
   pass

class OD(_HPGLCommand):
   """
      Returns last digitized point.
      X, Y, P (0 = PU, 1 = PD)
   """
   pass

class OE(_HPGLCommand):
   """
      Return first HP-GL error.
      #'s 0-8, excluding 4 and 7
      
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
      
      
      NOTE: some error meanings change depending on the plotter!
   """
   pass

class OF(_HPGLCommand):
   """
      dog ass me.
      Always outputs '40,40', which means that there are 40 plotter units/mm
   """
   pass

class OH(_HPGLCommand):
   """Return hard limits of plotter"""
   pass

class OI(_HPGLCommand):
   """Get ID of plotter."""
   pass

class OK(_HPGLCommand):
   '''Output key.'''
   pass

class OL(_HPGLCommand):
   '''Output label length.'''
   pass

class OO(_HPGLCommand):
   '''Output options.'''
   pass

class OP(_HPGLCommand):
   '''Get P1 & P2.'''
   pass

class OS(_HPGLCommand):
   """
      Return plotter status.
      
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
      
      but these may be different on different plotters...
   """
   pass

class OT(_HPGLCommand):
   '''Output carousel type.'''
   pass

class OW(_HPGLCommand):
   """
     Output window.
     Return xLL, yLL, xUR, yUR in plotter coords.
   """
   pass

class PB(_HPGLCommand):
   '''Print buffered label.'''
   pass
      
class PS(_HPGLCommand):
   """
       Paper Size
       0-3 == B or A3 size paper
       4-127 == A or A4 size paper
       WTF?
   """
   def __init__(self, size = None):
      self.size = size

   def __str__(self):
      if self.size:
         return '%s%d%s' % (self._name, self.size, self.terminator)
      else:
         return '%s%s' % (self._name, self.terminator)

class BL(_HPGLCommand):
   """
      Stores first 150 chars of text in buffer for later printing
      and label length measurements.
   """
   def __init__(self, label=None):
      self.label = label

   def __str__(self):
      if not self.label:
         return '%s%s' % (self._name, self.terminator)
      else:
         return '%s%s%s' % (self._name, chr(3), self.terminator)

class IN(_HPGLCommand):
   '''Initialize.'''
   pass


class SS(_HPGLCommand):
   '''Select standard character set.'''
   pass

class XT(_HPGLCommand):
   '''X tick.'''
   pass

class YT(_HPGLCommand):
   '''Y tick.'''
   pass

class CS(_HPGLCommand):
   '''Character set.'''
   def __init__(self, set = 0):   
      self.set = set

   def __str__(self):
      return '%s%d%s' % (self._name, self.set, self.terminator)

class CT(_HPGLCommand):
   '''Chord tolerance.'''
   def __init__(self, type = 0):   
      self.type = type

   def __str__(self):
      return '%s%d%s' % (self._name, self.type, self.terminator)

class CA(_HPGLCommand):
   '''Alternative(?) character set.'''
   def __init__(self, n = 0):   
      self.n = n

   def __str__(self):
      return '%s%d%s' % (self._name, self.n, self.terminator)

class CM(_HPGLCommand):
   '''Character select mode.'''
   def __init__(self, switch=0, fallback=0):   
      self.switch = switch
      self.fallback = fallback

   def __str__(self):
      return '%s%d,%d%s' % (self._name, self.switch, self.fallback, self.terminator)

class CP(_HPGLCommand):
   """
      Move the pen the specified number of spaces and lines
      valid values are -128 to 128
      CP by itself does CR & LF
   """
   def __init__(self, spaces=None, lines=None):   
      self.spaces = spaces
      self.lines = lines

   def __str__(self):
      if self.spaces:
         if self.fallback:
            return '%s%.4f,%.4f%s' % (self._name, \
            self.spaces, self.lines, self.terminator)
         else:
            return '%s%.4f%s' % (self._name, self.spaces, self.terminator)
            
      else:
         return '%s%s' % (self._name, self.terminator)

class DT(_HPGLCommand):
   """Define Label terminator."""
   def __init__(self, terminator = chr(3)):   
      self.labelTerminator = terminator

   def __str__(self):
      return '%s%c%s' % (self._name, self.labelTerminator, self.terminator)

class LB(_HPGLCommand):
   """Print text 'label'."""
   def __init__(self, text):   
      self.text = text
      self.labelTerminator = chr(3)

   def __str__(self):
      return '%s%s%s%s' % (self._name, self.text, self.labelTerminator, self.terminator)

class SP(_HPGLCommand):
   """Select Pen."""
   def __init__(self, pen = 0):   
      self.pen = pen

   def __str__(self):
      return '%s%d%s' % (self._name, self.pen, self.terminator)

class LT(_HPGLCommand):
   """Define line type:  
   0:  plot point at given point.
   1:  .   .   .   .   .   .
   2:  __   __   __   __   __
   3:  ___ ___ ___ ___ ___
   4:  __.__.__.__.__.__.
   5:  ___ _ ___ _ ___ _ ___ _
   6:  ___ _ _ ___ _ _ ___ _ _ ___
   """
   def __init__(self, pattern=None, length=4):   
      self.pattern = pattern
      self.length = length

   def __str__(self):
      if self.pattern:
         return '%s%d,%.4f%s' % (self._name, self.pattern, 
         self.length, self.terminator)
      else:
         return '%s%s' % (self._name, self.terminator)

class FT(_HPGLCommand):
   """ Set fill type:
   1:  Solid (space and angle ignored)
   2:  Solid too? (space and angle ignored)
   3:  Hatching
   4:  Cross hatching
   """
   def __init__(self, type = 1, space=None, angle=0):   
      self.type = type
      self.space = space
      self.angle = angle

   def __str__(self):
      if self.space:
         return '%s%d,%.4f,%d%s' % (self._name, self.type, self.space,
         self.angle, self.terminator)
      else:
         return '%s%d%s' % (self._name, self.type, self.terminator)

class PM(_HPGLCommand):
   """Plot polygon."""
   def __init__(self, n = 0):   
      self.n = n

   def __str__(self):
      return '%s%d%s' % (self._name, self.n, self.terminator)

class EC(_HPGLCommand):
   """Enable cut line."""
   def __init__(self, n = 0):   
      self.n = n

   def __str__(self):
      return '%s%d%s' % (self._name, self.n, self.terminator)

class PG(_HPGLCommand):
   """Page feed."""
   def __init__(self, n = None):   
      self.n = n

   def __str__(self):
      if self.n:
         return '%s%d%s' % (self._name, self.n, self.terminator)
      else:
         return '%s%s' % (self._name, self.terminator)

class SL(_HPGLCommand):
   """ Character Slant. Argument is tan of desired angle.  """
   def __init__(self, tan = 0):   
      self.tan = tan

   def __str__(self):
      return '%s%.4f%s' % (self._name, self.tan, self.terminator)

class SA(_HPGLCommand):
   '''Select alternate character set.'''
   pass

class RO(_HPGLCommand):
   """ Rotate coordinate system.  """
   def __init__(self, angle = 0):   
      self.angle = angle

   def __str__(self):
      return '%s%d%s' % (self._name, self.angle, self.terminator)

class RP(_HPGLCommand):
   """ Replot.  """
   def __init__(self, n = 1):   
      self.n = n

   def __str__(self):
      return '%s%d%s' % (self._name, self.n, self.terminator)

class SM(_HPGLCommand):
   """ Symbol Mode.  Plots the char at each plotted point. 
       char can be any printing ascii char, except ';'
       Calling without an argument cancels symbol mode.
   """
   def __init__(self, char = None):
      self.char = char

   def __str__(self):
      if self.char:
         return '%s%c%s' % (self._name, self.char, self.terminator)
      else:
         return '%s%s' % (self._name, self.terminator)

class SC(_TwoPoint):
   """Scale.
      NOTE: DraftMaster also has a more complex version 
      of 'SC' that is not implemented yet...
   """
   def __init__(self, coords=None):
     _TwoPoint.__init__(self, coords) 


class IW(_TwoPoint):
   """ Set plotting window.  """
   def __init__(self, coords=None):
      _TwoPoint.__init__(self, coords) 


class IP(_TwoPoint):
   """Set P1 & P2 scaling points"""
   def __init__(self, coords=None):   
      if coords:
         assert len(coords) in (2, 4)
      _TwoPoint.__init__(self, coords) 


class PT(_HPGLCommand):
   """
      Pen Thickness
      0.1mm < thickness < 5.0mm
   """
   def __init__(self, thickness = 0.3):
      self.thickness = thickness

   def __str__(self):
      return '%s%.4f%s' % (self._name, self.thickness, self.terminator)
      

class SI(_CharSize):
   """Absolute character size.
      Default values are width = 0.285cm, height=0.375cm"""
   pass

class SR(_HPGLCommand):
   '''Relative character size.'''
   pass
      
class DI(_HPGLCommand):
   '''Absolute direction of label.'''
   def __init__(self, run = None, rise = None):
      self.run = run
      self.rise = rise

   def __str__(self):
      if self.run and self.rise:
         return '%s%.4f%.4f%s' % (self._name, self.run, self.rise, self.terminator)
      else:
         return '%s%s' % (self._name, self.terminator)
         
class RD(_HPGLCommand):
   '''Relative direction of label.'''
   def __init__(self, run = None, rise = None):
      self.run = run
      self.rise = rise

   def __str__(self):
      if self.run and self.rise:
         return '%s%.4f%.4f%s' % (self._name, self.run, self.rise, self.terminator)
      else:
         return '%s%s' % (self._name, self.terminator)
         
class DV(_HPGLCommand):
   '''Print label vertically (top down).'''
   def __init__(self, vertical = 0):
      self.vertical = bool(vertical)

   def __str__(self):
      return '%s%i%s' % (self._name, self.vertical, self.terminator)
         
class ES(_HPGLCommand):
   '''Extra space. Defines character space and line space for labels.'''
   def __init__(self, charspace = None, linespace = None):
      self.charspace = charspace
      self.linespace = linespace

   def __str__(self):
      if self.charspace and self.linespace:
         return '%s%.4f%.4f%s' % (self._name, self.charspace, self.linespace, 
            self.terminator)
      else:
         return '%s%s' % (self._name, self.terminator)
         
class LO(_HPGLCommand):
   '''Label origin.'''
   def __init__(self, origin = 1):
      self.origin = origin

   def __str__(self):
      return '%s%i%s' % (self._name, self.origin, self.terminator)

class WG(_Wedge):
   '''Filled wedge.'''

class EW(_Wedge):
   '''Outlined wedge.'''


class TL(_HPGLCommand):
   '''Length of ticks drawn with the XT and YT instructions.'''

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

   def __str__(self):
      return '%s%.4f,%.4f%s' % (self._name, self.tp, self.tn, self.terminator)
        

class WD(_HPGLCommand):
   '''Write to display'''
   def __init__(self, text):
      self.text = text

   def __str__(self):
      return '%s%s%s' % (self._name, self.text, chr(3)) # no terminator??



### ESCAPES ###

class B(_HPGLEscape):
   '''Escape output buffer space.'''
   pass

class On(_HPGLEscape):
   """
      Places the plotter in a programmed on-state.
      
      old description (from where?):
      Instructs the plotter to interpret data as HPGL and DCI instructions, 
      rather than plotting the data stream as literal text characters.
   """
   @property
   def _name(self):
      return '('
   
class Off(_HPGLEscape):
   """
      Places the plotter in a programmed off-state
   """
   @property
   def _name(self):
      return ')'

class ExtendedError(_HPGLEscape):
   """
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
      
   """
   @property
   def _name(self):
      return 'E'

class K(_HPGLEscape):
   """Abort command: Tells the plotter to discard commands in its buffer."""
   pass


