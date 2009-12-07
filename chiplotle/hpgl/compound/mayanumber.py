from __future__ import division
from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.commands import PU, PD, CI, PA, PR, RA, EA, WG
from chiplotle.tools import hpgltools
import copy

class MayaNumber(_CompoundHPGL):

   def __init__(self, xy, value, size=500):
      _CompoundHPGL.__init__(self, xy) 
      self.value = value
      self.size = size
      self.filled = False


   ### HELPERS ###
   
   @property
   def _interdigitSpace(self):
      return self.size / 8.

   @property
   def _maxExponent(self):
      for i in xrange(100):
         if self.value // 20**i == 0:
            return i - 1

   @property
   def _digitValues(self):
      digits = [ ]
      value = self.value
      maxe = self._maxExponent
      if maxe == -1: ### if zero
         return [0]
      for e in range(maxe, -1, -1):
         digit = value // 20**e
         digits.append(digit)
         value = (value - 20**e * digit) 
      return digits

   @property
   def _subcommands(self):
      result = _CompoundHPGL._subcommands.fget(self)
      x = self.xabsolute
      y = self.yabsolute + \
         (len(self._digitValues) - 1) * (self.size + self._interdigitSpace)
      for v in self._digitValues:
         result.extend( _MayaDigit(x, y, v, 
                        self.size, self.filled)._subcommands )
         y -= (self.size + self._interdigitSpace)
      return result
         

class _MayaDigit(object):

   def __init__(self, x, y, value, size, filled=False):
      assert value < 20
      self.x = x
      self.y = y
      self.value = value
      self.size = size
      self.filled = filled

   ### PROPERTIES ###

   @property
   def barHeight(self):
      return self.size / 4. / 1.75

   @property
   def barWidth(self):
      return self.size - self.size / 4.

   @property
   def dotRadius(self):
      #return self.size / 4. / 2. / 2.
      return self.barHeight / 2.

   @property
   def _subdigits(self):
      fives = self.value // 5
      ones = self.value % 5
      return (fives, ones)

   @property
   def _subcommands(self):
      result = [ ]
      fives, ones = self._subdigits
      ### if 0, draw zero
      if (ones == 0) and (fives == 0):
         x = self.x + self.size / 2. / 3.5
         y = self.y + self.size / 2.
         zero = copy.deepcopy(self._zero)
         hpgltools.scale(zero, self.size / 2000.)
         result = [PU( ), PA((x, y))]
         result.extend( zero )
         return result
         
      ### draw bars
      xref = self.x
      yref = self.y
      for i in range(fives):
         x1 = xref + self.size / 2. - self.barWidth / 2.
         y1 = yref + self.size / 4. / 2. - self.barHeight / 2.
         x2 = x1 + self.barWidth
         y2 = y1 + self.barHeight
         result.append( PU( ) )
         result.append( PA((x1, y1)) )
         if self.filled:
            result.append( RA((x2, y2)) )
         else:
            result.append( EA((x2, y2)) )
         yref += self.size / 4.
      ### draw circles
      spacing = self.size / (ones + 1)
      xref = self.x
      y = yref + self.size / 4. / 2.
      for i in range(ones):
         x = xref + spacing
         result.append( PA((x, y)) )
         if self.filled:
            result.append( WG(self.dotRadius, 0, 359, 10) )
         else:
            result.append( CI(self.dotRadius) )
         xref += spacing
      return result

   @property
   def _zero(self):
      return [PD(xy=[]), PR(xy=[133,118]), PR(xy=[157, 84]), PR(xy=[171, 51]), PR(xy=[178, 16]), PR(xy=[179,-16]), PR(xy=[171,-51]), PR(xy=[157,-84]), PR(xy=[ 133,-118]), PR(xy=[-133,-119]), PR(xy=[-153, -87]), PR(xy=[-169, -55]), PR(xy=[-176, -21]), PR(xy=[-177,  15]), PR(xy=[-172,  51]), PR(xy=[-159,  88]), PR(xy=[-140, 128]), PU(xy=[]), PR(xy=[97,93]), PD(xy=[]), PR(xy=[ 95,-53]), PR(xy=[133,-34]), PR(xy=[158,-19]), PR(xy=[170, -3]), PR(xy=[168,  9]), PR(xy=[154, 21]), PR(xy=[125, 30]), PR(xy=[85,39]), PU(xy=[]), PR(xy=[-590, 187]), PD(xy=[]), PR(xy=[ -80,-280]), PU(xy=[]), PR(xy=[257, -5]), PD(xy=[]), PR(xy=[-80,280]), PU(xy=[]), PR(xy=[-359,-261]), PD(xy=[]), PR(xy=[122,246]), PU(xy=[]), PR(xy=[386, -4]), PD(xy=[]), PR(xy=[ 115,-237]), PU()]


