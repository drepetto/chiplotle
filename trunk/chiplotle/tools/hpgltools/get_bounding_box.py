from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.coordinatepair import CoordinatePair
from chiplotle.tools.hpgltools.get_all_coordinates import get_all_coordinates

def get_bounding_box(arg):
   '''Returns the pair of coordinate pairs outlining the bounding box or
   the given HPGL drawing.'''
   if not isinstance(arg, (list, tuple, _CompoundHPGL)):
      raise TypeError('arg must be list, tuple or _CompoundHPGL')

   min_x = min_y = 1000000.0
   max_x = max_y = -1000000.0
   
   coords = get_all_coordinates(arg)

   if len(coords) == 0:
      return None

   for c in coords:
      ## x...
      if c.x > max_x:
         max_x = c.x
      if c.x < min_x:
         min_x = c.x
      ## y...
      if c.y > max_y:
         max_y = c.y
      if c.y < min_y:
         min_y = c.y
   return (CoordinatePair(min_x, min_y), CoordinatePair(max_x, max_y))
