from chiplotle.hpgl.compound.histograms.radialhistogram import _RadialHistogram
from chiplotle.hpgl.commands import PA, PU, AA, PD
from chiplotle.utils.geometry import polar2xy

class RadialHistogramRF(_RadialHistogram):
   def __init__(self, xy, min_radius, max_radius, data, 
      chord=None, fill=False, fillines_spacing=50, pen=None):
      _RadialHistogram.__init__(self, xy, min_radius, max_radius, data,
      chord, fill, fillines_spacing, pen)


   ## PRIVATE PROPERTIES ##      

   @property
   def _subcommands_fill(self):
      '''radial fill with Absolute Angle (AA).'''
      angle_per_bin_deg = 360.0 / len(self.data)
      result = [PA( )] 
      for i, d in enumerate(self.data):
         length = d * (self.max_radius - self.min_radius) 
         for j in range(int(length / self.fillines_spacing) + 1):
            v = self.min_radius + j * self.fillines_spacing
            xy = polar2xy(v, i * self._bin_angle_width)
            result.append(PU(self.xyabsolute + xy))
            result.append(PD( ))
            result.append(AA(self.xyabsolute, angle_per_bin_deg))
      return result    

