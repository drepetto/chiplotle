from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.scalable import Scalable
from chiplotle.hpgl.commands import PU, LB, PA, ES, LO, SL, DI, DV, SI

class Label(_CompoundHPGL):
   '''Text label.

   * `xy`: 2-tuple of coordinates pair for label location.
   * `text`: The actual text to be printed.
   * `charsize`:  2-tuple (w, h) pair defining the absolute character size.
   * `direction`: 2-tuple. The inclination / angle of the text: 
      run (direction on x axis), rise (direction on y axis).
   * `charspace`: Factor to set spacing between characters. 
      Positive separates, negatives bring together. 
   * `linespace`: Factor to set spacing between lines. 
      Positive separates, negatives bring together.
   * `origin`: location of label relative to pen's current location. 
      Possible values:

         ====== ===== ======= =======
         .      Left  Inside  Right
         ====== ===== ======= =======
         Above    3     6      9
         Inside   2     5      8
         Below    1     4      7
         ====== ===== ======= =======

         If 10 is added to the above-mentioned location number, positions 
         (except 5) will be offset towards the center by 1/2 the character 
         width and 1/2 the character height. 

   * `slant`: slant of characters (italic). Possible values: [0-1). 
      0 is vertical, 0.5 is 45 degs., ...
   * `vertical`: Print text from left to right (False) or top down (True).
   '''

   def __init__(self, xy, text):
      _CompoundHPGL.__init__(self, xy) 
      self.text = text
      self.charsize = None
      self.direction = None
      self.charspace = None
      self.linespace = None
      self.origin = None
      self.slant = None
      self.vertical = False


   @apply
   def charsize( ):
      def fget(self):
         return self._charsize
      def fset(self, arg):
         if isinstance(arg, (list, tuple, Scalable)):
            if len(arg) == 2:
               self._charsize = Scalable(arg)
            else:
               raise ValueError("Character size has two values: (w, h).")
         elif arg is None:
            self._charsize = None
         else:
            raise ValueError("charsize must be None, (x, y) pair, or Scalar.")
      return property(**locals())
            
         
            
   @property
   def _subcommands(self):
      result = _CompoundHPGL._subcommands.fget(self)
      ### set commands
      result += [PU( ), PA(self.xyabsolute)]
      if not self.charsize is None:
         result.append(SI(*self.charsize))
      if self.charspace and self.linespace:
         result.append(ES(self.charspace, self.linespace))
      if self.direction:
         result.append(DI(*self.direction))
      if self.origin:
         result.append(LO(self.origin))
      if self.slant:
         result.append(SL(self.slant))
      if self.vertical:
         result.append(DV(int(self.vertical)))

      result.append(LB(self.text))

      ### unset commands
      if not self.charsize is None:
         result.append(SI( ))
      if self.charspace and self.linespace:
         result.append(ES( ))
      if self.direction:
         result.append(DI( ))
      if self.origin:
         result.append(LO(1))
      if self.slant:
         result.append(SL( ))
      if self.vertical:
         result.append(DV(0))

      return result
