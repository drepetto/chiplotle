from chiplotle.hpgl.commands import PU, PA, PD
from chiplotle.geometry.coordinatearray import CoordinateArray

def convert_coordinates_to_hpgl_absolute_path(coords):
   '''Converts an iterator of lists of coordinates
   e.g., [<x1, y1>, <x2, y2>, <x3, y3>, ...]
   into a list of PA, PD and PU HPGL commands. 
   '''
   if not isinstance(coords, (list, tuple, CoordinateArray)):
      raise TypeError('`coords` must be a list of coordinates or CoordinateArray.')

   result = [ ]
   result.append(PU( ))
   result.append(PA(coords[0]))
   result.append(PD( ))
   result.append(PA(coords[1:]))
   return result