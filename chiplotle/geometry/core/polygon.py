from chiplotle.geometry.core.path import Path

class Polygon(Path):
   '''A closed path.'''

   def __init__(self, points):  
      Path.__init__(self, points)

   @property
   def _preformat_points(self):
      '''Points (coordinates) ready for formatting (conversion to HPGL).'''
      coords = self.points.xy
      coords.append(self.points.xy[0])
      return coords
