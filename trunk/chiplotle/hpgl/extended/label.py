from chiplotle.hpgl.extended.extended import _ExtendedHPGL
from chiplotle.hpgl.commands import PU, LB, PA, ES, LO, SL, DI, DV, SI

class Label(_ExtendedHPGL):
   '''Text label.
   Settable properties:
   x, y:       coordinates of label location.
   text:       the actual text to be printed.
   charsize:   (w, h) pair defining the absolute character size.
   direction:  the inclination / angle of the text. Should be a pair of values: 
               run (direction on x axis), rise (direction on y axis).
   charspace:  spacing between characters. Positive separates, negatives bring 
               together.
   linespace:  spacing between lines. Positive separates, negatives bring together.
   origin:     location of label relative to pen's current location. Possible 
               values:
                     Left Inside Right
               Above   3     6     9
               Inside  2     5     8
               Below   1     4     7
               If 10 is added to the above-mentioned location number, positions 
               (except 5) will be offset towards the center by 1/2 the character 
               width and 1/2 the character height. 
   slant:      slant of characters (italic). Possible values: [0-1). 0 is vertical, 
               0.5 is 45 degs., ...
   vertical:   boolean; print text from left to right (False) or top down (True).
   '''

   def __init__(self, x, y, text):
      _ExtendedHPGL.__init__(self, (x, y)) 
      self.text = text
      self.charsize = None
      self.direction = None
      self.charspace = None
      self.linespace = None
      self.origin = None
      self.slant = None
      self.vertical = False


   @property
   def _subcommands(self):
      result = _ExtendedHPGL._subcommands.fget(self)
      ### set commands
      result += [PU( ), PA(self.xy)]
      if self.direction:
         result.append(DI(*self.direction))
      if self.charsize:
         result.append(SI(*self.charsize))
      if self.charspace and self.linespace:
         result.append(ES(self.charspace, self.linespace))
      if self.origin:
         result.append(LO(self.origin))
      if self.slant:
         result.append(SL(self.slant))
      if self.vertical:
         result.append(DV(int(self.vertical)))

      result.append(LB(self.text))

      ### unset commands
      if self.direction:
         result.append(DI( ))
      if self.charsize:
         result.append(SI( ))
      if self.charspace and self.linespace:
         result.append(ES( ))
      if self.origin:
         result.append(LO(1))
      if self.slant:
         result.append(SL( ))
      if self.vertical:
         result.append(DV(0))

      return result
