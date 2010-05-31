from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.commands import PA, PU, PD, AA, CI
from chiplotle.utils.geometry import polar2xy
import numpy

class _RadialHistogram(_CompoundHPGL):
   '''Abstract radial histogram class.'''

   _scalable = ['min_radius', 'max_radius']

   def __init__(self, xy, min_radius, max_radius, data, fill=False, 
      fillines_spacing=None, pen=None):
      _CompoundHPGL.__init__(self, xy, pen)
      self.min_radius = min_radius
      self.max_radius = max_radius
      self.fill = fill
      self.fillines_spacing = fillines_spacing
      self.data = data
      

   ## PRIVATE METHODS ##
   def _endpoints_from_angle(self, angle, data_value):
      '''given an angle, get the start and end points of a radial line.'''
      xy1 = numpy.array(polar2xy(self.min_radius, angle))
      v = data_value * (self.max_radius - self.min_radius) + self.min_radius
      xy2 = numpy.array(polar2xy(v, angle)) 
      return xy1, xy2

   ## PRIVATE PROPERTIES ##

   @property
   def _bin_angle_width(self):
      return 2 * numpy.pi / len(self.data)

   @property
   def _subcommands_outline(self):
      angle_per_bin_deg = 360.0 / len(self.data)
      result = [PA( )]
      for i, d in enumerate(self.data):
         ## edge 1...
         xy1a, xy2a = self._endpoints_from_angle(i * self._bin_angle_width, d)
         xy1b, xy2b = self._endpoints_from_angle((i+1) * self._bin_angle_width, d)
         result.append(PU(self.xyabsolute + xy1a))
         result.append(PD(self.xyabsolute + xy2a))
         ## edge 2...
         result.append(PU(self.xyabsolute + xy1b))
         result.append(PD(self.xyabsolute + xy2b))
         ## connecting arch...
         result.append(AA(self.xyabsolute, -angle_per_bin_deg))
      return result 

   @property
   def _subcommands_fill(self):
      '''define in subclasses.'''
      pass


   @property
   def _subcommands(self):
      result = _CompoundHPGL._subcommands.fget(self)
      result.append(PU(self.xyabsolute))
      ## draw min_radius circle...
      result.append(CI(self.min_radius))
      ## draw histogram outlines...
      result += self._subcommands_outline
      if self.fill:
         result += self._subcommands_fill
      return result

