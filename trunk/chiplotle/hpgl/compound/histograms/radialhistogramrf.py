from chiplotle.hpgl.compound.histograms.radialhistogram import _RadialHistogram
from chiplotle.hpgl.commands import PA, PU, AA, PD
from chiplotle.utils.geometry import polar2xy

class RadialHistogramRF(_RadialHistogram):
   '''A radial histogram with radial fill. The shape draws a circular
   histogram for the given list of relative frequencies. The bars of the
   histogram are filled 'radially', i.e., with arc shapes.

   - `min_radius`: a scalar of the smallest radius of the histogram.
   - `max_radius`: a scalar of the maximum radius of the histogram.
   - `data`: a list of relative frequencies [x, y, z, ...]. Values are
      assumed to be between 0 and 1.
   - `fill`: a boolean that indicated whether the bars should be filled or not.
   - `fillines_spacing`: a scalar indicating the spacing between fill lines.
   - `chord`: the chord tolerance of the arcs drawn.
   '''

   def __init__(self, xy, min_radius, max_radius, data, fill=False, 
      fillines_spacing=50, chord=None, pen=None):
      _RadialHistogram.__init__(self, xy, min_radius, max_radius, data,
      fill, fillines_spacing, pen)
      self.chord = chord


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
            result.append(AA(self.xyabsolute, angle_per_bin_deg, self.chord))
      return result    

