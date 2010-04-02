from chiplotle.hpgl.compound.histograms.radialhistogram import _RadialHistogram
from chiplotle.hpgl.commands import PA, PU, PD 

class RadialHistogramLF(_RadialHistogram):
   '''A radial histogram with linear outward fill. The shape draws a circular
   histogram for the given list of relative frequencies. The bars of the
   histogram are filled 'linearly', i.e., with lines moving outwards from 
   the center.

   - `min_radius`: a scalar of the smallest radius of the histogram.
   - `max_radius`: a scalar of the maximum radius of the histogram.
   - `data`: a list of relative frequencies [x, y, z, ...]. Values are
      assumed to be between 0 and 1.
   - `fill`: a boolean that indicated whether the bars should be filled or not.
   - `fillines_spacing`: a scalar indicating the angle between fill lines, 
      in radians.
   '''
   def __init__(self, xy, min_radius, max_radius, data, fill=False, 
      fillines_spacing=0.01, pen=None):
      _RadialHistogram.__init__(self, xy, min_radius, max_radius, data,
      fill, fillines_spacing, pen)


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

