from chiplotle.hpgl.commands import PA, PU, PD
from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.compound.label import Label
from chiplotle.hpgl.coordinatepair import CoordinatePair

class BusinessCard(_CompoundHPGL):
   '''A class for making simple presentation/business cards.
      
      - `logo`: is a single _CompoundHPGL instance to be placed in the card.
      - `texts`: is a list of Label instances containing text for the card.
   '''

   _scalable = _CompoundHPGL._scalable + ['width', 'height']

   def __init__(self, xy, logo, texts, width=None, height=None, pen=None):
      _CompoundHPGL.__init__(self, xy, pen)
      self.logo = logo
      self.texts = texts
      width = width or 3500 # int(round((3.5 - 1/16.) * 1016))
      height = height or 2000 # int(round((2.0 - 1/16.) * 1016))
      self.width = width
      self.height = height
      

   ## PUBLIC PROPERTIES ##

   @apply
   def logo( ):
      def fget(self):
         return self._logo
      def fset(self, logo):
         if isinstance(logo, _CompoundHPGL):
            self._logo = logo
            logo.parentage._switch(self)
         elif logo is None:
            self._logo = None
         else:
            raise TypeError('`logo` must be of type _CompoundHPGL or None.')
      return property(**locals( ))

   @apply
   def texts( ):
      def fget(self):
         return self._texts
      def fset(self, texts):
         if not isinstance(texts, (list, tuple)):
            raise TypeError('`texts` must be a list or tuple of Label instances.')
         for e in texts:
            if not isinstance(e, Label):
               raise TypeError('The text elements must be Label instances.')
         for e in texts:
            e.parentage._switch(self)
         self._texts = texts
      return property(**locals( ))

   @property
   def upper_left(self):
      return CoordinatePair(-self.width / 2.0, self.height / 2.0)

   @property
   def upper_right(self):
      return CoordinatePair(self.width / 2.0, self.height / 2.0)

   @property
   def lower_left(self):
      return CoordinatePair(-self.width / 2.0, -self.height / 2.0)

   @property
   def lower_right(self):
      return CoordinatePair(self.width / 2.0, -self.height / 2.0)

   ## PRIVATE PROPERTIES ##

   @property
   def _subcommands_corner_dots(self):
      result = [PU( )]
      result.append(PA(self.xyabsolute + self.upper_left))
      result += [PD( ), PU( )]
      result.append(PA(self.xyabsolute + self.upper_right))
      result += [PD( ), PU( )]
      result.append(PA(self.xyabsolute + self.lower_left))
      result += [PD( ), PU( )]
      result.append(PA(self.xyabsolute + self.lower_right))
      result += [PD( ), PU( )]
      return result

   @property
   def _subcommands(self):
      result = _CompoundHPGL._subcommands.fget(self)
      result += self._subcommands_corner_dots
      result.extend(self.texts)
      result.append(self.logo)
      return result
