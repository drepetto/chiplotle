from chiplotle.hpgl.commands import PM, EP, FP, FT, SP
from chiplotle.geometry.core.path import Path
from chiplotle.tools.hpgltools.convert_coordinates_to_hpgl_absolute_path \
   import convert_coordinates_to_hpgl_absolute_path

class Polygon(Path):
   '''A closed path.'''

   def __init__(self, points, filled=False):  
      Path.__init__(self, points)
      self.filled = filled

   @property
   def _preformat_points(self):
      '''Points (coordinates) ready for formatting (conversion to HPGL).'''
      coords = self.points.xy
      coords.append(self.points.xy[0])
      return coords

   @property
   def _infix_commands(self):
      if Polygon.language == 'HPGL':
         path =  convert_coordinates_to_hpgl_absolute_path(self._preformat_points)
         #result = [PM(0)] + path + [PM(2), EP()]
         result = path[0:2] + [PM(0)] + path[2:] + [PM(2), EP()]
         if self.filled:
            result.append(FP())
         return result

      elif _Shape.language == 'gcode':
         print 'Sorry, no g-code support!'




if __name__ == '__main__':
   from chiplotle import io

   p = Polygon([(0, 0), (2000, 0), (1000, 1000), (0, 500), (0, 0)], 0)

   io.view(p)
