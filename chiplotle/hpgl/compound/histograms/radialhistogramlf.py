from chiplotle.hpgl.compound.histograms.radialhistogram import _RadialHistogram
from chiplotle.hpgl.commands import PA, PU, PD 

class RadialHistogramLF(_RadialHistogram):
   def __init__(self, xy, min_radius, max_radius, data, 
      chord=None, fill=False, fillines_spacing=0.01, pen=None):
      _RadialHistogram.__init__(self, xy, min_radius, max_radius, data,
      chord, fill, fillines_spacing, pen)


   ## PRIVATE PROPERTIES ##      

   @property
   def _subcommands_fill(self):
      '''linear outward fill.'''
      result = [PA( )] 
      for i, d in enumerate(self.data):
         for j in range(int(self._bin_angle_width / self.fillines_spacing)+1):
            xy1, xy2 = self._endpoints_from_angle(
               i * self._bin_angle_width + j * self.fillines_spacing, d)
            result.append(PU(self.xyabsolute + xy1))
            result.append(PD(self.xyabsolute + xy2))
      return result    

